from flask import Flask, g, render_template, request, redirect, url_for, flash, session
import mysql.connector
from datetime import timedelta


from models.usuario import Usuario
from models.usuarioDAO import UsuarioDAO
from models.exemplar import Exemplar
from models.exemplarDAO import ExemplarDAO
from models.livro import Livro
from models.livroDAO import LivroDAO
from models.emprestimo import Emprestimo
from models.emprestimoDAO import EmprestimoDAO
from suapapi import Suap

app = Flask(__name__)

app.secret_key = "secret"

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "mydb"

app.auth = {
    # 'ação': {perfil:permissão}
    'painel_professor': {0: 1, 1: 0},
    'painel_aluno': {0: 0, 1: 1},
    'logout': {0: 1, 1: 1},
    'login': {0: 1, 1: 1},
    #'cadastrar_livro': {0: 1, 1: 0}
}


app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


#@app.before_request
def autorizacao():
    acao = request.path[1:]
    acao = acao.split('/')

    if len(acao) >= 1:
        acao = acao[0]

    acoes = app.auth.keys()
    if acao in list(acoes):
        if session.get('logado') is None:
            return redirect(url_for('index'))
        else:
            tipo = session['logado']['tipo']
            if app.auth[acao][tipo] == 0:
                return redirect(url_for('painel'))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('login.html')


global token


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        api = Suap()
        matricula = request.form['matricula']
        senha = request.form['senha']
        token = api.autentica(matricula, senha)
        session['token'] = token
        user = api.getMeusDados(token)
        user[matricula] = matricula
        print(user)

        daoUsuario = UsuarioDAO(get_db())
        usuario = daoUsuario.verificar_matricula(request.form['matricula'])

        if usuario is not None:

            session['vinculo']['matricula'] = matricula
            session['token'] = token
            return render_template('painel')
        else:

            if user['tipo_vinculo'] == "Professor":
                vinculo = 0

            else:
                vinculo = 1

            nome = user['nome_usual']
            curso = user['vinculo']['curso']
            email = user['email']
            link_foto = "https://suap.ifrn.edu.br" + user['url_foto_150x200']
            senha = request.form['senha']

            usuario = Usuario(matricula, nome, curso, email, vinculo, link_foto, senha)

            dao = UsuarioDAO(get_db())
            codigo = dao.inserir(usuario)

            if vinculo == 0:
                return render_template('painel_professor')

            else:
                return render_template('painel.html')

    return render_template('login.html')


@app.route('/painel_aluno', methods=['GET', 'POST'])
def painel_aluno():
    daoLivro = LivroDAO(get_db())
    livro_db = daoLivro.listar_livro()
    return render_template("painel.html", livro=livro_db)


@app.route('/minha_conta', methods=['GET', 'POST'])
def minha_conta():
    token = session.get('token')
    api = Suap()
    user = api.getMeusDados(token)
    url_foto_150x200 = user['url_foto_150x200']
    tipo_vinculo = user['tipo_vinculo']
    nome = user['vinculo']['nome']
    matricula = user['matricula']
    return render_template("my-account.html", url_foto_150x200=url_foto_150x200, nome=nome,  matricula=matricula, tipo_vinculo=tipo_vinculo)


@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == "POST":
        nome = request.form['nome']
        autor = request.form['autor']
        area_id_area = request.form['area']
        quantidade_pag = request.form['quantidade_pag']
        link_capa = request.form['link_capa']

        livro = Livro(nome, autor, quantidade_pag, area_id_area, link_capa)

        dao = LivroDAO(get_db())
        codigo = dao.inserir(livro)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "sucess")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "cadastrar"
    return render_template("cadastrar_livro.html", titulo=vartitulo)


@app.route('/livros', methods=['GET', 'POST'])
def livros():

    dao = LivroDAO(get_db())

    if request.method == "POST":
        id_livro = request.form['id_livro']
        dao.excluir(id_livro)
        return redirect('/livros')

    livros_db = dao.listar_livro()
    return render_template("livros.html", livros=livros_db)


@app.route('/consulta/<area_id_area>', methods=['GET', 'POST'])
def consulta(area_id_area):
    if request.method == "GET":
        area_id_area = request.args.get(area_id_area)
        dao = LivroDAO(get_db)
        livros_db = dao.listar_livro_area(area_id_area)
        return render_template('livros.html', livros=livros_db)


@app.route('/logout')
def logout():
    session['logado'] = None
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

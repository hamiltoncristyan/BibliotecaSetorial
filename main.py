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
    'painel': {0: 1, 1: 1},
    'logout': {0: 1, 1: 1},
    'login': {0: 1, 1: 1},
    'cadastrar_livro': {0: 1, 1: 0}
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
            print(session.get('logado'))
            return redirect(url_for('index'))
        else:
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

        if token:
            user = api.getMeusDados(token)


            daoUsuario = UsuarioDAO(get_db())
            user_db = daoUsuario.verificar_matricula(request.form['matricula'])
            user_db = None
            if user_db is None:
                matricula = request.form['matricula']
                matricula = int(matricula)
                nome = user['vinculo']['nome']
                curso = user['vinculo']['curso']
                email = user['email']
                link_foto = "https://suap.ifrn.edu.br" + user['url_foto_150x200']
                senha = request.form['senha']

                vinculo = 0
                if user['tipo_vinculo'] == 'Aluno':
                    vinculo = 1

                user_db = Usuario(matricula, nome, curso, email, vinculo, link_foto, senha)
                codigo = daoUsuario.inserir(user_db)
                user_db = daoUsuario.verificar_matricula(matricula)
                flash("Usuário Cadastrado! Código %d" % codigo, 'sucess')

            session['logado'] = {
                'matricula': user_db[0],
                'nome': user_db[1],
                'curso': user_db[2],
                'email': user_db[3],
                'vinculo': user_db[4],
                'link_foto': user_db[5]
            }

            return redirect(url_for('painel'))


@app.route('/painel', methods=['GET', 'POST'])
def painel():

    if session['logado']['vinculo'] == 0:
        mostrar_div = True
    else:
        mostrar_div = False

    daoLivro = LivroDAO(get_db())
    livro_db = daoLivro.listar_livro()

    return render_template("painel.html", livro=livro_db, mostrar_div=mostrar_div)


@app.route('/minha_conta', methods=['GET', 'POST'])
def minha_conta():

    matricula = session['logado']['matricula']
    dao = UsuarioDAO(get_db())
    user = dao.verificar_matricula(matricula)

    if session['logado']['vinculo'] == 0:
        mostrar_div = True
    else:
        mostrar_div = False

    url_foto_150x200 = user[5]
    tipo_vinculo = user[4]
    nome = user[1]
    matricula = user[0]

    return render_template("my-account.html", url_foto_150x200=url_foto_150x200, nome=nome,  matricula=matricula, tipo_vinculo=tipo_vinculo, mostrar_div=mostrar_div)


@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == "POST":
        nome = request.form['nome']
        autor = request.form['autor']
        area_id_area = request.form['area']
        quantidade_pag = request.form['quantidade_pag']
        link_capa = request.form['link_capa']
        quant_exemp = int(request.form['quant_exemp'])

        for exemplar in range(quant_exemp):
            livro = Livro(nome, autor, quantidade_pag, area_id_area, link_capa)

            dao = LivroDAO(get_db())
            codigo = dao.inserir(livro)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, 'sucess')
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "cadastrar"
    return render_template("cadastrar_livro.html", titulo=vartitulo)


@app.route('/livros', methods=['GET', 'POST'])
def livros():
    dao = LivroDAO(get_db())
    livros_db = dao.listar_livro()

    if session['logado']['vinculo'] == 0:
        mostrar_div = True
    else:
        mostrar_div = False

    return render_template("livros.html", livros=livros_db, mostrar_div = mostrar_div)


@app.route('/pesquisar_livro', methods=['GET', 'POST'])
def pesquisar_livro():
    if request.method == "POST":
        print(request.form['livro'])
        livro = request.form['livro']
        print(livro)
        dao = LivroDAO(get_db)
        livros_db = dao.pesquisar_livro(livro)
        print(livros_db)
        return render_template('livros.html', livros=livros_db)


@app.route('/logout')
def logout():
    session['logado'] = None
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

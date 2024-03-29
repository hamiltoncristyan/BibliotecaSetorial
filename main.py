from flask import Flask, g, render_template, request, redirect, url_for, flash, session
import mysql.connector
from datetime import timedelta, date

from models.usuario import Usuario
from models.usuarioDAO import UsuarioDAO
from models.livro import Livro
from models.livroDAO import LivroDAO
from models.pdf import pdf
from models.pdfDAO import PdfDAO
from models.emprestimo import Emprestimo
from models.emprestimoDAO import EmprestimoDAO
from models.avaliacao import Avaliacao
from models.avaliacaoDAO import AvaliacaoDAO

from suapapi import Suap

app = Flask(__name__, static_url_path='/static')

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
    # 'cadastrar_livro': {0: 1, 1: 0}
}

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)


# @app.before_request
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

        daoUsuario = UsuarioDAO(get_db())
        usuario = daoUsuario.verificar_matricula(request.form['matricula'])

        if usuario is not None:

            request.form['matricula'] = matricula
            session['token'] = token
            print(token)
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
            matricula = int(request.form['matricula'])


            usuario = Usuario(matricula, nome, curso, email, vinculo, link_foto)

            dao = UsuarioDAO(get_db())
            codigo = dao.inserir(usuario)

            if vinculo == 0:
                return render_template('painel_professor')

            else:
                return render_template('painel.html')

    return render_template('login.html')


@app.route('/painel', methods=['GET', 'POST'])
def painel():
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

    dao_emprestimo = EmprestimoDAO(get_db())
    emprestimos_pendentes = dao_emprestimo.listar_emprestimo_pendente()
    emprestimos_aprovados = dao_emprestimo.listar_emprestimo_aprovado()
    meus_emprestimos = dao_emprestimo.meus_emprestimos(user['matricula'])

    print(emprestimos_aprovados)

    if request.method == "POST":

        id_emprestimo_aprovar = request.form.get('id_emprestimo_aprovar')
        id_emprestimo_devolver = request.form.get('id_emprestimo_devolver')
        id_emprestimo_adiar = request.form.get('id_emprestimo_adiar')

        if id_emprestimo_aprovar is not None and id_emprestimo_aprovar != '':
            emprestimo = dao_emprestimo.aprovar_emprestimo(int(id_emprestimo_aprovar))
        elif id_emprestimo_devolver is not None and id_emprestimo_devolver != '':
            emprestimo = dao_emprestimo.devolver_emprestimo(int(id_emprestimo_devolver))
        elif id_emprestimo_adiar is not None and id_emprestimo_adiar != '':
            emprestimo = dao_emprestimo.adiar_emprestimo(int(id_emprestimo_adiar))

        return redirect('/minha_conta')

    return render_template("my-account.html", url_foto_150x200=url_foto_150x200, nome=nome, matricula=matricula, tipo_vinculo=tipo_vinculo, emprestimos_pendentes=emprestimos_pendentes, emprestimos_aprovados=emprestimos_aprovados, meus_emprestimos=meus_emprestimos)


@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == "POST":
        nome = request.form['nome']
        autor = request.form['autor']
        area_id_area = request.form['area']
        quantidade_pag = request.form['quantidade_pag']
        link_capa = request.form['link_capa']
        descricao = request.form['descricao']

        livro = Livro(nome, autor, quantidade_pag, area_id_area, link_capa, descricao)

        dao = LivroDAO(get_db())
        codigo = dao.inserir(livro)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "sucess")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "cadastrar"
    return render_template("cadastrar_livro.html", titulo=vartitulo)


@app.route('/cadastrar_pdf', methods=['GET', 'POST'])
def cadastrar_pdf():
    if request.method == "POST":
        nome = request.form['nome']
        autor = request.form['autor']
        area_id_area = request.form['area']
        quantidade_pag = request.form['quantidade_pag']
        pdfcol = request.form['pdfcol']

        PDF = pdf(nome, autor, quantidade_pag, area_id_area, pdfcol)

        dao = PdfDAO(get_db())
        codigo = dao.inserir(PDF)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "sucess")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "cadastrar"
    return render_template("cadastrar_pdf.html", titulo=vartitulo)


@app.route('/livros', methods=['GET', 'POST'])
def livros():

    dao = LivroDAO(get_db())

    if request.method == 'POST':
        id_livro = request.form['id_livro']
        dao.excluir(id_livro)
        return redirect('/livros')

    livros_db = listar_todos_livros()
    return render_template("livros.html", livros=livros_db)


@app.route('/livro_detalhes/<int:livro_id>', methods=['GET'])
def livro_detalhes(livro_id):

    dao_avaliacao = AvaliacaoDAO(get_db())
    avaliacao = dao_avaliacao.listar_avaliacao_livro(livro_id)

    dao_livro = LivroDAO(get_db())
    livro = dao_livro.listar_livro_id(livro_id)

    token = session.get('token')
    api = Suap()
    user = api.getMeusDados(token)
    matricula = user['matricula']

    return render_template("livro_detalhes.html", livro=livro, avaliacao=avaliacao, matricula=matricula)


@app.route('/livros/<int:area_id_area>', methods=['GET'])
def consulta(area_id_area):
    livros_db = listar_livro_area(area_id_area)
    return render_template('livros.html', livros=livros_db)


def listar_livro_area(area_id_area):
    dao = LivroDAO(get_db())
    livros_db = dao.listar_livro_area(int(area_id_area))
    return livros_db


def listar_todos_livros():
    dao = LivroDAO(get_db())
    livros_db = dao.listar_livro()
    return livros_db


@app.route('/pdf', methods=['GET', 'POST'])
def pdf():
    dao = PdfDAO(get_db())

    if request.method == 'POST':
        id_pdf = request.form['id_pdf']
        dao.excluir(id_pdf)
        return redirect('/pdf')

    pdf_db = dao.listar_Pdf()
    return render_template("pdf.html", pdf=pdf_db)


@app.route('/solicitar_emprestimo', methods=['POST'])
def solicitar_emprestimo():
    if request.method == "POST":
        livro_id_livro = request.form['livro_id_livro']
        livro_area_id_area = request.form['livro_area_id_area']
        usuario_matricula = request.form['usuario_matricula']
        data_emprestimo = date.today()
        data_devolucao = data_emprestimo + timedelta(days=15)
        estado = "Pendente"

        dao = EmprestimoDAO(get_db())
        emprestimo = Emprestimo(livro_id_livro, livro_area_id_area, usuario_matricula, data_emprestimo, data_devolucao, estado)

        codigo = dao.inserir(emprestimo)

        if codigo is not None:
            print("Empréstimo Cadastrado")
        else:
            print("Empréstimo NÃO Cadastrado")

    return redirect(url_for('livros'))


@app.route('/cadastrar_avaliacao', methods=['POST'])
def cadastrar_avaliacao():

    if request.method == "POST":
        nome = request.form['nome']
        data = date.today()
        avaliacao = request.form['avaliacao']
        livro_id_livro = request.form['livro_id_livro']
        livro_area_id_area = request.form['livro_area_id_area']

        avaliacao = Avaliacao(nome, data, avaliacao, livro_id_livro, livro_area_id_area)

        dao = AvaliacaoDAO(get_db())
        codigo = dao.inserir(avaliacao)

    if codigo > 0:
        print("Avaliação Cadastrada")
    else:
        print("Avaliação NÃO Cadastrada")

    return redirect(url_for('livro_detalhes', livro_id=livro_id_livro))


@app.route('/Pdf', methods=['GET', 'POST'])
def Pdf():
    dao = PdfDAO(get_db())

    if request.method == 'POST':
        id_Pdf = request.form['id_Pdf']
        dao.excluir(id_Pdf)
        return redirect('/Pdf')

    Pdf_db = dao.listar_Pdf()
    return render_template("Pdf.html", livros=Pdf_db)


@app.route('/logout')
def logout():
    session['logado'] = None
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

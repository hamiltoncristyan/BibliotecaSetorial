from Flask import Flask, g, render_template, request, redirect, url_for, flash, session
import mysql.connector

from models.usuario import Usuario
from models.usuarioDAO import UsuarioDAO
from models.exemplar import Exemplar
from models.exemplarDAO import ExemplarDAO
from models.livro import Livro
from models.livroDAO import LivroDAO
from models.emprestimo import Emprestimo
from models.emprestimoDAO import EmprestimoDAO

app = Flask(__name__)

app.secret_key = "senha123"

DB_HOST = "bibliotecasetorial"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "mydb"

app.auth = {
    # 'ação': {perfil:permissão}
    'painel': {0: 1, 1: 1},
    'logout': {0: 1, 1: 1},
    'cadastrar_produto': {0: 1, 1: 1}
}

@app.before_request
def autorizacao():
    acao = request.path[1:]
    acao = acao.split('/')

    if len(acao) >= 1:
        acao = acao[0]

    acoes = app.auth.keys()
    if acao in list(acoes):
        if session.get('logado') is None:
            return redirect(url_for('login'))
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
    return render_template("login.html", titulo="Login")

@app.route('/logout')
def logout():
    session['logado'] = None
    session.clear()
    return redirect(url_for('index'))

@app.route('/home')
def painel():
    daoLivro = LivroDAO(get_db())
    livro_db = daoLivro.listar_livro()
    return render_template("index.html", livro=livro_db)
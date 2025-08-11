from flask import Flask, render_template, request, redirect, url_for, jsonify 
from flask_mysqldb import MySQL


app = Flask(__name__)

# Config do MySQL
app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = 'xxxx'  
app.config['MYSQL_DB'] = 'banco_ansiedade'

mysql = MySQL(app)

# Rota para a página principal (index)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de Call
@app.route('/call')
def call():
    return render_template('call.html')

# Rota para a página de Clientes
@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

# Rota para a página de Crises
@app.route('/crises')
def crises():
    return render_template('crises.html')

# Rota para a página de Histórico
@app.route('/historico')
def historico():
    return render_template('historico.html')

# Rota para a página de Login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota para a página de Médicos
@app.route('/medicos')
def medicos():
    return render_template('medicos.html')

# Rota para a página de Técnicas
@app.route('/tecnicas')
def tecnicas():
    return render_template('tecnicas.html')


# Rota para receber dados do formulário de médicos
@app.route('/medicos', methods=['POST'])
def cadastrar_medico():
    if request.method == 'POST':
        # Coletar os dados do formulário
        crm = request.form['crm']
        nome = request.form['nome']
        especialidade = request.form['especialidade']
        data_nascimento = request.form['data-nascimento']
        genero = request.form['genero']
        email = request.form['email']
        senha = request.form['senha']
        confirmacao_senha = request.form['confirmacao']

        # Validação simples de senha
        if senha != confirmacao_senha:
            return "As senhas não conferem, por favor, tente novamente."

        # Conectar ao banco de dados e inserir o registro
        try:
            cursor = mysql.connection.cursor()
            query = """
            INSERT INTO registro_de_especialistas (crm, nome, especialidade, data_nascimento, genero, email, senha, confirmacao_senha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (crm, nome, especialidade, data_nascimento, genero, email, senha, confirmacao_senha))
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('medicos'))  # Redireciona para a página de médicos
        except Exception as e:
            return f"Erro ao cadastrar médico: {e}"

    return "Método inválido."


# Página para listar médicos
@app.route('/medicos/')
def listar_medicos():
    try:
        # Conectar ao banco de dados e buscar os registros
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM registro_de_especialistas")
        medicos = cursor.fetchall()  # Retorna uma lista de tuplas com os registros
        cursor.close()
        
        # Renderizar a página com os médicos
        return render_template('medicos/index.html', medicos=medicos)
    except Exception as e:
        return f"Erro ao listar médicos: {e}"

# Rota para Editar médico
@app.route('/medicos/')
@app.route('/medicos/edit/<int:id>', methods=['GET', 'POST'])
def editar_medico(id):
    try:
        # Buscar os dados do médico pelo ID
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM registro_de_especialistas WHERE id = %s", (id,))
        medico = cursor.fetchone()  # Retorna uma tupla com os dados do médico
        cursor.close()

        # Verificar se o médico existe
        if not medico:
            return "Médico não encontrado."

        if request.method == 'POST':
            # Coletar os dados do formulário
            crm = request.form['crm']
            nome = request.form['nome']
            especialidade = request.form['especialidade']
            data_nascimento = request.form['data-nascimento']
            genero = request.form['genero']
            email = request.form['email']

            # Atualizar os dados no banco de dados
            cursor = mysql.connection.cursor()
            query = """
            UPDATE registro_de_especialistas 
            SET crm = %s, nome = %s, especialidade = %s, data_nascimento = %s, genero = %s, email = %s 
            WHERE id = %s
            """
            cursor.execute(query, (crm, nome, especialidade, data_nascimento, genero, email, id))
            mysql.connection.commit()
            cursor.close()

            return redirect(url_for('listar_medicos'))  # Redireciona para a lista de médicos

        return render_template('medicos/edit.html', medico=medico)

    except Exception as e:
        return f"Erro ao editar médico: {e}"

# Rota para Deletar médico
@app.route('/medicos/delete/<int:id>', methods=['GET'])
def deletar_medico(id):
    try:
        # Conectar ao banco de dados e deletar o médico pelo ID
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM registro_de_especialistas WHERE id = %s", (id,))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('listar_medicos'))  # Redireciona para a lista de médicos após a exclusão
    except Exception as e:
        return f"Erro ao deletar médico: {e}"



#Rotas para receber dados do formulário de clientes
@app.route('/clientes', methods=['POST'])
def cadastrar_cliente():
    # Coletar os dados do formulário
    nome = request.form['nome']
    cpf = request.form['cpf']
    data_nascimento = request.form['data-nascimento']
    genero = request.form['genero']
    email = request.form['email']
    senha = request.form['senha']
    confirmacao_senha = request.form['confirmacao']

    if senha != confirmacao_senha:
        return "As senhas não conferem, por favor, tente novamente."

    # Conectar ao banco de dados e inserir o registro
    try:
        cursor = mysql.connection.cursor()
        query = """
        INSERT INTO registro_de_pacientes (nome, cpf, data_nascimento, genero, email, senha, confirmacao_senha)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nome, cpf, data_nascimento, genero, email, senha, confirmacao_senha))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('clientes'))
    except Exception as e:
        return f"Erro ao cadastrar cliente: {e}"
    
#Rota para listar clientes/pacientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM registro_de_pacientes")
        clientes = cursor.fetchall()  # Lista de tuplas com os registros
        cursor.close()
        return render_template('clientes/listar.html', clientes=clientes)
    except Exception as e:
        return f"Erro ao listar clientes: {e}"


#rota para atualizar clientes  
@app.route('/atualizar_clientes', methods=['POST'])
def atualizar_clientes():
    # Coletar os dados enviados pelo JavaScript (email, cpf, novaSenha, confirmarSenha)
    email = request.form['email']
    cpf = request.form['cpf']
    nova_senha = request.form['novaSenha']
    confirmar_senha = request.form['confirmarSenha']
    
    # Verificar se as senhas coincidem
    if nova_senha != confirmar_senha:
        return "As senhas não coincidem. Tente novamente.", 400

    # Conectar ao banco de dados e verificar se o email e cpf existem
    try:
        cursor = mysql.connection.cursor()
        query = """
        SELECT * FROM registro_de_pacientes WHERE email = %s AND cpf = %s
        """
        cursor.execute(query, (email, cpf))
        usuario = cursor.fetchone()

        if usuario:
            # Atualizar a senha e a confirmação da senha
            update_query = """
            UPDATE registro_de_pacientes
            SET senha = %s, confirmacao_senha = %s
            WHERE email = %s AND cpf = %s
            """
            cursor.execute(update_query, (nova_senha, nova_senha, email, cpf))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Senha atualizada com sucesso!"}), 200
        else:
            cursor.close()
            return "Usuário não encontrado.", 404

    except Exception as e:
        return f"Erro ao atualizar senha: {e}", 500


#Rota para deletar clientes/pacientes
@app.route('/clientes/deletar/<int:id>', methods=['GET'])
def deletar_cliente(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM registro_de_pacientes WHERE id = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('listar_clientes'))
    except Exception as e:
        return f"Erro ao deletar cliente: {e}"


from flask import request, redirect, url_for, jsonify

# Rota para cadastrar crises
@app.route('/crises', methods=['POST'])
def cadastrar_crise():
    # Coletar os dados do formulário
    paciente_id = request.form['paciente_id']  # Agora o paciente_id é obtido diretamente do formulário
    data = request.form['data']
    sintomas = request.form['sintomas']
    gatilho = request.form['gatilho']
    falta_de_ar = request.form['falta_de_ar']
    nivel_sintomas = request.form['nivel_sintomas']

    # Conectar ao banco de dados e inserir o registro
    try:
        cursor = mysql.connection.cursor()
        query = """
        INSERT INTO registro_de_crises (paciente_id, data, sintomas, gatilho, falta_de_ar, nivel_sintomas)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (paciente_id, data, sintomas, gatilho, falta_de_ar, nivel_sintomas))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('tecnicas'))  # Redireciona para a página de tecnicas para ajudar nas crises
    
    except Exception as e:
        return f"Erro ao cadastrar crise: {e}"


#Rota para listar crises
@app.route('/crises', methods=['GET'])
def listar_crises():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM registro_de_crises")
        crises = cursor.fetchall()  # Retorna uma lista de tuplas com os registros
        cursor.close()
        return render_template('crises/listar.html', crises=crises)
    except Exception as e:
        return f"Erro ao listar crises: {e}"

#Rota para editar crises
@app.route('/crises/editar/<int:id>', methods=['GET', 'POST'])
def editar_crise(id):
    try:
        cursor = mysql.connection.cursor()
        # Buscar crise atual para exibir no formulário
        cursor.execute("SELECT * FROM registro_de_crises WHERE id = %s", (id,))
        crise = cursor.fetchone()

        if request.method == 'POST':
            data = request.form['data']
            sintomas = request.form['sintomas']
            gatilho = request.form['gatilho']
            falta_de_ar = request.form['falta_de_ar']
            nivel_sintomas = request.form['nivel_sintomas']

            # Atualizar o registro no banco de dados
            query = """
            UPDATE registro_de_crises 
            SET data = %s, sintomas = %s, gatilho = %s, falta_de_ar = %s, nivel_sintomas = %s
            WHERE id = %s
            """
            cursor.execute(query, (data, sintomas, gatilho, falta_de_ar, nivel_sintomas, id))
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('listar_crises'))

        cursor.close()
        return render_template('crises/editar.html', crise=crise)
    except Exception as e:
        return f"Erro ao editar crise: {e}"

#rota para deletar crises 
@app.route('/crises/deletar/<int:id>', methods=['GET'])
def deletar_crise(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM registro_de_crises WHERE id = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('listar_crises'))
    except Exception as e:
        return f"Erro ao deletar crise: {e}"


#rota para verificar paciente 
@app.route('/verificar_paciente', methods=['POST'])
def verificar_paciente():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return jsonify({'success': False, 'message': 'Email ou senha ausente.'})
    try:
        cur = mysql.connection.cursor()
        # Verificando se o usuário existe no banco de dados
        query = "SELECT id, senha FROM registro_de_pacientes WHERE email = %s"
        cur.execute(query, (email,))
        result = cur.fetchone()
        cur.close()
        if result:
            stored_password = result[1]
            if stored_password == senha:
                return jsonify({'success': True, 'paciente_id': result[0]})
            else:
                return jsonify({'success': False, 'message': 'Senha incorreta.'})
        else:
            return jsonify({'success': False, 'message': 'Usuário não encontrado! Você será redirecionado para a página de cadastro.'})

    except Exception as e:
        print(f"Erro ao verificar paciente: {e}")
        return jsonify({'success': False, 'message': 'Erro interno do servidor.'})

#novo
@app.route('/historico/<int:paciente_id>', methods=['GET'])
def exibir_historico(paciente_id):
    try:
        cur = mysql.connection.cursor()
        query = """
            SELECT data, sintomas, gatilho, falta_de_ar, nivel_sintomas
            FROM registro_de_crises
            WHERE paciente_id = %s
            ORDER BY data DESC
        """
        cur.execute(query, (paciente_id,))
        crises = cur.fetchall()
        cur.close()

        crises_list = [
            {
                "data": crise[0].strftime('%d/%m/%Y'),
                "sintomas": crise[1],
                "gatilho": crise[2] or 'Não informado',
                "falta_de_ar": 'Sim' if crise[3] else 'Não',
                "nivel_sintomas": crise[4]
            }
            for crise in crises
        ]
        return jsonify(crises=crises_list)

    except Exception as e:
        print(f"Erro ao buscar crises: {e}")
        return jsonify(error="Erro ao carregar o histórico de crises"), 500


if __name__ == '__main__':
    app.run(debug=True)

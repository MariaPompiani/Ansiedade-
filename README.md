# Plataforma de Apoio à Saúde Mental – Gestão de Ansiedade

## Descrição

Projeto de plataforma web desenvolvida para apoiar pessoas com ansiedade, oferecendo ferramentas de autodiagnóstico, técnicas, suporte de profissionais de saúde (médicos), registro de crises e histórico do usuário. 

A plataforma também possui integração com banco de dados MySQL para gerenciamento de usuários (pacientes e médicos), registro e acompanhamento de crises, além de recomendações personalizadas baseadas no estado emocional.

Esse projeto foi desenvolvido em Flask (back-end Python) com front-end em HTML, CSS e JavaScript.

---

## Funcionalidades Principais

- Cadastro, edição, listagem e exclusão de Médicos e Pacientes
- Registro e gerenciamento de Crises de ansiedade
- Histórico de crises para cada paciente
- Verificação de login de paciente via API REST (JSON)
- Recomendações personalizadas de técnicas, canais e livros baseados na emoção do usuário
- Validação de formulários em tempo real no front-end
- Interface responsiva com feedback visual e animações leves
- Atualização automática do ano no rodapé
- Fila simulada para pacientes aguardando atendimento (exemplo funcional)

---

## Tecnologias Utilizadas

- Python 3.x
- Flask (framework web)
- Flask-MySQLdb (integração com banco de dados MySQL)
- MySQL (banco de dados relacional)
- HTML5, CSS3, JavaScript (front-end)
- Bootstrap (opcional, para estilo)
- AJAX (com fetch API para atualização dinâmica)

---

### Pré-requisitos

- Python 3 instalado
- MySQL instalado e em execução
- Git instalado (opcional, para controle de versão)
- Navegador web moderno

### Passos para rodar localmente

1. Clone o repositório:

```
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
```

2. Configure o banco de dados no MySQL:
-Crie o banco banco_ansiedade no MySQL
No MyQL:

```
CREATE TABLE registro_de_especialistas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    crm VARCHAR(50),
    nome VARCHAR(100),
    especialidade VARCHAR(100),
    data_nascimento DATE,
    genero VARCHAR(10),
    email VARCHAR(100),
    senha VARCHAR(255),
    confirmacao_senha VARCHAR(255)
);

CREATE TABLE registro_de_pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(11),
    data_nascimento DATE,
    genero VARCHAR(10),
    email VARCHAR(100),
    senha VARCHAR(255),
    confirmacao_senha VARCHAR(255)
);

CREATE TABLE registro_de_crises (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    data DATE,
    sintomas TEXT,
    gatilho TEXT,
    falta_de_ar BOOLEAN,
    nivel_sintomas VARCHAR(20),
    FOREIGN KEY (paciente_id) REFERENCES registro_de_pacientes(id)
);


3. Ajuste as configurações do banco de dados em app.py
'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sua_senha_aqui'
app.config['MYSQL_DB'] = 'banco_ansiedade'
```

4. Execute a aplicação Flask:

```
python app.py
```

5. Acesse no navegador
```
http://localhost:5000
```

Projeto desenvolvido como parte das disciplinas Banco de Dados Relacional e Programação Web - Pontifícia Universidade Católica de Campinas

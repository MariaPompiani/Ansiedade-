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

## Estrutura do Projeto


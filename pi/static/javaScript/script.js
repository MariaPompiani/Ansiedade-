//1
//Validação de Formulário em Tempo Real
document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form'); // Seleciona o formulário
  form.addEventListener('submit', function (event) {
    // Previne o envio do formulário até que as validações sejam feitas
    //event.preventDefault();

    // Obtém os valores dos campos do formulário
    const senha = document.getElementById('senha').value;
    const confirmacao = document.getElementById('confirmacao').value;
    const email = document.getElementById('email').value;
    const cpf = document.getElementById('cpf').value;

    // Valida a senha
    if (senha !== confirmacao) {
      alert('As senhas não coincidem!');
      return;
    }

    // Valida o email
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(email)) {
      alert('Por favor, insira um email válido!');
      return;
    }

    // Valida o CPF (simples validação de formato com 11 dígitos numéricos)
    const cpfRegex = /^\d{11}$/;
    if (!cpfRegex.test(cpf)) {
      alert('Por favor, insira um CPF válido!');
      return;
    }

    // Se todas as validações passarem, envia o formulário
    form.submit();
  });
});



//2
// Alterar cor do cabeçalho ao rolar a página
window.addEventListener('scroll', () => {
  const header = document.querySelector('.header');
  if (window.scrollY > 50) {
      header.style.backgroundColor = '#f1f1f1'; // Cor clara
      header.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
  } else {
      header.style.backgroundColor = 'transparent'; // Transparente
      header.style.boxShadow = 'none';
  }
});



//3
// Validação visual de formulário
const form = document.querySelector('.form');
if (form) {
  form.addEventListener('submit', (event) => {
      const senha = document.querySelector('#senha').value;
      const confirmacao = document.querySelector('#confirmacao').value;

      if (senha !== confirmacao) {
          event.preventDefault();
          alert('As senhas não coincidem. Por favor, verifique.');
          document.querySelector('#confirmacao').style.border = '2px solid red';
      } else {
          alert('Cadastro realizado com sucesso!');
      }
  });
}


//4
// Fila inicial com 4 pessoas
let fila = ['Pessoa 1', 'Pessoa 2', 'Pessoa 3', 'Pessoa 4'];

// Função que simula o paciente entrando na fila
function entrarNaFila() {
  // Adiciona o paciente na posição 5 da fila
  fila.push('Paciente');
  
  // Atualiza o status da fila na interface 
  atualizarStatusFila();
}

// Função para atualizar o status da fila
function atualizarStatusFila() {
  // Encontra a posição do paciente na fila (a última posição)
  const posicaoPaciente = fila.indexOf('Paciente') + 1;
  
  // Exibe a posição na tela
  document.getElementById('status-fila').textContent = `Sua posição na fila é: ${posicaoPaciente}, aguarde alguns minutos...`;
}



//5
//atualizacao de ano 
document.querySelector('.year').textContent = new Date().getFullYear();


//6
// Seleciona todos os botões dentro do elemento com a classe 'nav'
const navButtons = document.querySelectorAll('.nav-button');

// Itera sobre cada botão e adiciona eventos de mouse
navButtons.forEach(button => {
  // Evento ao passar o mouse
  button.addEventListener('mouseover', () => {
    button.style.backgroundColor = '#418e3e'; // Altere para a cor desejada
    button.style.color = '#FFFFFF';          // Cor do texto ao passar o mouse
  });

  // Evento ao remover o mouse
  button.addEventListener('mouseout', () => {
    button.style.backgroundColor = '';       // Retorna à cor original definida no CSS
    button.style.color = '';                 // Retorna à cor do texto original
  });
});


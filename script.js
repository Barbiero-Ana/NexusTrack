// script.js

// Selecionando o ícone do hambúrguer e o menu
const hamburger = document.getElementById('hamburger');
const menu = document.getElementById('menu');

// Adicionando evento de clique no hambúrguer para alternar a classe "active" no menu
hamburger.addEventListener('click', () => {
  menu.classList.toggle('active');
});

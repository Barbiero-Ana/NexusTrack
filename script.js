// Script para abrir e fechar o menu hamburguer
document.getElementById('hamburger').addEventListener('click', function() {
  const menu = document.querySelector('.menu');
  menu.classList.toggle('active');
});

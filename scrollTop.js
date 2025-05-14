// Obtém o botão de voltar ao topo
const btnTopo = document.getElementById("btnTopo");

// Mostra o botão quando o usuário rolar para baixo 100px
window.onscroll = function() {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    btnTopo.style.display = "block"; // Exibe o botão
  } else {
    btnTopo.style.display = "none"; // Esconde o botão
  }
};

// Função de rolar para o topo
function voltarAoTopo() {
  document.body.scrollTop = 0; // Para Safari
  document.documentElement.scrollTop = 0; // Para Chrome, Firefox, IE e Opera
}

// Função para animar o carrossel somente no modo responsivo
const teamGrid = document.querySelector('.team-grid');
const memberWidth = document.querySelector('.member').offsetWidth + 20; // Calcula a largura de cada card (incluindo o espaçamento)

let offset = 0;

function moveCarousel() {
  offset += memberWidth; // Incrementa o deslocamento
  if (offset >= teamGrid.scrollWidth - teamGrid.offsetWidth) {
    offset = 0; // Volta ao início quando chegar ao final
  }

  teamGrid.style.transform = `translateX(-${offset}px)`; // Move os cards para a esquerda
}

// Intervalo de tempo para animar o carrossel
setInterval(moveCarousel, 3000); // Muda os cards a cada 3 segundos



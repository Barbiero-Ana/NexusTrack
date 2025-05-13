import streamlit as st

# Imagem e título da sidebar
st.sidebar.image("/Users/anabarbiero/Documents/GitHub/portfolio-integrador/src/NT-logo.png",  width=300)

st.sidebar.title("Menu")

# Botões na sidebar
st.sidebar.markdown(
    """
    <a href="https://drive.google.com/drive/folders/1BYZRMK0gzw-DgrehBG2By-pd379DNQyk?usp=sharing" target="_blank">
        <button style="background-color:#8B5DFF;color:white;padding:10px 24px;border:none;border-radius:5px;cursor:pointer;margin-bottom:15px;">
            Acessar documentações do projeto
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# Botão 2
st.sidebar.markdown(
    """
    <a href="https://drive.google.com/drive/folders/1BYZRMK0gzw-DgrehBG2By-pd379DNQyk?usp=sharing" target="_blank">
        <button style="background-color:#8B5DFF;color:white;padding:10px 30px;border:none;border-radius:5px;cursor:pointer;margin-bottom:15px;">
            Acessar protótipo do projeto
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# Botão 3
st.sidebar.markdown(
    """
    <a href="https://drive.google.com/drive/folders/1BYZRMK0gzw-DgrehBG2By-pd379DNQyk?usp=sharing" target="_blank">
        <button style="background-color:#8B5DFF;color:white;padding:10px 30px;border:none;border-radius:5px;cursor:pointer;margin-bottom:15px;">
            Ver integrantes da equipe
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# Botão 4
st.sidebar.markdown(
    """
    <a href="https://forms.gle/XcWUS497KDSyejHp8" target="_blank">
        <button style="background-color:#8B5DFF;color:white;padding:10px 30px;border:none;border-radius:5px;cursor:pointer;margin-bottom:15px;">
            Avalie nosso projeto
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# Título principal
st.title('Portólio do projeto NexusTrack')

# Subtítulo
st.subheader('Conheça mais do nosso projeto e da nossa equipe.')

# Adicionando a quebra de linha após o subtítulo
st.markdown("""
    <style>
        .header-spacing {
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Aplicando a quebra de linha após o subtítulo
st.markdown('<div class="header-spacing"></div>', unsafe_allow_html=True)

# Animação de texto
st.markdown("""
    <style>
        @keyframes slidein {
            0% {
                transform: translateX(-100%);
            }
            100% {
                transform: translateX(0);
            }
        }
        .animated-text {
            font-size: 30px;
            color: white;
            animation: slidein 2s ease-out forwards;
        }
        .nexustrack {
            color: #8B5DFF;
        }
    </style>

    <div class="animated-text">
        Bem-vindo ao <span class="nexustrack">NexusTrack</span>! 🚚  
        Nosso projeto visa otimizar a logística de transporte e entrega, informando a qualquer momento a localização dos produtos e quando estarão prontos para retirada.
        Acompanhe em tempo real e garanta um processo mais eficiente e ágil para sua empresa.
    </div>
""", unsafe_allow_html=True)

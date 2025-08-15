# GeoGebra MiniLab

Este projeto é uma aplicação web para visualização de funções matemáticas, uma simplificação para o GeoGebra.  
A interface permite que o usuário insira funções e gere gráficos, utilizando um servidor Flask para processar e renderizar as imagens com Matplotlib.

## Estrutura

- **index.html** - Página principal da aplicação, interface gráfica do usuário.  
- **styles.css** - Arquivo de estilo da página.  
- **script.js** - Script em JavaScript responsável por capturar entradas do usuário e enviar para o backend, além de executar modificações na página html.  
- **app.py** - Servidor Flask que recebe as funções e retorna a imagem do gráfico em Base64.  
- **plotting.py** - Funções auxiliares para gerar o gráfico a partir das funções recebidas.  
- **Makefile** - Arquivo de automação para instalar dependências, executar o servidor e rodar um caso de estudo criado.  
---

## Dependências

O projeto utiliza as seguintes bibliotecas Python:

- **Flask** - Microframework web para o backend.  
- **Flask-CORS** - Permite as requisições.  
- **matplotlib** - Faz a geração dos gráficos.  
- **numpy** - Utilizada para manipulação de dados numéricos.  

---

## Instalação

1. Clone o repositório
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Instale as dependências com Makefile
    make install
Isso cria um ambiente virtual (venv) e instala todas as bibliotecas necessárias.

## Execução

Há duas maneiras possíveis para executar:

1:
Rodar apenas o servidor Flask com o seguinte comando:
    make run
O servidor ficará disponível em: http://127.0.0.1:5000
A seguir, para usar a interface, abra o arquivo index.html no navegador.

2:
Executar o caso de estudo com o comando:
    make study


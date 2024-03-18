<h1 align="center">PriceSeeking</h1>

## :page_with_curl: Sobre
Eu aproveitei que estou a ver Python na faculdade e resolvi fazer esse projeto utilizando-a.

Foi um desafio em conjunto que eu e meu pai tivemos, criar uma aplicação que acompanhasse o preço de qualquer crypto que jogássemos no App.
Ele fez em Delphi e eu fiz em Python.

- Python - Linguagem utilizada para desenvolvimento.
- Tkinter - Usado para criar uma interface para o código.
- Proxlight Designer - Programa que transforma um Design do Figma em código Python Tkinter.

Qual é a lógica da aplicação?

Eu construí fazendo uma GET na página das moedas do [CoinMarketCap](https://coinmarketcap.com/pt-br/), desmembro o HTML até chegar nos dados que eu preciso, exibindo-os de uma forma organizada. Quando o preço desejado para compra é atingido, a aplicação dá play em um áudio com som de Sabre de Luz pra chamar a atenção do usuário.

Por que eu não usei a API deles? Porque no modelo gratuito, tem um limite de requisicões, mesmo sendo bastante, preferi não usar.


Alguns impecílios que não usar API causou:

 - [ ] Mais trabalho no GET dos dados;
 - [ ] Cache do valor. Aparentemente, o site utiliza WebHook, o que faz com que ele fique em constante atualização, mas isso só acontece já com o site aberto. Então quando eu dou o GET na página, vem com o valor "cacheado".

Resolvi?

 - [x] Em relação ao cache, ele ainda atrapalha. Porém, uma breve análise me mostrou que ele atualiza em +ou- 1min, então eu realizo o GET da página de 10 em 10s, mostro quando foi feito o último e troco as inforamções da moeda apenas se for diferente do último preço obtido.

# Algumas imagens da interface da aplicação:

<h1 align="center">
  <img alt="Home" src="https://media.discordapp.net/attachments/904712495292358677/904712542528618526/unknown.png?ex=660aac36&is=65f83736&hm=3255f9e2a4ba329e3c869e4c22c94b4ec49724219843a92bdbf63e5838e93e91&=&format=webp&quality=lossless&width=765&height=468" width="800px" />
</h1>
<h1 align="center">
  <img alt="Working" src="https://media.discordapp.net/attachments/904712495292358677/904713052052664350/unknown.png?ex=660aacb0&is=65f837b0&hm=b854e448584d06ece8442e290cea4c84e5474e6e5817a2ff7374489a79d2ce22&=&format=webp&quality=lossless&width=775&height=468" width="800px" />
</h1>

## :hammer: Tecnologias

Este projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Proxlight Designer](https://proxlightapps.gumroad.com/l/Proxlight-Designer)
- [Pycharm](https://www.jetbrains.com/pt-br/pycharm/)

## :books: Requisitos
- Ter [**Git**](https://git-scm.com/) para clonar o projeto.
- Ter [**Python**](https://www.python.org) instalado.

## :gear: Iniciando a interface
```bash

  # Iniciar a aplicação:
  $ cd Interface
  $ python window.py
```

A aplicação tambpem funciona diretamente no terminal, mas sendo acessado por outro arquivo.

## :gear: Iniciando diretamente no terminal
```bash

  # Iniciar a aplicação:
  $ python main.py
```

Feito por João Vitor Freitas 👋🏻 [Toca aqui, maninho!](https://github.com/Jwmffreitas)

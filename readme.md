# Desafio Magalu
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=%20COMPLETO&color=GREEN&style=for-the-badge)

## Indice

*[Preparando Ambiente](#preparando-ambiente)
*[Rodando projeto](#rodando-projeto)
**[MLflow server](#mlflow-server)
**[Kedro](#kedro)
**[FastAPI](#fastapi)
*[Notas do Projeto](#notas-do-projeto)

### Preparando Ambiente

O ambiente de desenvolvimento utiliado nesse projeto foi uma env do anaconda, no qual o no arquivo requiriments.txt consta as dependencias utilizadas na env.

Fora isso é necessario tambem o Docker para rodar o projeto.

### Rodando Projeto

O projeto pode ser dividio em tres modulos principais, sendo cada um deles separado do outros de maneira a emular um ambiente de produção onde Kedro estaria rodando da sua maquina pessoal, MLflow Server e FastApi dentro de alguma aplicação online. Para que as interações entre os modulos ocorram corretamente é importante executar o projeto conforme a ordem apresentada abaixo.


#### MLflow Server

Neste projeto o MLflow foi desenvolvido dentro de um docker para simular como se ele estivesse dentro de um ambiente externo ao localhost do projeto, o projeto desse servidor de mlflow pode ser encontrado em [https://github.com/raphaelauv/mlflow_docker-compose](#https://github.com/raphaelauv/mlflow_docker-compose). Para executar basta entrar na pasta mlflow_docker-compose-master e rodar o comando:

docker-compose up

Depois disso a UI do mlflow estará disponivel em:

http://localhost:5000/



#### Kedro

Kedro é uma estrutura Python de código aberto para criar código de ciência de dados reprodutível, sustentável e modular. [Link da documentação](https://kedro.readthedocs.io/en/stable/index.html)

Primeiramente utilizar o kedro neste projeto basta verificar se as dependencias contidas em ml_pipeline/src/requiriment.txt estão instaladas corretamente. Em seguida estando dentro da pasta ml_pipeline basta rodar o comando kedro run que todo processamento de treinamento e log do modelo sera feito de maneira automatica e enviado para MLFlow server.

Caso deseja ter uma visualização interativa dos Nodes, pipelines e databases contidos dentro do projeto kedro, basta instalar o kedro-viz com:

pip install kedro-viz

Em seguida ativar ele com o comando: 

kedro viz

Kedro tambem gera uma documentação automatica das funções, isso pode ser lido executando o comando:

kedro docs


#### FastApi

Por fim com os dois modulo executados para utilizar FastApi é necessario um passo antes de rodar seu dockerfile, dentro do arquivo app/main.py é necessairo substitui http://<SEU_IP>:5000 por seu IP na região indicada. Isto é necessario para que dessa forma o Docker da FastApi possa se comunicar corretamente com o Docker do MlFlow. Com isso feito basta buildar a imagem com :

docker build -t fast_api .

E em seguida criar o container com:

docker run  --name fast_api -p 80:80 fast_api

Por fim para executar os testes da api basta estar dentro da pasta fast_api e rodar o comando:

pytest

#### Notas do Projeto

Para que FastApi funcione corretamente é importante garantir que tenha um modelo registrado e colocado em Staging dentro do MLFlow, para verificar isso basta entrar na UI do MLflow server. Caso não tenha nenhum modelo basta registrar algum dentro dos experimentos realizados.
# Aplicação de Votação

Uma aplicação distribuída simples executando através de múltiplos containers Docker.

Essa aplicação é um fork de: https://github.com/dockersamples/example-voting-app

## Começando

Faça o download do [Docker Desktop](https://www.docker.com/products/docker-desktop) para Mac ou Windows. O [Docker Compose](https://docs.docker.com/compose) será instalado automaticamente. No Linux, certifique-se de ter a versão mais recente do [Compose](https://docs.docker.com/compose/install/).

Esta solução utiliza Python, Node.js, .NET, com Redis para mensageria e Postgres para armazenamento.

Execute os comandos neste diretório para construir e rodar a aplicação:

```shell
docker compose up
```

A aplicação `vote` estará rodando em [http://localhost:8080](http://localhost:8080), e os `results` estarão em [http://localhost:8081](http://localhost:8081).

Alternativamente, se você quiser executar em um [Docker Swarm](https://docs.docker.com/engine/swarm/), primeiro certifique-se de ter um swarm. Se não tiver, execute:

```shell
docker swarm init
```

Depois que você tiver seu swarm, neste diretório execute:

```shell
docker stack deploy --compose-file docker-stack.yml vote
```

## Arquitetura

![Diagrama de arquitetura](architecture.excalidraw.png)

- Uma aplicação web front-end em [Python](/vote) que permite votar entre duas opções
- Um [Redis](https://hub.docker.com/_/redis/) que coleta novos votos
- Um worker [.NET](/worker/) que consome votos e os armazena no banco de dados.
- Um banco de dados [Postgres](https://hub.docker.com/_/postgres/) com backup em um volume Docker
- Uma aplicação web [Node.js](/result) que mostra os resultados da votação em tempo real

## Notas

A aplicação de votação aceita apenas um voto por navegador cliente. Ela não registra votos adicionais se um voto já foi enviado de um cliente.

# API de Processamento CPU

Esta é uma API de exemplo desenvolvida para o curso de Docker que demonstra diferentes níveis de processamento CPU através do cálculo da sequência de Fibonacci.

## Sobre o Projeto

A API possui dois endpoints que realizam cálculos da sequência de Fibonacci com diferentes cargas de processamento:

- Endpoint leve (`/light`): Calcula Fibonacci(20)
- Endpoint pesado (`/heavy`): Calcula Fibonacci(35)

## Tecnologias Utilizadas

- Python 3.11
- FastAPI
- Poetry (gerenciamento de dependências)
- Docker
- Docker Compose

## Requisitos

Para executar localmente com Poetry:

- Python 3.11+
- Poetry

Para executar com Docker:

- Docker
- Docker Compose

## Como Executar

### Usando Poetry

1. Instale o Poetry (caso não tenha):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Instale as dependências:

```bash
poetry install
```

3. Execute a aplicação:

```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
```

### Usando Docker

1. Construa e execute o container usando Docker Compose:

```bash
docker compose up --build
```

Para executar em segundo plano:

```bash
docker compose up -d
```

## Acessando a API

Após iniciar a aplicação, você pode acessar:

- API: http://localhost:8000
- Documentação (Swagger UI): http://localhost:8000/docs
- Documentação alternativa (ReDoc): http://localhost:8000/redoc

## Endpoints

### POST /light

Realiza processamento leve (Fibonacci 20)

**Exemplo de uso com curl:**

```bash
curl -X POST http://localhost:8000/light
```

Exemplo de resposta:

```json
{
  "result": 6765,
  "processing_time": 0.0021,
  "endpoint": "light"
}
```

### POST /heavy

Realiza processamento pesado (Fibonacci 35)

**Exemplo de uso com curl:**

```bash
curl -X POST http://localhost:8000/heavy
```

Exemplo de resposta:

```json
{
  "result": 9227465,
  "processing_time": 4.5678,
  "endpoint": "heavy"
}
```

## Monitoramento

A aplicação inclui healthcheck configurado para verificar a disponibilidade do serviço a cada 30 segundos.

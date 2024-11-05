# Docker Swarm - Principais comandos

## Gerenciamento de Nodes

- Inicializar um swarm: `docker swarm init`
- Listar nodes do swarm: `docker node ls`
- Obter o comando para novos nodes se juntarem ao swarm: `docker swarm join-token worker` ou `docker swarm join-token worker`. O comando exibe o comando necessário e o token: Por exemplo, para adicionar um worker a este swarm, execute o seguinte comando:

```
docker swarm join \
--token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
192.168.99.100:2377
```

- Verificar acessibilidade do service manager: `docker node inspect manager-node-name --format "{{ .ManagerStatus.Reachability }}"`
- Verificar estado do node: `docker node inspect node-name --format "{{ .Status.State }}"`
- Colocar um node em modo de manutenção: `docker node update --availability drain node_name`
- Ativar um node (após manutenção): `docker node update --availability active node_name`
- Adicionar uma label: `docker node update --label-add key=value node_name`
- Remover uma label: `docker node update --label-rm key node_name`
- Pesquisar label: `docker node inspect node_name | grep Labels -C5`

## Gerenciamento de Services

- Listar services (node manager): `docker service ls`
- Descrever services (node manager): `docker service ps service_name`
- Inspecionar um service: `docker service inspect service_name`
- Escalar um service: `docker service scale service_name=N`
- Remover service: `docker service rm service_name`
- Publicar o serviço em uma porta: `docker service create --name vote -p 8080:80 voting-app`

## Gerenciamento de Stacks

- Implantar stack a partir do arquivo docker-compose: `docker stack deploy -c docker-compose.yml stack_name`
- Listar stacks: `docker stack ls`
- Listar services da stack: `docker stack services stack_name`
- Listar tarefas da stack: `docker stack ps stack_name`
- Remover stack: `docker stack rm stack_name`

## Gerenciamento de Networks

- Listar networks: `docker network ls`
- Criar network overlay: `docker network create -d overlay network_name`
- Remover network: `docker network rm network_name`

## Monitoramento de Services

- Estatísticas Docker: `docker stats`
- Logs do service: `docker service logs service_name`

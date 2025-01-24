# Logistics Indicators API

## 🗒️ Descrição
O projeto trata-se de uma API que permite o cadastro de clientes e atendimentos a partir da carga com arquivo .csv ou cadastro individual para compor uma base de dados logistica, e a partir das informações a geração de relatórios de indicadores de produtividade e SLA dos atendimentos dos técnicos logísticos (Green Angels).

## 🎯 Objetivos
- Cadastro, consulta, filtro, atualização e deleção de clientes (customers)
- Cadastro, consulta, filtro e atualização de atendimentos (customer_services)
- Carga de clientes e atendimentos a partir de arquivo .csv
- Consulta de indicadores de operação:
  - Produtividade por Green Angel
  - SLA de cada base logística
  - SLA de cada Green Angel

## ⚡ Principais Features

- Autenticação JWT com rotas de registro, login e refresh token
- [Script de geração de dados fictícios de clientes](https://github.com/jocsakesley/logistics_indicators_api/blob/main/utils/create_customers.py) a partir dos valores únicos da coluna `id_cliente` do arquivo de atendimentos
- Carga do arquivo de clientes e atendimentos a partir de uma rota http que faz o processamento assíncrono, com transformação dos dados de `data_de_atendimento` que estavam despadronizadaos, utilizando uma thread para recepção do arquivo e envio das linhas para uma fila, evitando bloqueio da requisição, e 100 threads para a leitura da fila e gravação no banco de dados em chunks de 2000 registros por vez. As threads, chunks e sleep times são configuráveis por variáveis de ambiente garantindo o melhor tradeoff para produção (O tempo de processamento atual no endereço público está maior que ao rodar localmente, devido a limitação de configuração para evitar custos)
- Consulta do total de registros para clientes e atendimentos nas rotas `/v1/customers/total` e `/v1/services/total`, facilitando o monitoramento da conclusão da carga batch.
- Consulta da rota `/v1/customers` com filtros para todos os campos (`email`, `nome` e `telefone`) e paginação a partir dos parameters `limit` e `offset`
- Consulta da rota `/v1/services` com filtros para todos os campos (`angel`, `id_cliente`, `data_de_atendimento`, `data_limite` e `polo`) e paginação a partir dos parameters `limit` e `offset`
- Consuta da rota `/v1/indicators/productivity`, `/v1/indicators/sla/angel` e `/v1/indicators/sla/polo` com filtros de data (`start_date=YYYY-MM-DD` e `end_date=YYYY-MM-DD`) e ordenação (`sort_field=<total, total_sla, avg_time>`  e `desc=<true, false>`)
- Monitoramento das requisições através de logs com status e tempo de resposta, implementado a partir de um midlleware que calcula os tempos a cada requisição
![image](https://github.com/user-attachments/assets/769979f7-85a0-4cb2-a918-fa6b7542945b)
- Monitoramento do tempo de carga do arquivo batch através dos logs com uma média de 48 segundos para o arquivo de clientes com 573670 linhas e 80 segundos para o arquivo de atendimentos com 1048575 linhas
![image](https://github.com/user-attachments/assets/4e00b4d9-4a1f-4b4b-abb5-7ad0e0cf1751)
![image](https://github.com/user-attachments/assets/dc685b2a-2494-4c89-9aa4-c3bfd6b8dea9)
- Monitoramento através de requests às rotas `/v1/metrics` com métricas de CPU, memória e disco e `/v1/health` para monitoramento da saúde do servidor
- Testes unitários para os usecases que contém o core das regras de negócios
- Testes end-to-end foram feitos a partir de uma collection do postman, porém podem ser adicionados ao projeto
- Padronização de commits para cada tipo de alteração (feat, refactor, test, build, doc) 
- Execução do projeto a partir do docker compose
- Build e push da imagem para o docker hub através da pipeline do github actions
- Deploy da aplicação na AWS ECS a partir da pipeline do CloudFormation (optei por esse cloud provider por mais familiariade)
- Aplicação desenvolvida seguindo princípios da orientação a objetos utilizando uma metodologia baseada na Clean Archtecture onde foram separadas as camadas de infra, controllers e usecases seguindo o seguinte fluxo:
  ![image](https://github.com/user-attachments/assets/b01a460a-7b7a-4bd3-84f9-9bdfbf5807e0)

  
## 🔧 Pré requisitos técnicos
- Containers Docker para a execução da API e do banco de dados.
- Python 3 com Flask para criação da API
- Banco de dados Postgresql
- Projeto entregue pelo github
- README com instruções para instalação e execução do projeto

## 🚀 Instalação e Setup
Para a execução local do projeto é necessário que o [docker](https://docs.docker.com/engine/install/) e o [docker compose](https://docs.docker.com/compose/install/) estejam instalados e seguidos os seguintes passos:

1. Clone o repositório
```bash
git clone https://github.com/jocsakesley/logistics_indicators_api.git
cd logistics_indicators_api
```

2. Configure as variáveis de ambiente (opcional)

Arquivo .env disponibilizado no repositório apenas para desenvolvimento.
Para produção é recomendado que as variáveis sensíveis sejam setadas de forma segura através de um gerenciador de segredos.

Variáveis do arquivo .env:
 ```
 #Database
 POSTGRES_PASSWORD=postgres
 POSTGRES_USER=jocsa
 POSTGRES_DB=logistics
 POSTGRES_HOST=db
 
 #Autenticação
 JWT_SECRET_KEY=my-secret
 
 #File handler
 NUMBER_WORKER_FILE_THREADS=100
 SECONDS_WAIT_QUEUE_EMPTY=10
 SIZE_FILE_CHUNKS=2000
```
3. Inicialize o docker (pelo docker desktop ou pelo teminal)
   
4. Rode o docker-compose
```bash
docker-compose up --build -d
```
Obs.: Usar o comando sem o -d para acompanhar os logs no terminal

5. Verifique que os containers da aplicação, db estão rodando
```bash
docker ps
```
6. Acesse a API pela url `localhost:8000` mais a rota de preferência segundo a documentação

## 📓 Documentação da API

A documentação pode ser baixada a partir [desse link](https://github.com/jocsakesley/logistics_indicators_api/blob/main/docs/logistics-api.postman_collection.json)  e importada para um client http como o postman ou baixar a [especificação openapi nesse link](https://github.com/jocsakesley/logistics_indicators_api/blob/main/docs/openapi.yaml) e importar no editor online [swagger editor](https://editor.swagger.io/) para uma melhor visualização.

Obs.: Para as consultas, é possível remover os filtros para trazer todos os resultados, com paginação para clientes e atendimentos.

## 💻 Como usar

- Registre um usuário na rota `/v1/auth/register` com `username`, `email` e `password`
- Faça login na rota `/v1/auth/login` e copie o `access_token` retornado
- Em todas as chamadas passe no header o key `Authorization` e no value `Bearer <access_token>`
- Faça o upload do arquivo `customers_data.csv` na rota `/v1/customers/batch` 
- Monitore o total de linhas inseridas na rota `/v1/customers/total` (o total deve ser 573670)
- Faça o upload do arquivo `utils/bd_desafio.csv` na rota `/v1/services/batch`
- Monitore o total de linhas inseridas na rota `/v1/services/total` (o total deve ser 1048575) 
- Faça as devidas consultas conforme a documentação

## 🧪 Rodando Testes
Os testes podem ser executados a partir dos seguintes comandos:

```bash
pip install -r tests/requirements_tests.txt
coverage run -m pytest -s -v tests
coverage report
```

## 🔥 Desafios
Durante a execução do projeto me deparei com alguns desafios para o deploy via pipeline do github actions. As roles de acesso para meu usuário do github estavam funcionando porém o setup de configuração da máquina remota requeria alguns passos que poderiam ser facilmente contornados com uma imagem da instância personalizada e consequentemente mais cara. Poderia fazer também o provisionamento de infraestrutura via Terraform e github actions mas despriorizei devido ao tempo para a entrega e por ter uma alternativa para fazer o deploy.

Dessa forma optei por fazer o build e push da imagem pelo github actions no docker hub e a partir dessa imagem, com as configurações de credenciais aws configuradas localmente, consegui fazer o deploy no ECS usando docker contex para criar o cluster e os services a partir do arquivo `docker-compose.prd.yml` do projeto que inicializa uma pipeline do CloudFormation com todos os recursos necessários para disponibilização pública do serviço.

## 📝 Oportunidades de melhoria
Para a evolução do projeto pude identificar alguns pontos de melhoria:
- Gerenciamento de usuários (hoje só tem o registro)
- Revisar usecases que podem ser melhor divididos em outras partes de dominio de negócios
- Usar uma fila apartada da aplicação via sdk para evitar perda de dados in memory em caso de falha do container da aplicação
- Aumentar a cobertura de testes para todo o projeto
- Adicionar documentação do swagger na aplicação de forma automática
- Correção para deploy inteiramente pelo github actions
- Provisionamento de infraestrutura via módulo Terraform na pipeline do github actions
- Criar uma distribution no CloudFront com a origin apontada para o endereço do load balancer para minimizar a latência das chamadas já  que o load balancer se encontra na região US North Virginia da AWS
- Registrar um domínio e criar um DNS no Route53 para acesso via nomes de domínio na URL 


## 👤 Autor
- Jocsã Kesley - Backend Developer
- Email - jocsadm@gmail.com
- Project Link: https://github.com/jocsakesley/logistics_indicators_api

## 📊 Status do projeto
- Development


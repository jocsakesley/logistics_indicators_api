# Logistics Indicators API

## 🗒️ Descrição
O projeto trata-se de uma API que permite o cadastro de clientes e atendimentos a partir da carga com arquivo .csv ou cadastro individual para compor uma base de dados logistica, e a partir das informações a geração de relatórios de indicadores de produtividade e SLA dos atendimentos dos técnicos logísticos (Green Angels).

## 🎯 Objetivos
- Cadastro, consulta, filtro, atualização e deleção de clientes (customers)
- Cadastro, consutta, filtro e atualização de atendimentos (customer_services)
- Carga de clientes e atendimentos a partir de arquivo .csv
- Consulta de indicadores de operação:
  - Produtividade por Green Angel
  - SLA de cada base logística
  - SLA de cada Green Angel

## ⚡ Principais Features

- Autenticação JWT com rotas de registro, login e refresh token
- [Script de geração de dados fictícios de clientes](https://github.com/jocsakesley/logistics_indicators_api/blob/main/utils/create_customers.py) a partir dos valores únicos da coluna `id_cliente` do arquivo de atendimentos
- Carga do arquivo de clientes e atendimentos a partir de uma rota http que faz o processamento assíncrono, com transformação dos dados de `data_de_atendimento` que estavam despadronizadaos, utilizando uma thread para recepção do arquivo e envio das linhas para uma fila, evitando bloqueio da requisição, e 100 threads para a leitura da fila e gravação no banco de dados em chunks de 2000 registros por vez.
- Consulta do total de registros para clientes e atendimentos nas rotas `/v1/customers/total` e `/v1/services/total`, facilitando o monitoramento da conclusão da carga batch.
- Consulta da rota `/v1/customers` com filtros para todos os campos (`email`, `nome` e `telefone`) e paginação a partir dos parameters `limit` e `offset`
- Consulta da rota `/v1/services` com filtros para todos os campos (`email`, `nome` e `telefone`) e paginação a partir dos parameters `limit` e `offset`
- Consuta da rota `/v1/indicators/productivity`, `/v1/indicators/sla/angel` e `/v1/indicators/sla/polo` com filtros de data (`start_date=YYYY-MM-DD` e `end_date=YYYY-MM-DD`) e ordenação (`sort_field=<total, total_sla, avg_time>`  e `desc=<true, false>`)
- Monitoramento das requisições através de logs com status e tempo de resposta, implementado a partir de um midlleware que calcula os tempos a cada requisição
![image](https://github.com/user-attachments/assets/769979f7-85a0-4cb2-a918-fa6b7542945b)
- Monitoramento do tempo de carga do arquivo batch através dos logs
- Testes unitários para os usecases que contém o core das regras de negócios
- Testes end-to-end foram feitos a partir de uma collection do postman
- Padronização de commits para cada tipo de alteração (feat, refactor, test, build, doc) 
- Execução do projeto a partir do docker compose
- Build e push da imagem para o docker hub através da pipeline do github actions
- Deploy da aplicação na AWS ECS a partir da pipeline do CloudFormation
- Aplicação desenvolvida seguindo princípios da orientação a objetos utilizando uma metodologia baseada na Clean Archtecture onde foram separadas as camadas de infra, controllers e usecases seguindo o seguinte fluxo:
  ![image](https://github.com/user-attachments/assets/b01a460a-7b7a-4bd3-84f9-9bdfbf5807e0)

  
## 🔧 Pré requisitos técnicos
- Containers Docker para a execução da API e do banco de dados.
- Python 3 com Flask para criação da API
- Banco de dados Postgresql
- Projeto entregue pelo github
- README com instruções para instalação e execução do projeto

## 🚀 Instalação e Setup
Para a execução do projeto é necessario que o [docker](https://docs.docker.com/engine/install/) e o [docker compose](https://docs.docker.com/compose/install/) estejam instalados

1. Clone o repositório
```bash
git clone https://github.com/jocsakesley/logistics_indicators_api.git
cd logistics_indicators_api
```

2. Configure as variáveis de ambiente (opcional)
 ```
 Arquivo .env disponibilizado no repositório apenas para desenvolvimento
 Para produção é recomendado que as variáveis sejam setadas de forma segura
 Variáveis do arquivo .env:
 POSTGRES_PASSWORD=postgres
 POSTGRES_USER=jocsa
 POSTGRES_DB=logistics
 POSTGRES_HOST=db
 JWT_SECRET_KEY=my-secret
```
3. Inicialize o docker (pelo docker desktop ou pelo teminal)
   
4. Rode o docker-compose
```bash
docker-compose up -d
```
5. Verifique que os containers da aplicação, db e adminer estão rodando
```bash
docker ps
```

## 📓 Documentação da API

A documentação pode ser baixada a partir [desse link](https://github.com/jocsakesley/logistics_indicators_api/blob/main/docs/logistics-api.postman_collection.json)   e importada para um client http como o postman ou baixar a [especificação openapi nesse link](https://github.com/jocsakesley/logistics_indicators_api/blob/main/docs/openapi.yaml) e importar no editor online [swagger editor](https://editor.swagger.io/) para uma melhor visualização.

<<<<<<< HEAD
## 💻 Como usar

- Faça o upload do arquivo `bd_desafio.csv` na rota `/v1/customers/batch`
- Monitore o total de linhas inseridas na rota `/v1/customers/total` (o total deve ser 573670)
- Faça o upload do arquivo `customers_data.csv` na rota `/v1/services/batch`
- Monitore o total de linhas inseridas na rota `/v1/services/total` (o total deve ser 1048575)
- Registre um usuário na rota `/v1/auth/register` com `username`, `email` e `password`
- Faça login na rota `/v1/auth/login` e copie o `access_token` retornado
- Faça as devidas consultas conforme a documentação, passando no header o key `Authorization` e no value `Bearer <access_token>` 
=======
Obs.: Para as consultas, é possível remover os filtros para trazer todos os resultados com paginação para clientes e atendimentos.
>>>>>>> 0985e0e (refactor: move files to docs e utils and update README.MD)

## 🧪 Rodando Testes
Os testes podem ser executados a partir dos seguintes comandos:

```bash
pip install -r tests/requirements_tests.txt
coverage run -m pytest -s -v tests
coverage report
```

## 🔥 Desafios
Durante a execução do projeto me deparei com alguns desafios para o deploy via pipeline do github actions. As roles de acesso para meu usuário do github estavam funcionando porém o setup de configuração da máquina remota requeria alguns passos que poderiam ser facilmente contornados com uma imagem da instancia personalizada e consequentemente mais cara.
Dessa forma optei por fazer o build e push da imagem pelo github actions no docker hub e a partir dessa imagem e com as configurações de credenciais configuradas localmente, consegui fazer o deploy no ECS usando docker contex para criar o cluster e os services a partir do docker-compose.prd.yml do projeto que inicializa uma pipeline do CloudFormation com todos os recursos necessários para disponibilização pública.

## 📝 Oportunidades de melhoria
Para a evolução do projeto pude identificar alguns pontos de melhoria:
- Gerenciamento de usuários (hoje só tem o registro)
- Correção para deploy inteiramente pelo github actions
- Revisar usecases que podem ser melhor divididos em outras partes
- Permitir configuração de threads, chuncks e sleep times para o processamento de arquivo batch a partir de variáveis de ambiente, garantindo o melhor tradeoff para produção (O tempo de processamento atual no endereço público está maior que ao rodar localmente, devido a limitação de configuração para evitar custos)
- Montagem de um volume do banco de dados para garantir a persistência de arquivos ou uso do banco de dados gerenciado na nuvem (deixei sem volume para facilitar a remoção dos dados da carga batch
- Aumentar a cobertura de testes para todo o projeto, bem como adicionar um job de testes na pipeline do github actions
- Adicionar documentação do swagger na aplicação de forma automática


## 👤 Autor
- Jocsã Kesley - Backend Developer
- Email - jocsadm@gmail.com
- Project Link: https://github.com/username/project-name](https://github.com/jocsakesley/logistics_indicators_api

## 📊 Status do projeto
- Development


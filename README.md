# TheCatAPI
### Desenho Arquitetural

![Arquitetura](/apps/architecture/arq.png)

### Collections
As collections encontram-se na pasta `apps/collections`

### Projeto:

1. Utilizei o projeto apenas com o banco local pois tentei subir para AWS mas não consegui, visto que deu alguns erros de Authorização, mas se fosse usar um banco de produção seria o RDS Aurora Postgres pois já tenho uma certa familiaridade

2. Utilizei hooks pois acredito que o projeto fica mais robusto e profissional, visto que não aceita quaisquer tipo de erros

3. Para subir uma cópia local, precisa:
- Ter o Poetry instalado em sua máquina
- Clonar este repositório em sua máquina
- Copiar o arquivo local.env e setar a chave de acesso para conseguir acessar os endpoints públicos da api
- Rodar o comando `poetry install` para instalar todas as dependências deste arquivo
- Criar um banco de dados com as especificações contidas no `settings.py` e rodar o comando dentro da pasta ./cat `python manage.py migrate` para persistir as mudanças das migrações no banco de dados

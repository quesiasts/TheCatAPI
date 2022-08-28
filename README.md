# TheCatAPI

Case The Cat API



1. Realize um desenho arquitetural informando como sua solução vai funcionar.


2. Crie uma aplicação utilizando Python para coletar as seguintes informações da API de Gatos (https://thecatapi.com/):


        - Para cada uma das raças de gatos disponíveis, armazenar as informações de origem, temperamento e descrição em uma base de dados (se disponível);

        - Para cada uma das raças acima, salvar o endereço de 3 imagens em uma base de dados (se disponível);

        - Salvar o endereço de 3 imagens de gatos com chapéu;

        - Salvar o endereço de 3 imagens de gatos com óculos.


3. Use uma base de dados(ex.: Dynamo AWS, RDS AWS, ...) adequada para armazenar as informações (você terá que justificar o uso dessa base)


4. Utilizando linguagem Python, crie 4 APIs REST, se possível utilizando-se de OpenAPI:

        a. API capaz de listar todas as raças;

        b. API capaz de listar as informações de uma raça;

        c. API capaz de a partir de um temperamento listar as raças;

        d. API capaz de a partir de uma origem listar as raças.



5. Crie uma coleção no Insomnia (ou se preferir no Postman) para consumir as APIs criadas (não se esqueça de incluir como parte da entrega)

6. Utilize alguma biblioteca de logging de forma que os eventos gerados sejam identificados corretamente, por exemplo: Warning, Erro, Debug, Info, etc.


7. Publique o projeto no Github e documente em um README.md os itens abaixo:

        a. Documentação do projeto;

        b. Documentação das APIs;

        c. Documentação de arquitetura;

        d. Instruções sobre como podemos subir uma cópia deste ambiente localmente




#### Bônus - se você chegou até aqui, considere implementar um ou mais itens a seguir:


8. (Bônus) Publique sua API na cloud (Ex.: AWS Lambda).

9. (Bônus) para o item 6 integre a aplicação a alguma ferramenta de Logging (exemplos:AWS Cloudwatch, Elastic Search, Splunk, Graylog ou similar), crie uma query que mostre em tempo real os eventos que acontecem na execução da API criada no item 6, exemplos (Warning, Erro, Debug, Info, etc).

10. (Bônus) para o item 4, implemente as mesmas rotas mas com retorno assíncrono - ou seja, o usuário irá informar um e-mail para o qual as imagens (URL's) devem ser enviadas. Utilize algum mecanismo de enfileiramento que preferir.

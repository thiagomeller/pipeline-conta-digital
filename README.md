# pipeline-conta-digital

Um projeto de criação de uma pipeline de dados para um sistema de banco digital, o qual permitiria que os usuários gerenciassem suas finanças de forma prática e segura. O app ofereceria funcionalidades para movimentação de contas, solicitação de empréstimos, investimento em aplicações financeiras, e cadastro de cartões de crédito e débito.

## Começando 

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte [Implantação](#implantação) para saber como implantar o projeto.

## Desenho de Arquitetura 

![Ingest](https://github.com/thiagomeller/pipeline-conta-digital/assets/100603408/905d7a53-3df5-4606-9215-3623c2062106)


## Pré-requisitos 

Caso for rodar em uma maquina local é necessário baixar e instalar o Phyton e Pymongo como ferramenta.

## Documentação

Atavés desse link você poderá acessar a documentação desse projeto: [Documentação  ](http://thiagomeller.github.io/pipeline-conta-digital/).

## Implantação

Utilizamos o ambiente da Azure + Databricks para fazer toda a implantação

## Ferramentas utilizadas

Ferramentas ultilizadas para a criação do projeto: 

* [Python](https://www.python.org/) - Usado para criar o script para as informações do banco.
* [VScode](https://code.visualstudio.com/) - IDE ultilizada para o desenvolvimento em python.
* [Databricks](https://www.databricks.com/) - Ambiente de automação, processamento e geração de dashboard.
* [MKdocs](https://www.mkdocs.org/) - Programa ultilzado para documentação do projeto.
* [MongoDB](https://www.mongodb.com/) - Usado para a inserção de dados.
  
## Colaboração 

Por favor, leia o [Colaboração](#colaboração) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

Se desejar publicar suas modificações em um repositório remoto no GitHub, siga estes passos:

1. Crie um novo repositório vazio no GitHub.
2. No terminal, navegue até o diretório raiz do projeto.
3. Execute os seguintes comandos:
```
git remote set-url origin https://github.com/seu-usuario/nome-do-novo-repositorio.git
git add .
git commit -m "Adicionar minhas modificações"
git push -u origin master
```
Isso configurará o repositório remoto e enviará suas modificações para lá.

## Versão 

Primeira versão do projeto sobre pipeline em esquema de banco digital.

## Autores 

* Adriano - Documentação e Apresentação - [AdrianoReusSavi](https://github.com/AdrianoReusSavi)
* Arthur - População do Banco de Dados - [ArthurDMelo](https://github.com/ArthurDMello)
* Guilherme - Dashboard - [guiDalmolin](https://github.com/GuiDalmolin)
* Jorge Antônio - Documentação e Apresentação - [JorgeAntonioJr](https://github.com/JorgeAntonioJr)
* Luiz Miguel - Criação e administração do Banco de Dados - [Miguelito001](https://github.com/Miguelito001)
* Thiago - Processamento de dados e Automação - [Thiagomeller](https://github.com/thiagomeller)
* yuri - Processamento de dados e Automação - link do git

## Licença 

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Referências

[Databricks](https://www.databricks.com/blog)
[Apache Spark](https://spark.apache.org/docs/latest/)
[Mkdocs](https://www.mkdocs.org/)

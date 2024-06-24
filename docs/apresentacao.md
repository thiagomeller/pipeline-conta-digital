---
hide:
  - navigation
---

# Apresentação

Para a disponibilização dos dados, foi escolhido o modelo dimensional One Big Table (OBT), que consiste em uma tabela única concentrando os dados processados da camada Gold.

## One Big Table (OBT)

O modelo dimensional OBT é adotado na camada Gold para consolidar os dados processados em uma única tabela. Isso facilita a análise e consulta dos dados, proporcionando uma visão integrada e simplificada para análises posteriores.

![OBT](assets/obt.png)

## KPIs (Key Performance Indicators)

Os KPIs são métricas essenciais derivadas dos dados processados que ajudam a monitorar e avaliar o desempenho da organização. Com o modelo OBT, é possível calcular e analisar diversos KPIs de maneira eficiente, garantindo uma visão clara e precisa dos aspectos críticos do negócio. Os KPIs utilizados incluem:

- **KPI:** KPI

## Dashboard

Os dados transformados no modelo OBT são utilizados para alimentar um dashboard interativo. Este dashboard permite visualizações avançadas e oferece uma ferramenta poderosa para a análise de dados e suporte à tomada de decisões. Com ele, é possível:

- Monitorar KPIs em tempo real.
- Visualizar tendências e padrões através de gráficos e tabelas.
- Realizar análises comparativas e detalhadas.
- Facilitar a comunicação de insights e resultados para a equipe e stakeholders.

![Dashboard](assets/dashboard.png)

## Conclusão

O pipeline descrito assegura que os dados sejam processados de maneira eficiente e organizada, começando com a coleta de dados não estruturados do MongoDB, passando por várias camadas de refinamento e enriquecimento (landing, bronze, silver) e culminando na camada Gold. Na camada Gold, os dados são transformados em um modelo dimensional OBT, que centraliza e simplifica a análise dos dados.

Essa abordagem facilita a criação de dashboards dinâmicos, que são alimentados pelos dados consolidados e transformados no OBT, proporcionando uma ferramenta poderosa para a tomada de decisões baseada em dados. A arquitetura Medalhão, aliada ao modelo OBT, garante que os dados sejam precisos, consistentes e prontos para análises detalhadas, contribuindo significativamente para o sucesso das iniciativas de business intelligence da organização.
# Mapeamento de preços de Airbnb
Mapeamento de acomodações da plataforma de Airbnb usando Python.

## Dados do Airbnb
Os dados das acomodações Airbnb da cidade do Rio de Janeiro estão disponíveis no seguinte link: http://insideairbnb.com/get-the-data/. Eu baixei o arquivo listings.csv para visualizar os dados referentes aos preços da diária em relação à localização da acomodação na cidade.

![Alt text](inside.png?raw=true "Optional Title")
## Arquivo .shp do Rio de Janeiro
Utilizei o arquivo Shapefile do município do Rio de Janeiro que está disponível em: https://www.data.rio/datasets/3cd6efde472441aaa6c1ad25075190e1/explore como base para o mapeamento dos preços. Esse tipo de arquivo é essencial para geoprocessamento, pois possui atributos de feições geográficas que são muito úteis para mapeamentos de dados e sua visualização.

## Bibliotecas usadas
Criei um arquivo chamado requirements.txt com todas bibliotecas necessárias para esse projeto, que são: geopandas, pandas, numpy, matplotlib e shapely. Depois utilizei o comando ``` pip install -r requirements.txt ``` para efetuar a instalação.








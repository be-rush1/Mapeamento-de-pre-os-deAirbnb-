import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point

if __name__ == '__main__':

    map = gpd.read_file("limites_municipio/limites_rj.shp") #crio dataframe relativo ao shapefile
    keys = ['longitude', 'latitude', 'price'] #seleciono as colunas relevantes para esse projeto
    df = pd.read_csv('listings.csv', skipinitialspace=True , usecols=keys) #crio meu dataframe

    #print(df.head().to_string(index=False))  Testar se estou referenciando os dados relevantes p/ visualização

    crs = {'init': 'epsg:4326'} # defino o coordinate reference system
    geo = [Point(coor) for coor in zip(df["longitude"], df["latitude"])] #transformando coordenadas do objeto zip em type geometry POINT do Shapely através de Point() e armazena em vetor
    geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geo) #crio geopanda dataframe com os pontos dentro de geo
    fig, ax = plt.subplots(figsize=(10, 10)) #cria figura
    map.plot(ax=ax) #usa mesmo eixo que a figura criada acima
    geo_df.plot(column='price', ax=ax, markersize=2, alpha=.7, cmap='hot', vmin=0, vmax=1000) #seta gradiente de cores dos pontos mesmo eixo que o map
    ax.set_xlabel('Latitude') #nomeia eixo x
    ax.set_ylabel('Longitude') #nomeia eixo y
    ax.set_title('Preços do airbnb na cidade do Rio de Janeiro') #dá título para imagem
    plt.show() #persiste imagem

    #print(geo_df.head().to_string(index=False)) #Testar se estou referenciando os dados relevantes p/ visualização



'''
    street_map = gpd.read_file("RJ_Municipios_2022/RJ_Municipios_2022.shp")
    fig, ax = plt.subplots(figsize = (10,10))
    street_map.plot(ax=ax)
    plt.show()
   '''





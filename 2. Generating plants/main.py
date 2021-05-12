
import pandas as pd
import geopandas
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import adjustText as aT

pd.set_option( 'display.max_columns' , 30 )
pd.set_option( 'display.max_rows' , 300 )
pd.set_option( 'display.width' , 3000 )

# Convert generating plants to geodata. Convert CRS to Projected National Grid for accurate distances
generators = pd.read_csv('plants.csv')[['BMUnitID','Latitude','Longitude','BMU Fuel Type','Name','Owner']]
generators = geopandas.GeoDataFrame(
    generators, geometry=geopandas.points_from_xy(generators.Longitude, generators.Latitude))
generators = generators.set_crs("EPSG:4326")
generators = generators.to_crs("EPSG:27700")
# print(generators)
print(generators.dtypes)
# print(generators.index.tolist())


# Convert generating plants to geodata. Convert CRS to Projected National Grid for accurate distances
dno = geopandas.read_file("dno.geojson")
dno=geopandas.GeoDataFrame(
    dno, geometry=dno.geometry)
dno = dno.to_crs("EPSG:27700")
print(dno)
# print(dno.index.tolist())

# Create column of nearest regions to each generating points for offshore sites
genloc=geopandas.GeoSeries(generators['geometry'], index=range(1,272))
dnoloc = geopandas.GeoSeries(dno['geometry'])
# print(genloc.head)
# print(genloc.dtypes)
# print(dnoloc)
# # print(dnoloc.dtypes)
for i, row in generators.iterrows():
    lat = row.iat[1]
    lon = row.iat[2]
    point = Point(lat,lon)
    print(dnoloc.boundary.distance(point))
# print(point)


# lon = generators['geometry'].x
# print(lat)
# print(lon)
# print(point)

# genloc.distance(dnoloc, align=False)

#
# def nearestdno(df):
#     listdno = []
#
#
#
#     generators['nearest']=near
# print(generators)




# Create column to include carbon emissions/MWh by fuel type average

# merge2 = geopandas.sjoin(generators, dno, how="inner", op='intersects')
# print(merge2)

# compiling BM generation readings and merge with corresponding generators geodata
# dtypes ={'TimeSeriesID': 'string' ,
#        'RegisteredResourceEICCode': 'string' ,
#        'BMUnitID': 'string' ,
#        'NGCBMUnitID': 'string' ,
#        'NGC': 'string' ,
#        'PSRType': 'string' ,
#        'MarketGenerationUnitEICCode': 'string' ,
#        'MarketGenerationBMUID': 'string' ,
#        'MarketGenerationNGCBMUnitID': 'string' ,
#        'SettlementDate': 'date_time',
#        'SP': int,
#        'Quantity(MW)': 'float'}
#
# sep = pd.read_csv('september.csv', dtype=dtypes, low_memory=False)
# oc = pd.read_csv( 'october.csv' , dtype=dtypes, low_memory=False)
# nov = pd.read_csv( 'november.csv', dtype=dtypes, low_memory=False)
# dec = pd.read_csv( 'december.csv', dtype=dtypes, low_memory=False)
# jan = pd.read_csv( 'january1.csv', dtype=dtypes, low_memory=False )
# feb = pd.read_csv( 'february1.csv', dtype=dtypes, low_memory=False)
# mar = pd.read_csv( 'march1.csv', dtype=dtypes, low_memory=False)
# combined = pd.concat([sep, oc, nov, dec, jan, feb, mar])[['BMUnitID','SettlementDate','SP','Quantity(MW)']]
# print(combined['SettlementDate'].dtype)
# merged = pd.merge(
#     combined,
#     generators,
#     how="left",
#     on= 'BMUnitID',
#     sort=False,
#     validate="many_to_one")





# fig, ax = plt.subplots()
# ax.set_aspect('equal')
# dno.plot(ax=ax, column='Name')
# generators.plot(ax=ax, color='black', markersize=0.1)
# generators.apply(lambda x: ax.annotate(text=x.Name, xy=x.loc['geometry'].coords[0], fontsize=1.5), axis=1)
# plt.axis('off')
# plt.savefig("graph.svg")
# plt.show()




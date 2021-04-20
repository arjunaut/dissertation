import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt



pd.set_option('display.max_columns', 40)
pd.set_option('display.min_rows', 3419)
pd.set_option('display.width', 10000)
pd.set_option('display.max_colwidth', 1500)

cable = gpd.read_file("datasets/Cable.shp")
lines = gpd.read_file("datasets/OHL.shp")
substations = gpd.read_file("datasets/Substations.shp")
towers = gpd.read_file("datasets/Towers.shp")
gb = gpd.read_file("gb/DNO_License_Areas_20200506.shp")


# View the first five rows of the data
print(cable)
print(lines)

lines.to_csv()

ax = gb.plot(figsize=(10, 10), color='none', edgecolor='gray', zorder=3)
cable.plot(color='red', ax=ax)
substations.plot(color='darkred', ax=ax)
substations.plot(color='darkblue', ax=ax)
# towers.plot(color='darkblue', ax=ax)
plt.savefig("graph.svg")
plt.show()

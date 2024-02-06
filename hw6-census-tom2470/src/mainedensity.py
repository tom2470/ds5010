import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import matplotlib as mpl
import contextily as cx
url="https://www2.census.gov/geo/tiger/TIGER2016/TRACT/tl_2016_23_tract.zip"
gdf=gpd.read_file(url)
gdf=gdf[gdf['ALAND'] > 0]
url="https://api.census.gov/data/2016/acs/acs5?get=B01001_001E&for=tract:*&in=county:*&in=state:23"
df=pd.read_json(url)
df.columns=df.iloc[0]
df.drop(index=0, inplace=True)
df.reset_index(drop=True, inplace=True)
df['GEOID']=df['state']+df['county']+df['tract']
df.drop(columns=['state','county','tract'],inplace=True)
gdfnew = gdf.merge(df, on="GEOID")
gdfnew['pop'] = gdfnew[['B01001_001E']].astype('int64')
type(gdfnew['pop'].iloc[0])
gdfnew['density'] = gdfnew['pop'] / gdfnew['ALAND'] * 2589988
cmap = mpl.cm.RdYlGn_r
lighter = colors.ListedColormap(cmap(np.linspace(0.125, 0.875, 256)))
bounds = np.array([0, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000])
norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
#cmap = mpl.cm.coolwarm
ax = gdfnew.plot(column='density', cmap=lighter, norm=norm, legend=True)
ax.set_title('Population/mile$^2$ for Census tracts');
plt.savefig("img/mainedensity.png")
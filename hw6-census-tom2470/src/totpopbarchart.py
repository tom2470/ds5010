import pandas as pd
import matplotlib.pyplot as plt
url = "https://api.census.gov/data/2016/acs/acs5?get=B01001_003E,B01001_004E,B01001_027E,B01001_028E,B01001_005E,B01001_006E,B01001_007E,B01001_029E,B01001_030E,B01001_031E,B01001_008E,B01001_009E,B01001_010E,B01001_011E,B01001_032E,B01001_033E,B01001_034E,B01001_035E,B01001_012E,B01001_013E,B01001_036E,B01001_037E,B01001_014E,B01001_015E,B01001_038E,B01001_039E,B01001_016E,B01001_017E,B01001_040E,B01001_041E,B01001_018E,B01001_019E,B01001_020E,B01001_021E,B01001_042E,B01001_043E,B01001_044E,B01001_045E,B01001_022E,B01001_023E,B01001_046E,B01001_047E,B01001_024E,B01001_025E,B01001_048E,B01001_049E&for=state:*"
df=pd.read_json(url)
ages={"<10":["B01001_003E", "B01001_004E", "B01001_027E", "B01001_028E"],"10-19":["B01001_005E", "B01001_006E", "B01001_007E", "B01001_029E", "B01001_030E", "B01001_031E"],"20-29":["B01001_008E", "B01001_009E", "B01001_010E", "B01001_011E", "B01001_032E", "B01001_033E", "B01001_034E", "B01001_035E"],"30-39":["B01001_012E", "B01001_013E", "B01001_036E", "B01001_037E"],"40-49":["B01001_014E", "B01001_015E", "B01001_038E", "B01001_039E"],"50-59":["B01001_016E", "B01001_017E", "B01001_040E", "B01001_041E"],"60-69":["B01001_018E", "B01001_019E", "B01001_020E", "B01001_021E", "B01001_042E", "B01001_043E", "B01001_044E", "B01001_045E"],"70-79":["B01001_022E", "B01001_023E", "B01001_046E", "B01001_047E"],"≥80":["B01001_024E", "B01001_025E", "B01001_048E", "B01001_049E"]}
states = {"01": "AL", "02": "AK", "04": "AZ", "05": "AR", "06": "CA", "08": "CO", "09": "CT", "10": "DE", "11": "DC", "12": "FL", "13": "GA", "15": "HI", "16": "ID", "17": "IL", "18": "IN", "19": "IA", "20": "KS", "21": "KY", "22": "LA", "23": "ME", "24": "MD", "25": "MA", "26": "MI", "27": "MN", "28": "MS", "29": "MO", "30": "MT", "31": "NE", "32": "NV", "33": "NH", "34": "NJ", "35": "NM", "36": "NY", "37": "NC", "38": "ND", "39": "OH", "40": "OK", "41": "OR", "42": "PA", "44": "RI", "45": "SC", "46": "SD", "47": "TN", "48": "TX", "49": "UT", "50": "VT", "51": "VA", "53": "WA", "54": "WV", "55": "WI", "56": "WY", "72": "PR"}
df.columns = df.iloc[0]
df=df.drop(df.index[0])
df['state']=df['state'].apply(lambda x: states[x])
df.set_index('state',drop=True, inplace=True)
df=df.apply(pd.to_numeric)
new_df = pd.DataFrame()
for x,y in ages.items(): 
  new_df[x]=df.loc[:,y].sum(axis=1)
new_df['total']=df.sum(axis=1)
new_df.sort_values(by='total', inplace=True, ascending=False)
new_df=new_df.drop(columns=['total'])
popbarchart=new_df.plot.bar(stacked=True, title='Stacked Bar Chart of Population').get_figure()
plt.savefig('img/totalpopbarchart.png')


import pandas as pd
import matplotlib.pyplot as plt
url = "https://api.census.gov/data/2016/acs/acs5?get=B01001_001E&for=state:*"
df=pd.read_json(url)
states = {"01": "AL", "02": "AK", "04": "AZ", "05": "AR", "06": "CA", "08": "CO", "09": "CT", "10": "DE", "11": "DC", "12": "FL", "13": "GA", "15": "HI", "16": "ID", "17": "IL", "18": "IN", "19": "IA", "20": "KS", "21": "KY", "22": "LA", "23": "ME", "24": "MD", "25": "MA", "26": "MI", "27": "MN", "28": "MS", "29": "MO", "30": "MT", "31": "NE", "32": "NV", "33": "NH", "34": "NJ", "35": "NM", "36": "NY", "37": "NC", "38": "ND", "39": "OH", "40": "OK", "41": "OR", "42": "PA", "44": "RI", "45": "SC", "46": "SD", "47": "TN", "48": "TX", "49": "UT", "50": "VT", "51": "VA", "53": "WA", "54": "WV", "55": "WI", "56": "WY", "72": "PR"}
df.columns = df.iloc[0]
df=df.iloc[1:]
df['state']=df['state'].apply(lambda x: states[x])
df['pop']=df['B01001_001E'].astype(int)
df.drop(columns='B01001_001E')
df.sort_values(by='pop', inplace=True, ascending=False)
totalpop=df.plot.bar(x='state',y='pop')
plt.savefig("img/totalpop.png")
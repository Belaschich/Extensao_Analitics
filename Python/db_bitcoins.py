'''carregar os dados e verificar se tem duplicadas de carteiras e
se tem duas pessoas usando a mesma carteira'''

import pandas as pd

df = pd.read_csv(r'C:\Users\izabe\Documents\GitHub\Extensao_Analitics\Python\MOCK_DATA.csv')
#print(df.dtypes)
#print(df.isna().sum())
#print(df["id"].is_unique)
#print(pd.unique(df["id"]))
#print(df[df.duplicated(['btc_address'], keep=False)])
#print(df[df.duplicated(['btc_address'], keep=False)].value_counts(['btc_address']))
#print(df[df.btc_address.duplicated(keep=False)].sort_values("first_name").value_counts("btc_address"))
df1 = df.groupby(["id", "btc_address", "first_name"]
                     ).btc_address.count().sort_values(ascending=False)
print(df1)
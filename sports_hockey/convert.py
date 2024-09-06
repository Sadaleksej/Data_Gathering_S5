import pandas as pd
with open('res.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)
df.to_csv('res_csv.csv', encoding='utf-8', index=False)
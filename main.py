import json

import pandas as pd

df = pd.read_csv('./datas/namsan_library_popular_books_2023_05.csv', encoding='EUC_KR', low_memory=False)
print(df.head())
print(df)

d = {"name": "mad"}
d_json = json.dumps(d, ensure_ascii=False)
print(d_json)
print(type(d_json))

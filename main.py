import pandas as pd

df = pd.read_csv('./datas/namsan_library_popular_books_2023_05.csv', encoding='EUC_KR', low_memory=False)
df.drop('Unnamed: 13', axis=1, inplace=True)
print(df.head())

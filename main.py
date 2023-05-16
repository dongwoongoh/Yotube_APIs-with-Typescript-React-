import pandas as pd

df = pd.read_csv('./datas/namsan_library_popular_books_2023_05.csv', encoding='EUC_KR', low_memory=False)
df.to_json('2023_05_popular_books', force_ascii=False)

selected_columns = df.columns != 'Unnamed: 13'
ns_books = df.loc[:, selected_columns]
print(ns_books.head())

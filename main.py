import pandas as pd

df = pd.read_csv('./datas/namsan_library_popular_books_2023_05.csv', encoding='EUC_KR', low_memory=False)
df.to_json('2023_05_popular_books', force_ascii=False)

print(df.head())

loc = df.loc[[0, 1], ['도서명', '등록일자']]
print(loc)

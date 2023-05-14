import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

library_auth_api_key = os.environ.get('LIBRARY_AUTH_KEY')
base_url = f'http://data4library.kr/api/loanItemSrch?authKey={library_auth_api_key}'

df = pd.read_csv('./datas/namsan_library_popular_books_2023_05.csv', encoding='EUC_KR', low_memory=False)
print(df.head())
print(library_auth_api_key)

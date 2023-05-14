import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()

library_auth_api_key = os.environ.get('LIBRARY_AUTH_KEY')
base_url = f'http://data4library.kr/api/loanItemSrch?authKey={library_auth_api_key}'
url = f'{base_url}&startDt=2023-04-01&endDt=2023-04-21'

response = requests.get(url)
print(response.content)

df = pd.read_csv('./datas/namsan_library_popular_books_2023_05.csv', encoding='EUC_KR', low_memory=False)
print(df.head())
print(library_auth_api_key)

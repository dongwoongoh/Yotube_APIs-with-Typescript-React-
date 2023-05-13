import chardet

with open('./datas/namsan_library_popular_books_2023_05.csv', mode='rb') as f:
    read_line = f.readline()
    encoding_detect = chardet.detect(read_line)
    print(encoding_detect)

import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'


def get_movies():

    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')

    post_title = []
    post_date = []
    post_expect = []

    for data in sp.find_all('div', class_='release_info'):
        try:

            titles = data.find('a')
            #print("電影名稱 : ", (titles.text).strip())
            post_title.append((titles.text).strip())

            dates = data.find('div', class_='release_movie_time')
            for i in dates:
                d = (i.text.strip())
            #print('上映日期 : ', d)
            post_date.append(d)

            expect = data.find('span')
            #print('觀眾期待度 : ', expect.text)
            post_expect.append(expect.text)

            for i in range(len(post_expect)):
                if post_expect[i] == '上映日期：':
                    post_expect[i] = '0%'
            post_expect = post_expect
            # print("-"*50)
        except:
            continue

    yahoo_dict = {"movie": post_title,
                  # "date": post_date,
                  "expect": post_expect,
                  }

    yahoo_df = pd.DataFrame(yahoo_dict)
    df = yahoo_df
    df1 = df.copy()

    listx = df1['movie']
    listy = df1['expect']
    listz = []
    datas = []

    for i in range(len(listy)):
        try:
            ans = (listy[i]).split("%")
            datas.append(ans)
            listz.append(int(datas[i][0]))
        except:
            continue
    final_dict = {'movie': post_title,
                  'expect': listz
                  }

    final_df = pd.DataFrame(final_dict)

    return final_df.columns.tolist(), final_df.values.tolist()

    # yahoo_reset=yahoo_dict_df.set_index('movie') #刪除原有的index，由第一行取代
    # yahoo_reset.to_csv("yahoomovie.csv",encoding='utf-8-sig')
    # print(yahoo_dict_df)

import pandas as pd
import requests
from bs4 import BeautifulSoup
# 獲取匯率
url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'


def getbank():
    # 獲取匯率更新時間
    t = requests.get(url)
    sp = BeautifulSoup(t.text, "lxml")
    cointime = sp.find('span', class_='time')
    cointime = cointime.text

    # 匯率表格
    df = pd.read_html(url)
    bankdata = df[0]
    bankdata = bankdata.iloc[:, 0:5]
    bankdata.columns = ["幣別", "現今匯率-本行買入",
                        "現今匯率-本行賣出", "即期匯率-本行買入", "即期匯率-本行賣出"]

    # 處理幣別重複
    coin = bankdata["幣別"]

    s = []
    for i in range(len(coin)):
        d = (coin[i][0:10])
        s.append(d)
    # print(s)
    bankdata = bankdata.drop(columns=["幣別"])
    #mydata ["幣別"]=s
    bankdata.insert(0, "幣別", s)

    return bankdata.columns.to_list(), bankdata.values.tolist(), cointime


'''
df = pd.read_html(url)
bankdata = df[0]
bankdata = bankdata.iloc[:, 0:5]
bankdata.columns = ["幣別", "現今匯率-本行買入", "現今匯率-本行賣出", "即期匯率-本行買入", "即期匯率-本行賣出"]

# 處理幣別重複
coin = bankdata["幣別"]

s = []
for i in range(len(coin)):
    d = (coin[i][0:10])
    s.append(d)
# print(s)
bankdata = bankdata.drop(columns=["幣別"])
#mydata ["幣別"]=s
bankdata.insert(0, "幣別", s)
print(bankdata)
'''

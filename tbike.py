import requests
import json
import pandas as pd

url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"


def get_taipeibike():
    response = requests.get(url)
    ybike = json.loads(response.text)
    df = pd.DataFrame.from_dict(ybike["retVal"], orient='index')

    # 篩選需要的欄位
    df1 = df.drop(["lat", "lng", "sareaen", "snaen",
                  "aren", "act", "sno"], axis=1)

    site, address, capacity, bikecount, spacecount, time = [], [], [], [], [], []

    for a in df1["sna"]:
        site.append(a)
    for b in df1["ar"]:
        address.append(b)
    for c in df1["tot"]:
        capacity.append(c)
    for d in df1["sbi"]:
        bikecount.append(d)
    for e in df1["bemp"]:
        spacecount.append(e)
    for f in df1["mday"]:
        time.append(f)

    tbike_dict = {"站名": site,
                  "地址": address,
                  "格位數": capacity,
                  "可借車輛數": bikecount,
                  "可停空位數": spacecount,
                  "更新時間": time
                  }
    taipei_bike = pd.DataFrame(tbike_dict)

    return taipei_bike.columns.tolist(), taipei_bike.values.tolist(), site

# myset=set()
# for i in df1["sarea"]:
#     myset.add(i)
# myset=list(myset)
# print(myset)

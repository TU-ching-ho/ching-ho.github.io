import json
import requests
import pandas as pd

url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Json'


def get_bike():
    response = requests.get(url)
    tbike = json.loads(response.text)
    df = pd.DataFrame(tbike, columns=('StationName', 'Address', 'Capacity',
                      'AvaliableBikeCount', 'AvaliableSpaceCount', 'UpdateTime'))

    site, address, capacity, bikecount, spacecount, time = [], [], [], [], [], []

    for a in df["StationName"]:
        site.append(a)
    for b in df["Address"]:
        address.append(b)
    for c in df["Capacity"]:
        capacity.append(c)
    for d in df["AvaliableBikeCount"]:
        bikecount.append(d)
    for e in df["AvaliableSpaceCount"]:
        spacecount.append(e)
    for f in df["UpdateTime"]:
        time.append(f)

    bike_dict = {"站名": site,
                 "地址": address,
                 "格位數": capacity,
                 "可借車輛數": bikecount,
                 "可停空位數": spacecount,
                 "更新時間": time
                 }

    tainan_bike = pd.DataFrame(bike_dict)
    # print(tainan_bike[0:1][0:])
    # print(tainan_bike.loc[0])

    return tainan_bike.columns.tolist(), tainan_bike.values.tolist(),  site


def looking_bike():
    response = requests.get(url)
    tbike = json.loads(response.text)
    df = pd.DataFrame(tbike, columns=('StationName', 'Address', 'Capacity',
                      'AvaliableBikeCount', 'AvaliableSpaceCount', 'UpdateTime'))

    site, address, capacity, bikecount, spacecount, time = [], [], [], [], [], []

    for a in df["StationName"]:
        site.append(a)
    for b in df["Address"]:
        address.append(b)
    for c in df["Capacity"]:
        capacity.append(c)
    for d in df["AvaliableBikeCount"]:
        bikecount.append(d)
    for e in df["AvaliableSpaceCount"]:
        spacecount.append(e)
    for f in df["UpdateTime"]:
        time.append(f)

    bike_dict = {"站名": site,
                 "地址": address,
                 "格位數": capacity,
                 "可借車輛數": bikecount,
                 "可停空位數": spacecount,
                 "更新時間": time
                 }

    tainan_bike = pd.DataFrame(bike_dict)
    return tainan_bike.columns.tolist(), tainan_bike.values.tolist()
    # print(tainan_bike.loc[0][0])
    # looking = input("輸入查詢車站")
    # for row in tainan_bike.values:
    #     if looking == row[0]:
    #         print(row[0])
    #         print(row[1])
    #         print(row[2])
    #         print(row[3])
    #         print(row[4])

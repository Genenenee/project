import csv
from array import *


# 全部
x = 1  # 日均線天數
best = 0  # 最高獲利
bestx = 0  # 最高獲利均線天數
bestt = 0 # 最高獲利的交易次數



#設定區
z = 30 # 均線日數上限
fileplace = ''#檔案位置  TX00_day.csv
    #檔案要用.csv檔     第一行跳過(標題)   每日收盤價在第2列  

#漲就買，繼續漲就繼續買，跌就全賣


# 以迴圈輸出每一列
while (x <= z):  # 每輪
    with open(fileplace, newline='') as csvfile:

        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        day = 0  # 第幾天
        cost = 0  # 當輪花費
        sell = 0  # 當輪售出總額
        total = 0 #共
        t = 0 #交易次數
        k = 0  # 持有
        yday = 0  # 昨天平均
        today = 0  # 今天平均
        a = array('f', [])

        for row in rows:


            p = 0  # 用來算每日的

            if (day == 0):
                day = day+1
                continue
            elif (day <= x):
                a.append(float(row[1]))
                for i in a:
                    p = p+i
                today = p/len(a)
            # print("today=",today)

                if (today > yday):
                    cost = cost+float(row[1])
                    k = k+1
                    t=t+1
                elif (today < yday):
                    sell = sell+k*float(row[1])
                    k = 0
                    t=t+1

            else:

                a.pop(0)
                a.append(float(row[1]))
                for i in a:
                    p = p+i
                today = p/len(a)
            # print("today=",today)
                if (today > yday):
                    cost = cost+float(row[1])
                    k = k+1
                    t=t+1
                elif (today < yday):
                    sell = sell+k*float(row[1])
                    k = 0
                    t=t+1

                # 每天
            day = day+1
            yday = today
            today = 0

    print(x, "日均線")
    print("cost=", cost)
    print("sell=", sell)
    print("k=", k)
    print("交易次數:",t)
    total = sell-cost+k*float(row[1])
    print("total =", total)
    if (best < total):
        best = total
        bestx = x
        bestt = t

    x = x+1
    csvfile.close
    
print("best:", best, " bestx:", bestx," 交易次數:",t)

import csv
from array import *
import matplotlib.pyplot as plt
import numpy as np 
x = 1  # 日均線x天數
best = 0  # 最高獲利
bestx = 0  # 最高獲利均線x天數
besty = 0   #最高獲利均線y天數
bestt = 0 # 最高獲利的交易次數
linex = []
liney = []
h = []         # 第一組數據高度
h2 = []        # 第二組數據高度



#設定區
z = 30 # 均線日數上限
fileplace = ''#檔案位置 TX00_day.csv
    #檔案要用.csv檔     第一行跳過(標題)   每日收盤價在第2列  

######短日均線(x)高過長日均線(y)就一直買，短比長低就全賣



while (x < z):  #外圈
    y = x+1  # 日均線y天數
    while(y<=z): #內圈
        with open(fileplace, newline='') as csvfile: 
            rows = csv.reader(csvfile)
            day = 0  # 第幾天
            cost = 0  # 當輪花費
            sell = 0  # 當輪售出總額
            k = 0  # 持有
            total = 0  #共
            t = 0 #交易次數
            yday = 0    #y均線今天的
            xday = 0    #x均線今天的
            a = array('f', [])
            b = array('f', [])
            for row in rows:
                px = 0  # 用來算x日的
                py = 0  # 用來算每日的
                if (day == 0): #第一行跳過
                    #print(x,",",y,"跳過第一行")
                    #print("目前cost=",cost," 目前sell=",sell," 目前k=",k)
                    day = day+1
                    continue
                elif (day <= x):   #第二行開始 xy都沒滿
                    #print(x,",",y,"都沒滿")
                    #print("目前cost=",cost," 目前sell=",sell," 目前k=",k)
                    a.append(float(row[1]))
                    for i in a:
                        px = px+i
                    xday = px/len(a)
                    b.append(float(row[1]))
                    for i in b:
                        py = py+i
                    yday = py/len(b)

                    if (xday > yday):
                        cost = cost+float(row[1])
                        k = k+1
                        t=t+1
                    elif (xday < yday):
                        sell = sell+k*float(row[1])
                        k = 0
                        t=t+1
                elif ((day > x) &  (day <= y)): #第二行開始 x滿y沒滿
                    #print(x,",",y,"x滿y沒滿")
                    #print("目前cost=",cost," 目前sell=",sell," 目前k=",k)
                    a.pop(0)
                    a.append(float(row[1]))
                    for i in a:
                        px = px+i
                    xday = px/len(a)
                    b.append(float(row[1]))
                    for i in b:
                        py = py+i
                    yday = py/len(b)
                    if (xday > yday):
                        cost = cost+float(row[1])
                        k = k+1
                        t=t+1
                    elif (xday < yday):
                        sell = sell+k*float(row[1])
                        k = 0
                        t=t+1
                
                else: #xy都滿
                    #print(x,",",y,"都滿")
                    #print("目前cost=",cost," 目前sell=",sell," 目前k=",k)
                    a.pop(0)
                    a.append(float(row[1]))
                    for i in a:
                        px = px+i
                    xday = px/len(a)
                    b.pop(0)
                    b.append(float(row[1]))
                    for i in b:
                        py = py+i
                    yday = py/len(b)
                    if (xday > yday):
                        cost = cost+float(row[1])
                        k = k+1
                        t=t+1
                    elif (xday < yday):
                        sell = sell+k*float(row[1])
                        k = 0
                        t=t+1
                day = day+1
                xday = 0
                yday = 0
            print(x, "日均線跟",y,"日均線")
            print("cost=", cost)
            print("sell=", sell)
            print("k=", k)
            print("交易次數:",t)
            total = sell-cost+k*float(row[1])
            print("total =", total)
        if (best < total):
            best = total
            bestx = x
            besty = y
            bestt = t
        y=y+1
        csvfile.close()
    x=x+1
print("best:", best, " bestx:", bestx," besty:",besty," 交易次數:",t)
#圖
with open(fileplace, newline='') as csvfile: 
            rows = csv.reader(csvfile)
            day = 0  # 第幾天
            cost = 0  # 當輪花費
            sell = 0  # 當輪售出總額
            k = 0  # 持有
            total = 0  #共
            t = 0 #交易次數
            yday = 0    #y均線今天的
            xday = 0    #x均線今天的
            a = array('f', [])
            b = array('f', [])
            for row in rows:
                px = 0  # 用來算x日的
                py = 0  # 用來算每日的
                if (day == 0): #第一行跳過
                    #print(x,",",y,"跳過第一行")
                    #print("目前cost=",cost," 目前sell=",sell," 目前k=",k)
                    day = day+1
                    continue
                elif (day <= bestx):   #第二行開始 xy都沒滿
                    #print(x,",",y,"都沒滿")
                    #print("目前cost=",cost," 目前sell=",sell," 目前k=",k)
                    a.append(float(row[1]))
                    for i in a:
                        px = px+i
                    xday = px/len(a)
                    b.append(float(row[1]))
                    for i in b:
                        py = py+i
                    yday = py/len(b)

                    if (xday > yday):
                        cost = cost+float(row[1])
                        k = k+1
                        t=t+1
                    elif (xday < yday):
                        sell = sell+k*float(row[1])
                        k = 0
                        t=t+1
                    linex.append((sell-cost)+(k*float(row[1])))
                    liney.append(row[0])
                elif ((day > bestx) &  (day <= besty)): #第二行開始 x滿y沒滿
                    #print(x,",",y,"x滿y沒滿")
                    #print("目前cost=",cost," 目前sell=",sell," 目前k=",k)
                    a.pop(0)
                    a.append(float(row[1]))
                    for i in a:
                        px = px+i
                    xday = px/len(a)
                    b.append(float(row[1]))
                    for i in b:
                        py = py+i
                    yday = py/len(b)
                    if (xday > yday):
                        cost = cost+float(row[1])
                        k = k+1
                        t=t+1
                    elif (xday < yday):
                        sell = sell+k*float(row[1])
                        k = 0
                        t=t+1
                    linex.append((sell-cost)+(k*float(row[1])))
                    liney.append(row[0])
                else: #xy都滿
                    #print(x,",",y,"都滿")
                    #print("目前cost=",cost," 目前sell=",sell," 目前k=",k)
                    a.pop(0)
                    a.append(float(row[1]))
                    for i in a:
                        px = px+i
                    xday = px/len(a)
                    b.pop(0)
                    b.append(float(row[1]))
                    for i in b:
                        py = py+i
                    yday = py/len(b)
                    if (xday > yday):
                        cost = cost+float(row[1])
                        k = k+1
                        t=t+1
                    elif (xday < yday):
                        sell = sell+k*float(row[1])
                        k = 0
                        t=t+1
                    linex.append((sell-cost)+(k*float(row[1])))
                    liney.append(row[0])
                day = day+1
                xday = 0
                yday = 0

title = ' best:', best,'  bestx:', bestx,' besty:',besty,' times:',t
plt.plot(liney,linex, 'r', linewidth=0.2)
plt.title(title)
plt.xticks(liney[::250],rotation=30)
plt.show()   



import csv
from array import *
import matplotlib.pyplot as plt
import numpy as np 
x = 1  # 日均線x天數
best = -99999999999  # 最高獲利
bestx = 0  # 最高獲利均線x天數
besty = 0   #最高獲利均線y天數
bestt = 0 # 最高獲利的交易次數
linex = []
liney = []
h = []         # 第一組數據高度
h2 = []        # 第二組數據高度
bestw=0
bestl=0
biggw = 0
biggl = 0
wwday = []
wwx = 0
wwy = 0
llday = []
llx = 0
lly = 0
bbw = 0
bbl = 0
bbwday = []
bblday = [] 
bwa = 0
bla = 0
awb = 0
alb = 0
awbx = 0
awby = 0
albx = 0
alby = 0

#設定區
z = 15 # 均線日數上限
fileplace = ''#檔案位置 TX00_day.csv
    #檔案要用.csv檔     第一行跳過(標題)   每日收盤價在第2列  
winover = 4000
#賺超過多少印出來
lossover = 1800
#手續費
fee = 12

#短日均線(x)高過長日均線(y)就一直買，短比長低就全賣

averagerecordw = [[j for j in range(z)] for i in range(z)]
averagerecordl = [[j for j in range(z)] for i in range(z)]
recordtotal = [[j for j in range(z)] for i in range(z)]


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
            tcost=0
            tsell=0
            twin=0
            tloss=0
            bigw = 0
            bigl = 0
            wday = []
            lday = []
            wa =0
            la =0
            wsc = 0
            lsc = 0
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
                        if(k>=0):
                            cost = cost+float(row[1])
                            tcost = tcost+float(row[1])
                            k = k+1
                            t=t+1
                        elif(k<0):
                            cost = cost-(k*float(row[1]))
                            tcost = tcost-(k*float(row[1]))
                            tcost=0
                            tsell=0
                            k = 0
                            t=t+1
                            
                    elif (xday < yday):
                        if(k>0):
                            sell = sell+(k*float(row[1]))
                            tsell = tsell+(k*float(row[1]))
                            if(tsell>tcost):
                                twin=twin+1
                                wsc = wsc+tsell-tcost
                                if(tsell-tcost>bigw):
                                    bigw = tsell-tcost
                                    wday = row[0]
                            elif(tsell<tcost):
                                tloss=tloss+1
                                lsc = lsc-tsell+tcost
                                if(tcost-tsell>bigl):
                                    bigl = tcost-tsell
                                    lday = row[0]
                            tcost=0
                            tsell=0
                            k = 0
                            t=t+1
                        elif(k<=0):
                            sell = sell+float(row[1])
                            tsell = tsell+float(row[1])
                            k = k-1
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
                        if(k>=0):
                            cost = cost+float(row[1])
                            tcost = tcost+float(row[1])
                            k = k+1
                            t=t+1
                        elif(k<0):
                            cost = cost-(k*float(row[1]))
                            tcost = tcost-(k*float(row[1]))
                            tcost=0
                            tsell=0
                            k = 0
                            t=t+1
                    elif (xday < yday):
                        if(k>0):
                            sell = sell+(k*float(row[1]))
                            tsell = tsell+(k*float(row[1]))
                            if(tsell>tcost):
                                twin=twin+1
                                wsc = wsc+tsell-tcost
                                if(tsell-tcost>bigw):
                                    bigw = tsell-tcost
                                    wday = row[0]
                            elif(tsell<tcost):
                                tloss=tloss+1
                                lsc = lsc-tsell+tcost
                                if(tcost-tsell>bigl):
                                    bigl = tcost-tsell
                                    lday = row[0]
                            tcost=0
                            tsell=0
                            k = 0
                            t=t+1
                        elif(k<=0):
                            sell = sell+float(row[1])
                            tsell = tsell+float(row[1])
                            k = k-1
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
                        if(k>=0):
                            cost = cost+float(row[1])
                            tcost = tcost+float(row[1])
                            k = k+1
                            t=t+1
                        elif(k<0):
                            cost = cost-(k*float(row[1]))
                            tcost = tcost-(k*float(row[1]))
                            tcost=0
                            tsell=0
                            k = 0
                            t=t+1
                    elif (xday < yday):
                        if(k>0):
                            sell = sell+(k*float(row[1]))
                            tsell = tsell+(k*float(row[1]))
                            if(tsell>tcost):
                                twin=twin+1
                                wsc = wsc+tsell-tcost
                                if(tsell-tcost>bigw):
                                    bigw = tsell-tcost
                                    wday = row[0]
                            elif(tsell<tcost):
                                tloss=tloss+1
                                lsc = lsc-tsell+tcost
                                if(tcost-tsell>bigl):
                                    bigl = tcost-tsell
                                    lday = row[0]
                            tcost=0
                            tsell=0
                            k = 0
                            t=t+1
                        elif(k<=0):
                            sell = sell+float(row[1])
                            tsell = tsell+float(row[1])
                            k = k-1
                            t=t+1
                day = day+1
                xday = 0
                yday = 0
                
                
            print(x, "日均線跟",y,"日均線")
            print("cost=", cost)
            print("sell=", sell)
            print("k=", k)
            print("交易次數:",t)
            total = sell-cost+(k*float(row[1]))-(fee*t)
            wa = wsc/twin
            print("賺的次數: ",twin,"平均賺: ",'%.3f'%wa)
            la = lsc/tloss
            print("賠的次數: ",tloss,"平均賠: ",'%.3f'%la)
            print("total =", total)
            print("一次賺最多: ",bigw,"在: ",wday)
            print("一次賠最多: ",bigl,"在: ",lday)
            print(" ")
        averagerecordw[x-1][y-1] = wa
        averagerecordl[x-1][y-1] = la
        recordtotal[x-1][y-1] = total

        if (best < total):
            best = total
            bestx = x
            besty = y
            bestt = t
            bestw = twin
            bestl = tloss
            bbw = bigw
            bbl = bigl
            bbwday = wday
            bblday = lday
            bwa = wa
            bla = la
        if(biggw<bigw):
            biggw = bigw
            wwday = wday
            wwx = x
            wwy = y
        if(biggl<bigl):
            biggl = bigl
            llday = lday
            llx = x
            lly = y
        if(wa>awb):
            awb= wa
            awbx = x
            awby = y

        if(la>alb):
            alb = la
            albx = x
            alby = y
        y=y+1
        csvfile.close()
    x=x+1
print("best:", best, " bestx:", bestx," besty:",besty," 交易次數:",t) #,"賺的次數: ",bestw,"平均賺: ",'%.3f'%bwa,"賠的次數: ",bestl,"平均賠: ",'%.3f'%bla,"勝率:",'%.3f'%(bestw/(bestw+bestl))
print("賺最多是在x= ",wwx,",y= ",wwy,"的",wwday," biggest win = ",biggw)
print("賠最多是在x= ",llx,",y= ",lly,"的",llday," biggest loss = ",biggl)
print("平均賺最多是在x= ",awbx,",y= ",awby,"  平均賺 = ",'%.3f'%awb)
print("平均賠最多是在x= ",albx,",y= ",alby,"  平均賠 = ",'%.3f'%alb)
print("平均賺超過",winover,": ")
for i in range(0,z-1):
    for j in range(1,z):
        if(averagerecordw[i][j]>winover):
            
            print("x: ",i," y: ",j," 平均賺: ",'%.3f'%averagerecordw[i][j]," 最後共:",recordtotal[i][j])
print("平均賠超過",lossover,": ")
for i in range(0,z-1):
    for j in range(1,z):
        if(averagerecordl[i][j]>lossover):
            print("x: ",i," y: ",j," 平均賠: ",'%.3f'%averagerecordl[i][j]," 最後共:",recordtotal[i][j])


#圖(先不印)
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



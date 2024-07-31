#TX跟四線比對 連續漲跌天數跟幅度的關係 (輸出excel檔)
#目前執行時會印出TX跟四線第一條的比對資料跟輸出TX跟四線比較的四個excel檔  
import csv
from array import *
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import sqlite3
import time
import functools
import sys 
from datetime import datetime
#用到的變數     四線編號  1up 2c1 3c2 4lo
op11 = 0  #紀錄數值
op12 = 0
op21 = 0
op22 = 0
op31 = 0
op32 = 0
op41 = 0
op42 = 0
op1pm = 0  #看正負
op2pm = 0
op3pm = 0
op4pm = 0
op1pmm = 0
op2pmm = 0
op3pmm = 0
op4pmm = 0
pmsum1 = 0  #連續的和
pmsum2 = 0  #連續的和
pmsum3 = 0  #連續的和
pmsum4 = 0  #連續的和
count1 = 0  #連續天數
count2 = 0  #連續天數
count3 = 0 #連續天數
count4 = 0  #連續天數
day1 = []
day2 = []
day3 = []
day4 = []
oij1p = [[]for i in range(200)]     #正開始日期
oij1m = [[]for i in range(200)]     #負開始日期
paverage1 = [[]for i in range(200)]  #正平均
maverage1 = [[]for i in range(200)]  #負平均
oij2p = [[]for i in range(200)]     #開始日期
oij2m = [[]for i in range(200)]     #開始日期
paverage2 = [[]for i in range(200)]  #平均
maverage2 = [[]for i in range(200)]  #平均
oij3p = [[]for i in range(200)]     #開始日期
oij3m = [[]for i in range(200)]     #開始日期
paverage3 = [[]for i in range(200)]  #平均
maverage3 = [[]for i in range(200)]  #平均
oij4p = [[]for i in range(200)]     #開始日期
oij4m = [[]for i in range(200)]     #開始日期
paverage4 = [[]for i in range(200)]  #平均
maverage4 = [[]for i in range(200)]  #平均
check = 0


TXi = 0
TX2 = 0
TXpm = 0
day = 0 #紀錄天數
total1 = 0  #同向天數
total2 = 0  #同向天數
total3 = 0  #同向天數
total4 = 0  #同向天數
start = 0 #日期對上
rowstart = 0 #row開始

##
TXXX = []
TX_date = []
up = []
cost1 = []
cost2 = []
lower = []
temp = 0
##

#讀TX
fileplace = ''  #TX檔案位置 我用的是 08/20/1998 ~12/09/2022 的檔案
    #檔案要用.csv檔     第一行跳過(標題)   每日收盤價在第2列  

#讀取四線 日期
conn = sqlite3.connect('')  #四線檔案位置(.db)   2001/12/24~2022/08/29  
df = pd.read_sql("SELECT date,upper,cost1,cost2,lower FROM four_line", conn)
        # 轉成時間戳
#########################################################################################################################################################
startday = '2002/01/02'  #2002 01 02            y/m/d  
endday = '2022/08/29'    #2022 08 29     
print1 = 0          
print2 = 0
print3 = 0
print4 = 0

#########################################################################################################################################################
date_list = df['date'].tolist()
printt = 0
if(print1|print2|print3|print4):
     printt = 1
if(	date_list.count(startday)==0):
    sys.exit("找不到開始日期")
if(	date_list.count(endday)==0):
    sys.exit("找不到結束日期")   
dlt = date_list.index(startday) 
startrow = startday.split('/')
startrowrow = startrow[1]+'/'+startrow[2]+'/'+startrow[0]
dltf = date_list.index(endday) 

if(dlt>0):
     rowstart = 1

# 2002 / 1 / 2 開始
with open(fileplace, newline='') as csvfile: 
    rows = csv.reader(csvfile)
    for row in rows:

        

        if(rowstart>0):
            if(row[0]== startrowrow):     
                start = 1
                
            if(start== 1):
            #TX
            #從第二天開始才會有比對  
                checkrow = row[0].split('/')
                
                checkrowrow = checkrow[2]+'/'+checkrow[0]+'/'+checkrow[1]
                temp = df['upper'][dlt].tolist()
                if(temp==0):
                    dlt=dlt+1
                    continue 
                if(date_list[dlt]!=checkrowrow):
                    dbcheck = date_list[dlt].split('/')
                    #
                    if(check<80):
                        #print("opi = ",date_list[dlt],"  TX =  ",checkrowrow)

                        #if(date_list[dlt]>checkrowrow):
                            #print("1111")
                        #else:
                            #print("2222")
                        check = check+1
                    #
                    if(checkrow[2]>dbcheck[0]):
                        while((checkrow[2]!=dbcheck[0])|(checkrow[0]!=dbcheck[1])|(checkrow[1]!=dbcheck[2])):
                            dlt=dlt+1
                            dbcheck = date_list[dlt].split('/')
                            #
                            if(check<80):
                                #print("opi = ",date_list[dlt],"  TX =  ",checkrowrow)

                                #if(date_list[dlt]>checkrowrow):
                                    #print("1111")
                                #else:
                                    #print("2222")
                                check = check+1
                            #
                    elif(checkrow[2]<dbcheck[0]): 
                        continue
                    elif(checkrow[0]>dbcheck[1]):
                        while((checkrow[2]!=dbcheck[0])|(checkrow[0]!=dbcheck[1])|(checkrow[1]!=dbcheck[2])):
                            dlt=dlt+1
                            dbcheck = date_list[dlt].split('/')
                            #
                            if(check<80):
                                #print("opi = ",date_list[dlt],"  TX =  ",checkrowrow)

                                #if(date_list[dlt]>checkrowrow):
                                    #print("1111")
                                #else:
                                    #print("2222")
                                check = check+1
                            #
                    elif(checkrow[0]<dbcheck[1]):
                        continue
                    elif(checkrow[1]>dbcheck[2]):
                        while((checkrow[2]!=dbcheck[0])|(checkrow[0]!=dbcheck[1])|(checkrow[1]!=dbcheck[2])):
                            dlt=dlt+1
                            dbcheck = date_list[dlt].split('/')
                            #
                            if(check<80):
                                #print("opi = ",date_list[dlt],"  TX =  ",checkrowrow)

                                #if(date_list[dlt]>checkrowrow):
                                    #print("1111")
                                #else:
                                    #print("2222")
                                check = check+1
                            #
                    elif(checkrow[1]<dbcheck[2]):
                        continue
                      
                         

               
                ###
                TXXX.append(float(row[1]))
                dayT = datetime.strptime(row[0],'%m/%d/%Y')
                TX_date.append(dayT)
                temp = df['upper'][dlt].tolist()
             
                up.append(int(temp))
                temp = df['cost1'][dlt].tolist()
                cost1.append(int(temp))
                temp = df['cost2'][dlt].tolist()
                cost2.append(int(temp))
                temp = df['lower'][dlt].tolist()
                lower.append(int(temp))



                ###
                
                if(printt):
                    print(" ")
                    print(checkrowrow)
                    
                if(printt):

                    print("day=",day)
                if(day==0):
                    TXi = row[1]
                    if(printt):
                        print("TXi = ",TXi)
                elif(day==1):
                    TX2 = row[1]
                    if(TX2>TXi):
                        TXpm = 1
                    else:
                        TXpm = 2
                    if(printt):
                        print("TXi = ",TXi)
                        print("TX2 = ",TX2)
                        print("TXpm = ",TXpm)
                else:
                    TXi = TX2
                    TX2 = row[1]
                    if(TX2>TXi):
                        TXpm = 1
                    else:
                        TXpm = 2  
                    if(printt):
                        print("TXi = ",TXi)
                        print("TX2 = ",TX2)
                        print("TXpm = ",TXpm)
                #opij
                
                if(day==0):
                    #讀資料
                    op11 = df['upper'][dlt].tolist()
                    op21 = df['cost1'][dlt].tolist()  
                    op31 = df['cost2'][dlt].tolist()
                    op41 = df['lower'][dlt].tolist()
                    if(print1):
                        print("op11 = ",op11)
                        print("op12 = ",op12)
                    if(print2):
                        print("op21 = ",op21)
                        print("op22 = ",op22)
                    if(print3):
                        print("op31 = ",op31)
                        print("op42 = ",op32)
                    if(print4):
                        print("op41 = ",op41)
                        print("op42 = ",op42)

                    day = 1
                elif(day==1):
                    op12 = df['upper'][dlt].tolist()
                    op22 = df['cost1'][dlt].tolist()  
                    op32 = df['cost2'][dlt].tolist()
                    op42 = df['lower'][dlt].tolist()   
                    
                    if(print1):
                        print("op11 = ",op11)
                        print("op12 = ",op12)
                    if(print2):
                        print("op21 = ",op21)
                        print("op22 = ",op22)
                    if(print3):
                        print("op31 = ",op31)
                        print("op32 = ",op32)
                    if(print4):
                        print("op41 = ",op41)
                        print("op42 = ",op42)
                    #比對
                    if(op11<op12):
                        op1pm = 1
                    
                        day = day+1
                    else:
                        op1pm = 2

                        day = day+1
                    if(print1):
                        print("op1pm =",op1pm)
                    if(op21<op22):
                        op2pm = 1

                    else:
                        op2pm = 2
                    if(print2):
                        print("op2pm =",op2pm)
                    if(op31<op32):
                        op3pm = 1

                    else:
                        op3pm = 2
                    if(print3):
                        print("op3pm =",op3pm)
                    if(op41<op42):
                        op4pm = 1

                    else:
                        op4pm = 2
                    if(print4):
                        print("op4pm =",op4pm)
                else:
                    op11 = op12
                    op21 = op22
                    op31 = op32
                    op41 = op42
                    op12 = df['upper'][dlt].tolist()
                    op22 = df['cost1'][dlt].tolist()  
                    op32 = df['cost2'][dlt].tolist()
                    op42 = df['lower'][dlt].tolist()   
                    if(print1):
                        print("op11 = ",op11)
                        print("op12 = ",op12)
                    if(print2):
                        print("op21 = ",op21)
                        print("op22 = ",op22)
                    if(print3):
                        print("op31 = ",op31)
                        print("op32 = ",op32)
                    if(print4):
                        print("op41 = ",op41)
                        print("op42 = ",op42)
                    if(op11<op12):
                        op1pm = 1
                        day = day+1
                    else:
                        op1pm = 2
                        day = day+1
                    if(print1):
                        print("op1pm =",op1pm)
                    if(op21<op22):
                        op2pm = 1

                    else:
                        op2pm = 2
                    if(print2):
                        print("op2pm =",op2pm)
                    if(op31<op32):
                        op3pm = 1

                    else:
                        op3pm = 2
                    if(print3):
                        print("op3pm =",op3pm)
                    if(op41<op42):
                        op4pm = 1

                    else:
                        op4pm = 2
                    if(print4):
                        print("op4pm =",op4pm)



                #兩個的對比  *****************************
                    #同向
                if(TXpm==op1pm):
                    if(print1):
                        print("op1同向")
                    if((TXpm != 0) & (count1==0)):   #同向第一天且昨天不同向
                        if(print1):    
                            print("op1同向第一天")
                            print("方向:",TXpm)
                        count1 = count1 + 1
                        total1 = total1 + 1 
                        day1.append(row[0])
                        pmsum1 = op12-op11
                    elif(TXpm!=0 ):                  #同向第n天
                        
                        if((TXpm==1) & (op1pmm==1)): #同正
                                if(print1):    
                                    print("11")
                                count1 = count1 + 1
                                total1 = total1 + 1
                                pmsum1 = pmsum1+op12-op11 
                                if(print1):    
                                    print("op1同向第",count1,"天")
                        elif((TXpm==2) & (op1pmm==2)): #同負
                                if(print1):    
                                    print("22")
                                count1 = count1 + 1
                                total1 = total1 + 1
                                pmsum1 = pmsum1+op12-op11
                                if(print1):    
                                    print("op1同向第",count1,"天")
                        elif((TXpm==1) & (op1pmm==2)):   #昨天同負今天同正
                                if(print1):    
                                    print("21")
                                total1 = total1 + 1 
                                l = len(day1)
                                oij1m[count1].append(day1[l-1])

                                maverage1[count1].append(pmsum1/count1)
                                count1 = 1
                                day1.append(row[0])
                                pmsum1 = op12-op11
                                if(print1):    
                                    print("op1同向第一天")
                        elif((TXpm==2) & (op1pmm==1)):  #昨天同正今天同負
                                if(print1):
                                    print("12")
                                total1 = total1 + 1 
                                l = len(day1)
                                oij1p[count1].append(day1[l-1])

                                paverage1[count1].append(pmsum1/count1)
                                count1 = 1
                                day1.append(row[0])
                                pmsum1 = op12-op11
                                if(print1):    
                                    print("op1同向第一天")
                        
                else:                       #沒有同向
                    if(count1!=0):          #到昨天還有同向(結算)
                        if(print1):
                            print("op1同向結束")
                        if(op1pmm==1):      #昨天正
                            l = len(day1)
                            oij1p[count1].append(day1[l-1])

                            paverage1[count1].append(pmsum1/count1)
                        elif(op1pmm == 2):  #昨天負
                            l = len(day1)
                            oij1m[count1].append(day1[l-1])

                            maverage1[count1].append(pmsum1/count1)   
                        count1 = 0
                        pmsum1 = 0

                
                if(TXpm==op2pm):
                    if(print2):
                        print("op2同向")
                    if((TXpm != 0) & (count2==0)):   #同向第一天且昨天不同向
                        if(print2):    
                            print("op2同向第一天")
                            print("方向:",TXpm)
                        count2 = count2 + 1
                        total2 = total2 + 1 
                        day2.append(row[0])
                        pmsum2 = op22-op21
                    elif(TXpm!=0 ):                  #同向第n天
                        
                        if((TXpm==1) & (op2pmm==1)): #同正
                                if(print2):    
                                    print("11")
                                count2 = count2 + 1
                                total2 = total2 + 1
                                pmsum2 = pmsum2+op22-op21 
                                if(print2):    
                                    print("op2同向第",count2,"天")
                        elif((TXpm==2) & (op2pmm==2)): #同負
                                if(print2):    
                                    print("22")
                                count2 = count2 + 1
                                total2 = total2 + 1
                                pmsum2 = pmsum2+op22-op21
                                if(print2):    
                                    print("op1同向第",count2,"天")
                        elif((TXpm==1) & (op2pmm==2)):   #昨天同負今天同正
                                if(print2):    
                                    print("21")
                                total2 = total2 + 1 
                                l = len(day2)
                                oij2m[count2].append(day2[l-1])

                                maverage2[count2].append(pmsum2/count2)
                                count2 = 1
                                day2.append(row[0])
                                pmsum2 = op22-op21
                                if(print2):    
                                    print("op2同向第一天")
                        elif((TXpm==2) & (op2pmm==1)):  #昨天同正今天同負
                                if(print2):
                                    print("12")
                                total2 = total2 + 1 
                                l = len(day2)
                                oij2p[count2].append(day2[l-1])

                                paverage2[count2].append(pmsum2/count2)
                                count2 = 1
                                day2.append(row[0])
                                pmsum2 = op22-op21
                                if(print2):    
                                    print("op2同向第一天")
                        
                else:                       #沒有同向
                    if(count2!=0):          #到昨天還有同向(結算)
                        if(print2):
                            print("op2同向結束")
                        if(op2pmm==1):      #昨天正
                            l = len(day2)
                            oij2p[count2].append(day2[l-1])

                            paverage2[count2].append(pmsum2/count2)
                        elif(op2pmm == 2):  #昨天負
                            l = len(day2)
                            oij2m[count2].append(day2[l-1])

                            maverage2[count2].append(pmsum2/count2)   
                        count2 = 0
                        pmsum2 = 0




                if(TXpm==op3pm):
                    if(print3):
                        print("op3同向")
                    if((TXpm != 0) & (count3==0)):   #同向第一天且昨天不同向
                        if(print3):    
                            print("op3同向第一天")
                            print("方向:",TXpm)
                        count3 = count3 + 1
                        total3 = total3 + 1 
                        day3.append(row[0])
                        pmsum3 = op32-op31
                    elif(TXpm!=0 ):                  #同向第n天
                        
                        if((TXpm==1) & (op3pmm==1)): #同正
                                if(print3):    
                                    print("11")
                                count3 = count3 + 1
                                total3 = total3 + 1
                                pmsum3 = pmsum3+op32-op31 
                                if(print3):    
                                    print("op3同向第",count1,"天")
                        elif((TXpm==2) & (op3pmm==2)): #同負
                                if(print3):    
                                    print("22")
                                count3 = count3 + 1
                                total3 = total3 + 1
                                pmsum3 = pmsum3+op32-op31
                                if(print3):    
                                    print("op3同向第",count3,"天")
                        elif((TXpm==1) & (op3pmm==2)):   #昨天同負今天同正
                                if(print3):    
                                    print("21")
                                total3 = total3 + 1 
                                l = len(day3)
                                oij3m[count3].append(day3[l-1])

                                maverage3[count3].append(pmsum3/count3)
                                count3 = 1
                                day3.append(row[0])
                                pmsum3 = op32-op31
                                if(print3):    
                                    print("op3同向第一天")
                        elif((TXpm==2) & (op3pmm==1)):  #昨天同正今天同負
                                if(print3):
                                    print("12")
                                total3 = total3 + 1 
                                l = len(day3)
                                oij3p[count3].append(day3[l-1])

                                paverage3[count3].append(pmsum3/count3)
                                count3 = 1
                                day3.append(row[0])
                                pmsum3 = op32-op31
                                if(print2):    
                                    print("op3同向第一天")
                        
                else:                       #沒有同向
                    if(count3!=0):          #到昨天還有同向(結算)
                        if(print3):
                            print("op3同向結束")
                        if(op3pmm==1):      #昨天正
                            l = len(day3)
                            oij3p[count3].append(day3[l-1])

                            paverage3[count3].append(pmsum3/count3)
                        elif(op3pmm == 2):  #昨天負
                            l = len(day3)
                            oij3m[count3].append(day3[l-1])

                            maverage3[count3].append(pmsum3/count3)   
                        count3 = 0
                        pmsum3 = 0



                if(TXpm==op4pm):
                    if(print4):
                        print("op4同向")
                    if((TXpm != 0) & (count4==0)):   #同向第一天且昨天不同向
                        if(print4):    
                            print("op4同向第一天")
                            print("方向:",TXpm)
                        count4 = count4 + 1
                        total4 = total4 + 1 
                        day4.append(row[0])
                        pmsum4 = op42-op41
                    elif(TXpm!=0 ):                  #同向第n天
                        
                        if((TXpm==1) & (op4pmm==1)): #同正
                                if(print4):    
                                    print("11")
                                count4 = count4 + 1
                                total4 = total4 + 1
                                pmsum4 = pmsum4+op42-op41 
                                if(print4):    
                                    print("op4同向第",count4,"天")
                        elif((TXpm==2) & (op4pmm==2)): #同負
                                if(print4):    
                                    print("22")
                                count4 = count4 + 1
                                total4 = total4 + 1
                                pmsum4 = pmsum4+op42-op41
                                if(print4):    
                                    print("op4同向第",count4,"天")
                        elif((TXpm==1) & (op4pmm==2)):   #昨天同負今天同正
                                if(print4):    
                                    print("21")
                                total4 = total4 + 1 
                                l = len(day4)
                                oij4m[count4].append(day4[l-1])

                                maverage4[count4].append(pmsum4/count4)
                                count4 = 1
                                day4.append(row[0])
                                pmsum4 = op42-op41
                                if(print4):    
                                    print("op4同向第一天")
                        elif((TXpm==2) & (op4pmm==1)):  #昨天同正今天同負
                                if(print4):
                                    print("12")
                                total4 = total4 + 1 
                                l = len(day4)
                                oij4p[count4].append(day4[l-1])

                                paverage4[count4].append(pmsum4/count4)
                                count4 = 1
                                day4.append(row[0])
                                pmsum4 = op42-op41
                                if(print4):    
                                    print("op4同向第一天")
                        
                else:                       #沒有同向
                    if(count4!=0):          #到昨天還有同向(結算)
                        if(print4):
                            print("op4同向結束")
                        if(op4pmm==1):      #昨天正
                            l = len(day4)
                            oij4p[count4].append(day4[l-1])

                            paverage4[count4].append(pmsum4/count4)
                        elif(op4pmm == 2):  #昨天負
                            l = len(day4)
                            oij4m[count4].append(day4[l-1])

                            maverage4[count4].append(pmsum4/count4)   
                        count4 = 0
                        pmsum4 = 0
                
                dlt=dlt+1
                op1pmm=op1pm
                op2pmm=op2pm
                op3pmm=op3pm
                op4pmm=op4pm
            if(dlt>dltf):
                
                rowstart=0   
csvfile.close()                
        
               
#輸出
#共同向

with open('D:/ncue/work/data/output1.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['從',startday,'到',endday,'在',day,'天中同向:',total1,'天'])
    writer.writerow(['正負', '連續天數', '開始日期','平均'])

        
    l = 0
    #連續天數跟幅度關係
    #正連續
    for i in range (0,199):
        l = len(oij1p[i])
        if(l!=0):
            sumpav1=0 
            for j in range (0,l):
                #print("從",oij1p[i][j],"開始的平均為",paverage1[i][j])
                writer.writerow(['正', i, oij1p[i][j],paverage1[i][j]])
                sumpav1=sumpav1+paverage1[i][j]
            writer.writerow(['平均: ',sumpav1/l])


    #負連續
    for i in range (0,199):
        l = len(oij1m[i])
        if(l!=0):
            summav1=0
            for j in range (0,l):
                #print("從",oij1m[i][j],"開始的平均為",maverage1[i][j])
                writer.writerow(['負', i, oij1m[i][j],maverage1[i][j]])
                summav1=summav1+maverage1[i][j]
            writer.writerow(['平均: ',summav1/l])

csvfile.close()             

with open('D:/ncue/work/data/output2.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['從',startday,'到',endday,'在',day,'天中同向:',total2,'天'])
    writer.writerow(['正負', '連續天數', '開始日期','平均'])

        
    l = 0
    #連續天數跟幅度關係
    #正連續
    for i in range (0,199):
        l = len(oij2p[i])
        if(l!=0):
            sumpav2=0
            for j in range (0,l):
                #print("從",oij2p[i][j],"開始的平均為",paverage2[i][j])
                writer.writerow(['正', i, oij2p[i][j],paverage2[i][j]])
                sumpav2=sumpav2+paverage2[i][j]
            writer.writerow(['平均: ',sumpav2/l])


    #負連續
    for i in range (0,199):
        l = len(oij2m[i])
        if(l!=0):
            summav2=0
            for j in range (0,l):
                #print("從",oij2m[i][j],"開始的平均為",maverage2[i][j])
                writer.writerow(['負', i, oij2m[i][j],maverage2[i][j]])
                summav2=summav2+maverage2[i][j]
            writer.writerow(['平均: ',summav2/l])

csvfile.close() 
with open('D:/ncue/work/data/output3.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['從',startday,'到',endday,'在',day,'天中同向:',total3,'天'])
    writer.writerow(['正負', '連續天數', '開始日期','平均'])

        
    l = 0
    #連續天數跟幅度關係
    #正連續
    for i in range (0,199):
        l = len(oij3p[i])
        if(l!=0):
            sumpav3=0
            for j in range (0,l):
                #print("從",oij3p[i][j],"開始的平均為",paverage3[i][j])
                writer.writerow(['正', i, oij3p[i][j],paverage3[i][j]])
                sumpav3=sumpav3+paverage3[i][j]
            writer.writerow(['平均: ',sumpav3/l])


    #負連續
    for i in range (0,199):
        l = len(oij3m[i])
        if(l!=0):
            summav3=0
            for j in range (0,l):
                #print("從",oij3m[i][j],"開始的平均為",maverage3[i][j])
                writer.writerow(['負', i, oij3m[i][j],maverage3[i][j]])
                summav3=summav3+maverage3[i][j]
            writer.writerow(['平均: ',summav3/l])

csvfile.close() 

with open('D:/ncue/work/data/output4.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['從',startday,'到',endday,'在',day,'天中同向:',total4,'天'])
    writer.writerow(['正負', '連續天數', '開始日期','平均'])

        
    l = 0
    #連續天數跟幅度關係
    #正連續
    for i in range (0,199):
        l = len(oij4p[i])
        if(l!=0):
            sumpav4=0
            for j in range (0,l):
                #print("從",oij4p[i][j],"開始的平均為",paverage4[i][j])
                writer.writerow(['正', i, oij4p[i][j],paverage4[i][j]])
                sumpav4=sumpav4+paverage4[i][j]
            writer.writerow(['平均: ',sumpav4/l])



    #負連續
    for i in range (0,199):
        l = len(oij4m[i])
        if(l!=0):
            summav4=0
            for j in range (0,l):
                #print("從",oij4m[i][j],"開始的平均為",maverage4[i][j])
                writer.writerow(['負', i, oij4m[i][j],maverage4[i][j]])
                summav4=summav4+maverage4[i][j]
            writer.writerow(['平均: ',summav4/l])
csvfile.close() 
###
#plt.subplot(411)
#plt.plot(TX_date,TXXX,color=(255/255,100/255,100/255),linewidth='0.5',markersize="1",marker = '.')        #橘色為k線
#plt.plot(TX_date,up,color=(100/255,100/255,255/255),linewidth='0.5',markersize="1",marker = '.')        #藍色為d線

#plt.subplot(412)
#plt.plot(TX_date,TXXX,color=(255/255,100/255,100/255),linewidth='0.5',markersize="1",marker = '.')        #橘色為k線
#plt.plot(TX_date,cost1,color=(100/255,100/255,255/255),linewidth='0.5',markersize="1",marker = '.')        #藍色為d線

#plt.subplot(413)
#plt.plot(TX_date,TXXX,color=(255/255,100/255,100/255),linewidth='0.5',markersize="1",marker = '.')        #橘色為k線
#plt.plot(TX_date,cost2,color=(100/255,100/255,255/255),linewidth='0.5',markersize="1",marker = '.')        #藍色為d線

#plt.subplot(414)
#plt.plot(TX_date,TXXX,color=(255/255,100/255,100/255),linewidth='0.5',markersize="1",marker = '.')        #橘色為k線
#plt.plot(TX_date,lower,color=(100/255,100/255,255/255),linewidth='0.5',markersize="1",marker = '.')        #藍色為d線

#plt.show()
###

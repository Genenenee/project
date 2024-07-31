import datetime
import os
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#每天抓TX用的

driver = webdriver.Chrome('') #chromedriver位置

driver.get("https://www.taifex.com.tw/cht/3/dlOptDailyMarketView") # 網址

element = driver.find_element("name", "queryStartDate") #開始日期
date = str(datetime.date.today()).replace("-","/")
element.send_keys(date)
element = driver.find_element("name", "queryEndDate") #結束日期
element.send_keys(date)

time.sleep(1)

select_element = driver.find_element(By.ID,'commodity_idt')  #選擇
select_object = Select(select_element)

time.sleep(1)

select_object.select_by_value("all")

time.sleep(1)

select_element = driver.find_element(By.ID,'commodity_idt') #選擇*2次
select_object = Select(select_element)

time.sleep(1)

select_object.select_by_value("TXO")

time.sleep(1)

dc = driver.find_element("xpath","/html/body/div[1]/div[4]/div[2]/div/div[2]/table[1]/tbody/tr[3]/td/input") #下載
ActionChains(driver).double_click(dc).perform()

time.sleep(5)

driver.close() # 關閉瀏覽器視窗
driver.quit()



# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:33:25 2021

@author: agente3z
"""
import time
import winsound
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe") #change your firefox.exe path
driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\Users\\agent\\Desktop\\Desktop\\geckodriver.exe") #change your geckodriver.exe path

driver.set_window_position(0, 0)

driver.get('https://warframe.market/items/saryn_prime_set') #if you want to change item then just change the link
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[1]/button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/section/section/div[1]/button').click()
time.sleep(1)

while 1==1:

    contatore=0
    
    for uwu in range(5):
        try:
            time.sleep(1)
            contatore+=1
            stringa='/html/body/section/section/div/section[2]/div[3]/div[2]/div[2]/div/div['+str(contatore)+']/div[4]'
            ordine=driver.find_element_by_xpath(stringa)
            ordine=ordine.get_attribute('outerHTML')
            
            prezzo=int(ordine[101:104])
            
            if prezzo<=210: #210 is the price you'll get alerted, you can change it
                print('orcodio svegliate')
                
                for _ in range(2):
                    winsound.Beep(1000, 600)
                    time.sleep(0.1)
                    winsound.Beep(1000, 600)
                    time.sleep(0.4)




                
        except:
            print('orcaccia la madonna')
    
    time.sleep(10)
    driver.refresh()
    time.sleep(5)
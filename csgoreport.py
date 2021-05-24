from selenium import webdriver
from bs4 import BeautifulSoup
import pylint
import os
import sys
import threading
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver1 = webdriver.Chrome(PATH)
driver2 = webdriver.Chrome(PATH)
driver3 = webdriver.Chrome(PATH)

site1 = "http://csgoreportbot.net"
site2 = "https://www.vedbex.com/tools/csgo_reportbot"
site3 = "https://extremereportbot.com/main/"


def go_SITE1(crDriver):
    crDriver.get(site1)
    inputID = crDriver.find_element_by_id('player_profile')
    inputID.send_keys(SteamID)
    find = crDriver.find_element_by_id('find-player')
    find.click()
    isloaded = False
    
    while isloaded == False:
        isloaded = crDriver.find_element_by_id('pName').is_displayed()
    
    confirmbtn = crDriver.find_element_by_id('submit_s_2')
    confirmbtn.click()
    confirmbtn2 = crDriver.find_element_by_id('submit_s_3')
    confirmbtn2.click()
    confirmbtn3 = crDriver.find_element_by_id('submit_s_4')
    confirmbtn3.click()
    time.sleep(12)

def go_SITE2(crDriver):
    crDriver.get(site2)


def go_SITE3(crDriver):
    crDriver.get(site3)
    inputID = crDriver.find_element_by_id('steamuser')
    inputID.send_keys(SteamID)
    findbtn = crDriver.find_element_by_id('finduser')
    findbtn.click()



n = len(sys.argv)
if n != 2:
    print("Ce programme doit avoir un Steam ID en argument !!!")
    input("Appuies sur n'importe quelle touche pour terminer")
    sys.exit()


SteamID = sys.argv[1]

thread1 = threading.Thread(target=go_SITE1, args=[driver1])
thread2 = threading.Thread(target=go_SITE2, args=[driver2])
thread3 = threading.Thread(target=go_SITE3, args=[driver3])
#thread1.start()
#thread2.start()
thread3.start()



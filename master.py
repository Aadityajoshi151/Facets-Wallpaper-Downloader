from selenium import webdriver
from datetime import datetime
import wget
import time
import os


print("""
This bot is designed by Aaditya Joshi.
It is meant to automate the process of downloading the wallpapers made by the famous digital artist Justin Maller.
It is only capable of downloading the wallpapers from http://www.facets.la/ that HAVE the download link on the website as some of the wallpapers do not.
This bot is only used for automated downloading. Aaditya Joshi DOES NOT have the ownership of the website or the artwork present there.
 """)
while(True):
    choice = str(input("Do You Want To Start? (y/n)\n"))
    if choice.lower() == "y":
        break
    elif choice.lower() == "n":
        quit()
driver_path = "WebDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)

os.mkdir("Images")
starttime = datetime.now()
driver.get("http://www.facets.la/2013/1/")
for i in range(1,366):
    daynum = driver.find_element_by_xpath('//*[@id="content"]/div[3]/p/span[1]/strong').text
    title = driver.find_element_by_xpath('//*[@id="content"]/div[3]/h1').text
    try:
        downloadlink = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[9]/a').get_attribute("href")
        print(f'Day - {daynum}: "{title}" Downloading...')
        wget.download(downloadlink, out = "Images/")
        print("\n")
        time.sleep(1.75)
    except:  
        print(f'Day - {daynum}: "{title}" Not Available For Download\n')
    if i < 365:
        nextlink = driver.find_element_by_xpath('//*[@id="search-box-next"]/a')
        nextlink.click()
driver.quit()
endtime = datetime.now()
print(f"Time Taken (hh:mm:ss.milliseconds) - {endtime-starttime}")
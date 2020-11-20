from selenium import webdriver
import wget
import time
import os

driver_path = "WebDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)

#todo Short desc and type to start
#todo Remove unnecessary variables
os.mkdir("Images")
driver.get("http://www.facets.la/2013/1/")
for i in range(1,11):
    daynum = driver.find_element_by_xpath('//*[@id="content"]/div[3]/p/span[1]/strong')
    title = driver.find_element_by_xpath('//*[@id="content"]/div[3]/h1')
    try:
        downloadlink = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[9]/a')
        imageurl = downloadlink.get_attribute("href")
        print(f"\nDay - {daynum.text}: {title.text} Downloading...")
        filename = wget.download(imageurl, out = "Images/")
        time.sleep(2.5)
    except:  
        print(f"\nDay - {daynum.text}: {title.text} Not Available For Download")
    nextlink = driver.find_element_by_xpath('//*[@id="search-box-next"]/a')
    nextlink.click()
driver.quit()
from selenium import webdriver
import wget
import time
import os

while(True):
    choice = str(input("Do You Want To Start? (y/n)\n"))
    if choice.lower() == "y":
        break
    elif choice.lower() == "n":
        quit()
driver_path = "WebDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)

#todo Short desc and type to start
#todo Remove unnecessary variables

os.mkdir("Images")
driver.get("http://www.facets.la/2013/1/")
for i in range(1,11):
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
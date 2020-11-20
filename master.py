from selenium import webdriver
import wget
import time
driver_path = "WebDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)
#todo Ask for download location in the starting.
#todo Remove unnecessary variables
driver.get("http://www.facets.la/2013/1/")
for i in range(1,11):
    daynum = driver.find_element_by_xpath('//*[@id="content"]/div[3]/p/span[1]/strong')
    title = driver.find_element_by_xpath('//*[@id="content"]/div[3]/h1')
    try:
        downloadlink = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[9]/a')
        imageurl = downloadlink.get_attribute("href")
        print(f"Day - {daynum.text}: {title.text} Downloading...\n")
        filename = wget.download(imageurl, out = "Images/")
        time.sleep(3)
    except:  
        print(f"Day - {daynum.text}: {title.text} Not Available For Download\n")
    nextlink = driver.find_element_by_xpath('//*[@id="search-box-next"]/a')
    nextlink.click()
driver.quit()
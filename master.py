from selenium import webdriver

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
        flag = True #todo remove the flag varible altogther
    except:
        flag = False
    print(f"Day - {daynum.text}: {title.text} {flag}")
    nextlink = driver.find_element_by_xpath('//*[@id="search-box-next"]/a')
    nextlink.click()
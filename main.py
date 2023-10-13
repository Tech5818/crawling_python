from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 웹 드라이버 설정
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

# 
url = "https://comic.naver.com/index"
driver.get(url)

driver.implicitly_wait(10)
elements = driver.find_elements(by=By.CSS_SELECTOR, value="#container > div.content_wrap > div.Aside__aside_wrap--iF5ju.Aside__type_home_logout--R6qSd > div:nth-child(2) > ul > li > div.AsideList__info_area--PVPwn > a.ContentTitle__title_area--x24vt > span > span")

for element in elements:
    print(element.text)

driver.quit()
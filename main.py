from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json

# 웹 드라이버 설정
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

# 네이버 웹툰 인기순위 크롤링
# url = "https://comic.naver.com/index"
# driver.get(url)

# driver.implicitly_wait(15)
# elements = driver.find_elements(by=By.CSS_SELECTOR, value="#container > div.content_wrap > div.Aside__aside_wrap--iF5ju.Aside__type_home_logout--R6qSd > div:nth-child(2) > ul > li > div.AsideList__info_area--PVPwn > a.ContentTitle__title_area--x24vt > span > span")

# i = 1
# rank ={}
# for element in elements:
#     rank[i] = element.text
#     i = i+1
# print(rank)

# json_data = json.dumps(rank, ensure_ascii=False, indent=2)

# with open("data.json", "w", encoding="utf-8") as json_file:
#     json_file.write(json_data)

url = "https://www.melon.com"
driver.get(url)
driver.implicitly_wait(10)
elements = driver.find_elements(by=By.XPATH, value='//*[@id="conts"]/div[5]/div/ul/li[1]/div/ul/li/div[2]/div[2]/p/a')

i = 1
melon_rank = {}
for element in elements:
    melon_rank[i] = element.text
    i = i+1

json_data = json.dumps(melon_rank, ensure_ascii=False, indent=2)

with open("data.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

driver.quit()
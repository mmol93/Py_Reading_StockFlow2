import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


## EWY 지수 얻기 위한 파일임 - ok

def EWY_Graph():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    # 구글에 접속
    driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
    url = "https://kr.investing.com/etfs/ishares-south-korea-index-historical-data"
    driver.get(url)
    time.sleep(2)

    price_list = []
    # 일주일치 price 데이터 얻기 - ok
    for i in range(1, 8):
        price_xpath = "//*[@id='curr_table']/tbody/tr[" + str(i) + "]/td[2]"
        price_element = WebDriverWait(driver, 20). \
        until(EC.presence_of_all_elements_located((By.XPATH, price_xpath)))

        price_list.append(price_element[0].text)

    change_list = []
    # 일주일치 change 데이터 얻기 - ok
    for i in range(1, 8):
        change_xpath = "//*[@id='curr_table']/tbody/tr[" + str(i) + "]/td[7]"
        change_element = WebDriverWait(driver, 20). \
            until(EC.presence_of_all_elements_located((By.XPATH, change_xpath)))

        change_list.append(change_element[0].text)

    # 일주일치 Date 데이터 얻기 - ok
    date_list = []
    for i in range(1, 8):
        date_xpath = "//*[@id='curr_table']/tbody/tr[" + str(i) + "]/td[1]"
        date_element = WebDriverWait(driver, 20). \
            until(EC.presence_of_all_elements_located((By.XPATH, date_xpath)))

        date_list.append(date_element[0].text)


    # 출력할 데이터 - ok
    show_list = []

    show_list.append("EWY 지수: ")
    show_list.append(date_list[0])
    show_list.append(price_list[0])
    show_list.append(change_list)
    show_list.append(driver.current_url)

    print(show_list)

    driver.close()
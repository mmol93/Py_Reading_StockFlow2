import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


## 달러 인덱스 지수 얻기 위한 파일임 - ok

def KdollarIndex():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
    url = "https://finance.daum.net/exchanges/FRX.KRWUSD" # 다음 달러 환율
    driver.get(url)
    time.sleep(2)

    change_list = []
    change_integrate = 0
    # 10일치 change 데이터 얻기 - ok
    for i in range(1, 11):
        change_xpath = "//*[@id='boxHistories']/div[1]/div[2]/div/table/tbody/tr[" + str(i) + "]/td[4]/span"
        change_element = WebDriverWait(driver, 30). \
            until(EC.presence_of_all_elements_located((By.XPATH, change_xpath)))

        change_list.append(change_element[0].text)
        change_element = change_element[0].text  # 원하는 항목만 가져옴
        change_element = change_element[:-1]    # 마지막에 %를 제거해준다

        change_integrate = change_integrate + float(change_element)

    show_List = []

    show_List.append("10일간 누적%: " + str(round(change_integrate, 2)) + "%")
    show_List.append(change_list)
    show_List.append(driver.current_url)

    print("<한국 달러 인덱스(10일간)> ", end="")
    print(show_List)    # 결과값 출력

    return round(change_integrate, 2)
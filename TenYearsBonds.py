from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def america():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
    url = "https://kr.investing.com/rates-bonds/u.s.-10-year-bond-yield-historical-data"  # 인베스팅_10년물 채권 수익률
    driver.get(url)

    price_list = []
    # 일주일치 price 데이터 얻기 - ok
    for i in range(1, 8):
        price_xpath = "//*[@id='curr_table']/tbody/tr[" + str(i) + "]/td[2]"
        price_element = WebDriverWait(driver, 25). \
            until(EC.presence_of_all_elements_located((By.XPATH, price_xpath)))

        price_list.append(price_element[0].text)

    change_list = []
    # 일주일치 change 데이터 얻기 - ok
    for i in range(1, 8):
        change_xpath = "//*[@id='curr_table']/tbody/tr[" + str(i) + "]/td[6]"
        change_element = WebDriverWait(driver, 25). \
            until(EC.presence_of_all_elements_located((By.XPATH, change_xpath)))

        change_list.append(change_element[0].text)

    change_integrate = 0

    # 14일치 change 데이터 얻기 - ok
    for i in range(1, 15):
        change_xpath = "//*[@id='curr_table']/tbody/tr[" + str(i) + "]/td[6]"
        change_element = WebDriverWait(driver, 25). \
            until(EC.presence_of_all_elements_located((By.XPATH, change_xpath)))

        change_element = change_element[0].text
        change_element = change_element[:-1]
        change_integrate = change_integrate + float(change_element)

    # 일주일치 Date 데이터 얻기 - ok
    date_list = []
    for i in range(1, 8):
        date_xpath = "//*[@id='curr_table']/tbody/tr[" + str(i) + "]/td[1]"
        date_element = WebDriverWait(driver, 25). \
            until(EC.presence_of_all_elements_located((By.XPATH, date_xpath)))

        date_list.append(date_element[0].text)

        # 출력할 데이터 - ok
        show_list = []

        show_list.append("미국 10년 채권: ")
        show_list.append(date_list[0])
        show_list.append(str(round(change_integrate, 2))+"%")
        show_list.append(change_list)
        show_list.append(driver.current_url)

        print(show_list)

        driver.close()

        # 몇 일 연속으로 오르고 or 내렸는지 화인
        plus = 0  # 플러스일 경우 +1
        minus = 0  # 마이너스일 경우 +1
        plus_plus = 0  # 연속 +
        minus_minus = 0  # 연속 -
        stoper = 0
        for i in range(0, 7):
            singleData = change_list[i]
            # 수급의 플러스, 마이너스 확인하기
            if singleData[0] == "-":
                minus += 1
            else:
                plus += 1
                # 순매도의 경우에는 부호 -가 붙지만
                # 순매수의 경우에는 부호가 붙지않아서 붙여줌
                singleData = "+" + str(singleData)

            # 연속 + or - 확인하기
            if i == 0 and plus == 1:
                plus_plus = 1
            elif i == 0 and minus == 1:
                minus_minus = 1

            # 부호의 경우 마이너스는 -가 붙지만 플러스는 바로 숫자로 표기됨
            if i >= 1 and singleData[0] == "+" and plus_plus >= 1 and stoper == 0:
                plus_plus += 1
            elif i >= 1 and singleData[0] == "-" and plus_plus >= 1 and stoper == 0:
                stoper = 1
            elif i >= 1 and singleData[0] == "-" and minus_minus >= 1 and stoper == 0:
                minus_minus += 1
            elif i >= 1 and singleData[0] == "+" and minus_minus >= 1 and stoper == 0:
                stoper = 1

        return change_integrate
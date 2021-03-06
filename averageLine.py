from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import controlExcel
import time
import controlExcel

# 코스피의 5일, 20일, 60일, 120일 평균선을 구한다
# 매개변수 = 다음 금융의 코스피 or 코스닥
def index(url, index):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)

    driver.get(url)

    # 실시간 시세의 경우 상승/하락에 따라 selector 값이 달라진다
    try:
        # 하락 시
        selctor = "#boxDashboard > div.currentStk > div > span.numB.down > strong"
        cur_kospi = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selctor))).text
    except:
        # 상승 시
        selctor = "#boxDashboard > div.currentStk > div > span.numB.up > strong"
        cur_kospi = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selctor))).text

    # 실시간 코스피 or 코스닥 등락률
    try:
        xpath = "//*[@id='boxDashboard']/div[1]/div/span[1]/p[2]"
        cur_kospiRatio = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).text
    except:
        selector = "#boxDashboard > div.currentStk > div > span.numB.up > p:nth-child(3)"
        cur_kospiRatio = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).text

    # 코스피 or 코스닥 지난 기록 가져오기
    history = []
    i = 1  # 표의 row
    j = 1  # 표의 페이지

    # print(cur_kospi)
    # print(cur_kospiRatio)

    # 120일치의 데이터를 얻어온다
    # i는 아래의 루프에서 사용되지 않고 그냥 카운트를 위해서 쓰일뿐임
    while len(history) < 120:
        # j는 코스피 데이터가 있는 표의 row에 해당한다
        # 해당 표는 10개의 row만 있기 때문에 i의 초기화와 페이지를 넘기는 작업이 필요하다
        if i == 11:
            # 페이지 클릭하여 넘기기
            xpath = f"//*[@id='boxDailyHistory']/div[2]/div/div/a[{j}]"
            nextPage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            # 다음 페이지 클릭
            nextPage.click()
            # 페이지를 넘긴 후 잠깐 기다린다
            time.sleep(4)
            i = 1
            j += 1
        # 현재 보고 있는 표에서 데이터 얻기(10일치 데이터 얻을 수 있음)
        xpath = f"//*[@id='boxDailyHistory']/div[2]/div/table/tbody/tr[{i}]/td[2]/span"
        data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).text
        # 숫자형 데이터로 바꾸기 위해선 콤마(,)를 제거해야한다
        data = data.replace(",", "")
        # 데이터를 숫다로 바꾼다
        history.append(float(data))
        i += 1
    # 5일
    average5 = round(sum(history[:5]) / 5, 1)

    # 20일
    average20 = round(sum(history[:20]) / 20, 1)

    # 60일
    average60 = round(sum(history[:60]) / 60, 1)

    # 120일
    average120 = round(sum(history) / len(history), 1)

    print(f"현재값: {cur_kospi}")
    print(f"average5: {average5}")
    print(f"average20: {average20}")
    print(f"average60: {average60}")
    print(f"average120: {average120}")

    # 엑셀에 기록 후 저장
    controlExcel.writeIndex(index, average5, average20, average60, average120)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 20일 간의 수급을 가져온다

def TwldayCompanyKOSPI():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("disable-gpu")

        driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
        url = "https://finance.daum.net/domestic/investors/KOSPI"  # 다음_주식_거래원 코스피 일자별 매매
        driver.get(url)

        xpath1 = "//*[@id='boxDays']/div[2]/div/table/tbody/tr["
        xpath2 = "]/td[4]"

        total = []  # 마지막에 출력할 데이터 집합
        plus = 0   # 플러스일 경우 +1
        minus = 0   # 마이너스일 경우 +1
        plus_plus = 0   # 연속 +
        minus_minus = 0 # 연속 -
        accumulate_sum = 0  # 20일간 매도량, 매수량의 누적 계산 데이터
        stoper = 0

        for i in range(1, 11):
            xpath = xpath1 + str(i) + xpath2
            singleData = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath))).text

            # 수급의 플러스, 마이너스 확인하기
            if singleData[0] == "-":
                minus += 1
            else:
                plus += 1
                # 순매도의 경우에는 부호 -가 붙지만
                # 순매수의 경우에는 부호가 붙지않아서 붙여줌
                singleData = "+" + str(singleData)

            # 연속 + or - 확인하기
            if i == 1 and plus == 1:
                plus_plus = 1
            elif i == 1 and minus == 1:
                minus_minus = 1

            # 부호의 경우 마이너스는 -가 붙지만 플러스는 바로 숫자로 표기됨
            if i >= 2 and singleData[0] == "+" and plus_plus >= 1 and stoper == 0:
                plus_plus += 1
            elif i >= 2 and singleData[0] == "-" and plus_plus >= 1 and stoper == 0:
                stoper = 1
            elif i >= 2 and singleData[0] == "-" and minus_minus >= 1 and stoper == 0:
                minus_minus += 1
            elif i >= 2 and singleData[0] == "+" and minus_minus >= 1 and stoper == 0:
                stoper = 1

            # 누적 계산하기
            # 10일간의 기관 매도 + 매수 누적 값을 구한다
            singleData = singleData.replace(",", "")
            accumulate_sum = int(singleData) + accumulate_sum

            # i = 10이 됐을 경우 해당 페이지의 기관 정보 수집은 끝났다
            # 그러므로 다음 페이지로 넘어가야할 필요가 있다
            if i == 10:
                xpathSecondPage = "//*[@id='boxDays']/div[2]/div/div/a[1]"
                nextPage = driver.find_element_by_xpath("//*[@id='boxDays']/div[2]/div/div/a[1]")
                nextPage.click()
                time.sleep(10)


        # 똑같이 한 번 더 반복하면 20일 간의 기록을 얻을 수 있다
        for i in range(1, 11):
            xpath = xpath1 + str(i) + xpath2
            singleData = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath))).text

            # 수급의 플러스, 마이너스 확인하기
            if singleData[0] == "-":
                minus += 1
            else:
                plus += 1
                # 순매도의 경우에는 부호 -가 붙지만
                # 순매수의 경우에는 부호가 붙지않아서 붙여줌
                singleData = "+" + str(singleData)

            # 연속 + or - 확인하기
            if i == 1 and plus == 1:
                plus_plus = 1
            elif i == 1 and minus == 1:
                minus_minus = 1

            # 부호의 경우 마이너스는 -가 붙지만 플러스는 바로 숫자로 표기됨
            if i >= 2 and singleData[0] == "+" and plus_plus >= 1 and stoper == 0:
                plus_plus += 1
            elif i >= 2 and singleData[0] == "-" and plus_plus >= 1 and stoper == 0:
                stoper = 1
            elif i >= 2 and singleData[0] == "-" and minus_minus >= 1 and stoper == 0:
                minus_minus += 1
            elif i >= 2 and singleData[0] == "+" and minus_minus >= 1 and stoper == 0:
                stoper = 1

            # 누적 계산하기
            # 10일간의 기관 매도 + 매수 누적 값을 구한다
            singleData = singleData.replace(",", "")
            accumulate_sum = int(singleData) + accumulate_sum

        # 수집한 데이터들 모아서 total에 넣어서 리스트 만들기
        if plus_plus >= 1:
            total.append(str(plus_plus) + "일 연속 매수")
        elif minus_minus >= 1:
            total.append(str(minus_minus) + "일 연속 매도")
        total.append("(" + str(plus) + ")일 매수")
        total.append("(" + str(minus) + ")일 매도")
        total.append(accumulate_sum)
        total.append(driver.current_url)

        # 출력 메시지 설정
        print("<코스피 20일간 기관 누적 수급> ", end="")
        print(total)

        # 다른 요소와 연계하기 위해 반환값 주기
        if plus_plus >= 1:
            return "+" + str(plus_plus)
        elif minus_minus >= 1:
            return "-" + str(minus_minus)
    except:
        print("코스피 기관 수급 20일치 가져오기 - 현물 통신에러")

# 20일 간의 코스닥 외인 기록을 가져온다
def TwldayCompanyKOSDAQ():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("disable-gpu")

        driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
        url = "https://finance.daum.net/domestic/investors/KOSDAQ"  # 다음_주식_거래원 코스닥 일자별 매매
        driver.get(url)

        xpath1 = "//*[@id='boxDays']/div[2]/div/table/tbody/tr["
        xpath2 = "]/td[4]"

        total = []  # 마지막에 출력할 데이터 집합
        plus = 0   # 플러스일 경우 +1
        minus = 0   # 마이너스일 경우 +1
        plus_plus = 0   # 연속 +
        minus_minus = 0 # 연속 -
        accumulate_sum = 0  # 20일간 매도량, 매수량의 누적 계산 데이터
        stoper = 0

        for i in range(1, 11):
            xpath = xpath1 + str(i) + xpath2
            singleData = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath))).text

            # 수급의 플러스, 마이너스 확인하기
            if singleData[0] == "-":
                minus += 1
            else:
                plus += 1
                # 순매도의 경우에는 부호 -가 붙지만
                # 순매수의 경우에는 부호가 붙지않아서 붙여줌
                singleData = "+" + str(singleData)

            # 연속 + or - 확인하기
            if i == 1 and plus == 1:
                plus_plus = 1
            elif i == 1 and minus == 1:
                minus_minus = 1

            # 부호의 경우 마이너스는 -가 붙지만 플러스는 바로 숫자로 표기됨
            if i >= 2 and singleData[0] == "+" and plus_plus >= 1 and stoper == 0:
                plus_plus += 1
            elif i >= 2 and singleData[0] == "-" and plus_plus >= 1 and stoper == 0:
                stoper = 1
            elif i >= 2 and singleData[0] == "-" and minus_minus >= 1 and stoper == 0:
                minus_minus += 1
            elif i >= 2 and singleData[0] == "+" and minus_minus >= 1 and stoper == 0:
                stoper = 1

            # 누적 계산하기
            # 10일간의 기관 매도 + 매수 누적 값을 구한다
            singleData = singleData.replace(",", "")
            accumulate_sum = int(singleData) + accumulate_sum

            # i = 10이 됐을 경우 해당 페이지의 기관 정보 수집은 끝났다
            # 그러므로 다음 페이지로 넘어가야할 필요가 있다
            if i == 10:
                xpathSecondPage = "//*[@id='boxDays']/div[2]/div/div/a[1]"
                nextPage = driver.find_element_by_xpath("//*[@id='boxDays']/div[2]/div/div/a[1]")
                nextPage.click()
                time.sleep(10)

        # 똑같이 한 번 더 반복하면 20일 간의 기록을 얻을 수 있다
        for i in range(1, 11):
            xpath = xpath1 + str(i) + xpath2
            singleData = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath))).text

            # 수급의 플러스, 마이너스 확인하기
            if singleData[0] == "-":
                minus += 1
            else:
                plus += 1
                # 순매도의 경우에는 부호 -가 붙지만
                # 순매수의 경우에는 부호가 붙지않아서 붙여줌
                singleData = "+" + str(singleData)

            # 연속 + or - 확인하기
            if i == 1 and plus == 1:
                plus_plus = 1
            elif i == 1 and minus == 1:
                minus_minus = 1

            # 부호의 경우 마이너스는 -가 붙지만 플러스는 바로 숫자로 표기됨
            if i >= 2 and singleData[0] == "+" and plus_plus >= 1 and stoper == 0:
                plus_plus += 1
            elif i >= 2 and singleData[0] == "-" and plus_plus >= 1 and stoper == 0:
                stoper = 1
            elif i >= 2 and singleData[0] == "-" and minus_minus >= 1 and stoper == 0:
                minus_minus += 1
            elif i >= 2 and singleData[0] == "+" and minus_minus >= 1 and stoper == 0:
                stoper = 1

            # 누적 계산하기
            # 10일간의 기관 매도 + 매수 누적 값을 구한다
            singleData = singleData.replace(",", "")
            accumulate_sum = int(singleData) + accumulate_sum

        # 수집한 데이터들 모아서 total에 넣어서 리스트 만들기
        if plus_plus >= 1:
            total.append(str(plus_plus) + "일 연속 매수")
        elif minus_minus >= 1:
            total.append(str(minus_minus) + "일 연속 매도")
        total.append("(" + str(plus) + ")일 매수")
        total.append("(" + str(minus) + ")일 매도")
        total.append(accumulate_sum)
        total.append(driver.current_url)

        # 출력 메시지 설정
        print("<코스닥 20일간 기관 누적 수급> ", end="")
        print(total)

        # 다른 요소와 연계하기 위해 반환값 주기
        return accumulate_sum
    except:
        print("코스닥 기관 수급 20일치 가져오기 - 현물 통신에러")
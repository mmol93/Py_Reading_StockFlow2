from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


### 신용잔고 확인 (7일분) - 오르면 안좋음

def customerCredit():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("disable-gpu")

        driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
        url = "https://finance.naver.com/sise/sise_deposit.nhn"  # 네이버_증시자금동향
        driver.get(url)

        xpath1 = "//*[@id='contentarea_left']/div[3]/table[1]/tbody/tr["
        xpath2 = "]/td[4]"

        numberDataList = [] # 숫자 데이터 넣음
        perDataList = []    # (현제 데이터 - 이전 데이터) / 이전 데이터 의 % 값을 넣음
        total = []  # 최종 결과값에 대한 리스트

        plus_shock = 0  # 변동율이 +2.5%를 넘어 갈 경우 카운트됨
        minus_shock = 0 # 변동율이 -2.5%를 넘어 갈 경우 카운트됨

        intagrate_Result = 0  # 적산값 출력


        # 신용잔고 수치 뽑아내기
        for i in range(4,14):
            if 4 <= i <= 8 or 12 <= i <= 13:
                xpath = xpath1 + str(i) + xpath2
                singleData = WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, xpath))).text

                # 계산을 위해서 ,(콤마) 제거
                singleData = singleData.replace(",", "")
                numberDataList.append(singleData) # 최근 데이터의 인덱스가 빠름(예: 인덱스 0번에는 현재 or 오늘 데이터 들어감)

        # 위에서 뽑아낸 데이터 계산하여 변동량으로 나타내기
        for i in range(0, 6):
            singleData = (int(numberDataList[i]) - int(numberDataList[i+1])) / int(numberDataList[i+1]) * 100
            singleData = round(singleData, 2)   # 소수점 2자리 까지 반올림

            intagrate_Result = singleData + intagrate_Result  # 적산 값 출력(%를 적산하여 계산했음)

            # 변동율이 +-2.5%를 넘어 갈 경우 카운트
            if singleData >= 2.5:
                plus_shock += 1
            elif singleData <= -2.5:
                minus_shock -= 1

            # 연산 결과가 +일 경우에는 +가 붙지 않기 때문에 붙여준다
            # 뒤에 연속일 계산에서는 String일 필요가 있기 때문에 str로 변환한다
            if singleData >= 0:
                singleData = "+" + str(singleData)
            else:
                singleData = str(singleData)

            perDataList.append(singleData)

        # 변동량 데이터를 xx일 연속 감소 같은 문자열 데이터로 나타내기
        stoper = 0
        plus = 0
        minus = 0
        plus_plus = 0
        minus_minus = 0

        for i in range(0, 6):
            singleData = perDataList[i]

            # 첫 수급의 플러스, 마이너스 확인하기
            if i == 0 and singleData[0] == "-":
                minus = 1
            elif i == 0 and singleData[0] == "+":
                plus = 1


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

        # 다른 요소와 연계하기 위해 반환값 주기
        if plus_shock >= 1 and minus_shock >= 1:
            total.append(0)
        elif plus_shock >= 1:
            total.append(plus_shock)
        elif minus_minus >= 1:
            total.append(minus_minus)
        else:
            total.append(0)

        if plus_plus >= 1:
            total.append("+" + str(plus_plus))

        elif minus_minus >= 1:
            total.append("-" + str(minus_minus))

        print("<신용잔고(6일간)> ", end="")
        print("6일간 누적%: ", end="")
        print(str(round(intagrate_Result, 2)), end="%, ")
        print("[+-2.5% 변동율, 연속 증가/감소]", end="")
        print(total, end="")
        print(driver.current_url)

        return total
    except:
        print("# 신용잔고 데이터 가져오기 통신에러")
        driver.quit()












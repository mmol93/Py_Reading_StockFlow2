from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import controlExcel

## 코스피 top10 종목에서 각 종목의 외국인 매매금액과 코스피 전체의 외국인 매매금액의 차이를 구하고
## 조건에 따른 메시지를 출력하게 한다(7일간)

def kospiTopTen():
    try:
        ## 코스피 Top10 종목코드
        # 혹시 top10에 순위 변경이 있으면 이 부분만 바꿔주면된다
        # 코스피의 경우 "삼성전자우"는 뺏음 => 그래서 결국 top9임 현재
        # 아래 종목 및 코드를 수정할 때는 종목명을 검색하여 관련 코드도 다 고친다
        # 예: sumsungElec를 고치고 싶다 -> "삼성전자" 검색 후 메시지 전부 고치기
        samsungElec = "005930"
        skHigh = "000660"
        lgChemi = "051910"
        samsungBio = "207940"
        celltrion = "068270"
        naver = "035420"
        samsungSDI = "006400"
        hyundai = "005380"
        kakao = "035720"
        hyundaiMobi = "012330"
        samsungCNT = "028260"
        KIA = "000270"
        POSCO = "005490"
        lgElect = "066570"
        skInnovation = "096770"
        koreaSOE = "009540"
        kbBank = "105560"
        CSwind = "112610"
        NCsoft = "036570"
        douzone = "012510"
        skTele = "017670"
        CJ = "097950"
        hotelShinra = "008770"
        SK = "034730"
        samsungSDS = "018260"
        samsungElectronics = "009150"
        apgroup = "002790"
        SKbio = "326030"


        stockList = []  # 위 종목 코드를 담는 리스트

        stockList.append(samsungElec)
        stockList.append(skHigh)
        stockList.append(lgChemi)
        stockList.append(samsungBio)
        stockList.append(celltrion)
        stockList.append(naver)
        stockList.append(samsungSDI)
        stockList.append(hyundai)
        stockList.append(kakao)
        stockList.append(hyundaiMobi)
        stockList.append(samsungCNT)
        stockList.append(KIA)
        stockList.append(POSCO)
        stockList.append(lgElect)
        stockList.append(skInnovation)
        stockList.append(koreaSOE)
        stockList.append(kbBank)
        stockList.append(CSwind)
        stockList.append(NCsoft)
        stockList.append(douzone)
        stockList.append(skTele)
        stockList.append(CJ)
        stockList.append(hotelShinra)
        stockList.append(SK)
        stockList.append(samsungSDS)
        stockList.append(samsungElectronics)
        stockList.append(apgroup)
        stockList.append(SKbio)


        # 주식의 이름을 담는 리스트
        stockNameList = []
        stockNameList.append("삼성전자")
        stockNameList.append("sk하이닉스")
        stockNameList.append("LG화학")
        stockNameList.append("삼성바이오")
        stockNameList.append("셀트리온")
        stockNameList.append("네이버")
        stockNameList.append("삼성SDI")
        stockNameList.append("현대차")
        stockNameList.append("카카오")
        stockNameList.append("현대모비스")
        stockNameList.append("삼성물산")
        stockNameList.append("기아차")
        stockNameList.append("포스코")
        stockNameList.append("LG전자")
        stockNameList.append("sk이노베이션")
        stockNameList.append("한국조선해양")
        stockNameList.append("KB금융")
        stockNameList.append("씨에스윈드")
        stockNameList.append("엔씨소프트")
        stockNameList.append("더존비즈온")
        stockNameList.append("SK텔레콤")
        stockNameList.append("CJ제일제당")
        stockNameList.append("호텔신라")
        stockNameList.append("SK")
        stockNameList.append("삼성SDS")
        stockNameList.append("삼성전기")
        stockNameList.append("아모레퍼시픽")
        stockNameList.append("SK바이오팜")

        kospiForeignBuying_List = []  # 코스피 외인 순매수/매도 데이터 리스트

        # Kospi 외인 크롤링 확인용 카운터
        # kospi의 크롤링은 한 번만 하면 되기 때문에 설정한다
        counter = 0

        ## 종목별 반복(위 코드 변수 갯수만큼 반복)
        for i in range(0, len(stockList)):

            options = webdriver.ChromeOptions()
            options.add_argument("headless")
            options.add_argument("disable-gpu")

            driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
            url1 = "https://finance.daum.net/quotes/A"
            url2 = stockList[i]
            url3 = "#influential_investors/home"
            url = url1 + url2 + url3    # 다음금융_외인/기관_탭

            driver.get(url)

            foreignBuyingAmountList = []    # 외인 순매수량 리스트(7일간)
            stockPriceList = [] # 해당 일 주식 종가 리스트(7일간)
            priceXamountList = []   # 종가 * 순매수/매도량 값의 리스트(7일간)


            ## 날짜별 반복
            # 해당 주식의 외인 순매수량, 해당 날의 종가 정보 가져오기(7일간 기록)
            for j in range(1, 8):

                ## 먼저 해당 주식의 순매수량 가져오기
                xpath1 = "//*[@id='boxContents']/div[4]/div[1]/div[3]/div[2]/div/table/tbody/tr["
                xpath2 = "]/td[4]"

                xpath = xpath1 + str(j) + xpath2

                foreignBuyingAmount = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath))).text

                # 계산을 위해 각 데이터에 있는 ,(콤마) 제거
                foreignBuyingAmount = foreignBuyingAmount.replace(",", "")

                # 제일 앞에 항상 +가 따라오기 때문에 이 +부호를 제거
                foreignBuyingAmount = foreignBuyingAmount.replace("+", "")

                if foreignBuyingAmount[0] == "-":
                    foreignBuyingAmount = foreignBuyingAmount[1:]

                # 계산을 위해 int형으로 변경후 리스트에 추가하기
                foreignBuyingAmountList.append(int(foreignBuyingAmount))


                ## 해당 주식의 해당 날의 종가 가져오기
                xpath2 = "]/td[6]"
                xpath = xpath1 + str(j) + xpath2

                stockPrice = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath))).text

                # 계산을 위해 각 데이터에 있는 ,(콤마) 제거
                stockPrice = stockPrice.replace(",", "")

                # 계산을 위해 int형으로 변경후 리스트에 추가하기
                stockPriceList.append(int(stockPrice))

                ## 해당 주식의 순매도(매수)량 * 종가 (단위는 억 이므로 // 100000000을 해준다)
                # 즉, 각 종목에 대한 외인들의 매매 금액이다
                priceXamountList.append((int(foreignBuyingAmount) * int(stockPrice)) // 100000000)



            # print("priceXamountList: ", end= "")    # (삭제) 확인용
            # print(priceXamountList)     # (삭제) 확인용


            ## 7일간의 코스피 외인 순매수/매도 데이터를 가져온다
            #(수정하기) - 코스피 일자별 매매 데이터 시작일과 각 종목의 외국인 매매 데이터 시작일은 다를 수 있음 어케함?
            dateValue_start = 1   # 위의 문제점을 해결하기 위해 넣은 변수
            dateValue_end = 8   # 위의 문제점을 해결하기 위해 넣은 변수
            # 시간을 확인하여 19시 이전에 프로그램을 시작했으면 start = 2 / end = 9
            # 19시 이후에 프로그램 시작했으면 dataValue = 1 / end = 8

            # 9~19시 사이에 실시했다면 start = 2 / end = 9
            if 9 <= datetime.datetime.now().hour < 19:
                dateValue_start = 2
                dateValue_end = 9

            # 주말은 항상 19시 이후로 생각한다
            if datetime.datetime.now().strftime("%a") == "Sat" or datetime.datetime.now().strftime("%a") == "Sun":
                dateValue_start = 1
                dateValue_end = 8

            ## 코스피에서 외인들의 매매금액을 가져온다(7일간)
            if counter == 0:
                counter += 1
                for k in range(dateValue_start, dateValue_end):
                    options = webdriver.ChromeOptions()
                    options.add_argument("headless")
                    options.add_argument("disable-gpu")

                    driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
                    url = "https://finance.daum.net/domestic/investors/KOSPI"  # 다음금융_코스피_탭

                    driver.get(url)

                    xpath1 = "//*[@id='boxDays']/div[2]/div/table/tbody/tr["
                    xpath2 = "]/td[3]"
                    xpath = xpath1 + str(k) + xpath2

                    kospiForeignBuying = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, xpath))).text

                    # 받은 데이터를 int화 시킨다
                    kospiForeignBuying = int(kospiForeignBuying.replace(",", ""))

                    kospiForeignBuying_List.append(kospiForeignBuying)

            # print("kospiForeignBuying_List: ", end="")  # (삭제) 확인용
            # print(kospiForeignBuying_List)  # (삭제) 확인용

            ## 일일 코스피 전체 외인 매매금액에 대한 top10 각 종목의 일일 매매금액의 비율을 구한다
            ## 조건에 따른 메시지를 출력한다
            # 아래의 z는 xx일 전 데이터를 의미한다
            for z in range(0, 7):
                # 각 종목의 일별 외인 매매금액(+,- 상관없음) / 코스피의 외인 매매금액 * 100 (반올림 2자리까지)
                per_result = round(priceXamountList[z] / kospiForeignBuying_List[z] * 100, 2)
                if z == 0:
                    # 종목별로 줄바꿈을 실시하기 위해 넣음
                    print("")
                # 위 결과가 3% 넘을 경우 메시지 표기
                if per_result >= 2.0:
                    # 3%를 넘긴하는데 코스닥 & 개별 종목 둘 다 순매도일 때 출력
                    if priceXamountList[z] <= 0 and kospiForeignBuying_List[z] <= 0:
                        print(stockNameList[i] + ": " + str(z + 1) + "일 전에 외인들이 코스피의 " + str(per_result) + "% 만큼 매도함 / ", end="")
                    # 개별 종목도 외인들 순매수 + 코스피도 외인 순매수일 때 출력
                    else:
                        print(stockNameList[i] + ": " + str(z + 1) + "일 전에 외인들이 코스피의 " + str(per_result) + "% 만큼 '매수'함 / ", end="")
                # 위 결과가 -3%를 넘을 경우 메시지 표기
                if per_result <= -2.0:
                    # 코스피는 외인 순매도이지만, 개별 종목의 순매수 금액이 지수 매도금액의 3%를 넘으면 "역매수"로 표기하게 한다
                    # 즉, 개별 종목은 순매수(+), 지수의 외인 매매는 순매도로 (-) 이며동시에 연산 결과가 -3% 이하인 애들
                    if priceXamountList[z] >= 0 and kospiForeignBuying_List[z] <= 0:
                        print(stockNameList[i] + ": " + str(z + 1) + "일 전에 외인들이 코스피의 " + str(per_result * -1) + "% 만큼 '역매수'함 / ", end="")
    except TimeoutException:
        driver.quit()
        print("")
        print("에러: 시간 초과됨")
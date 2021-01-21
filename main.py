import successiveForegin
import dollarIndex
import Future_foreignBuying
import CustomerDiposit
import CustomerCredit
import KospiTopTen
import KosdaqTopTen
import datetime
import time
import successiveCompany
import TenYearsBonds
import EWY

print("실시 날짜: " + str(datetime.datetime.now().strftime("%Y/%m/%d, %H:%M")))
# 1. 외국인 연속 수급 일수 가져오기(7일간) - C
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
successiveForeginKOSPI = successiveForegin.FivedayForeignKOSPI()    # 몇 일간 순매수 or 순매도 했는지 일 수 변수
print("------------------------")
successiveForeginKOSDAQ = successiveForegin.FivedayForeignKOSDAQ()  # 몇 일간 순매수 or 순매도 했는지 일 수 변수
print("------------------------")

# 2. 기관 연속 수급 일수 가져오기 ()7일간
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
successiveCompanyKOSPI = successiveCompany.FivedayCompanyKOSPI()    # 몇 일간 순매수 or 순매도 했는지 일 수 변수
print("------------------------")
successiveCompanyKOSDAQ = successiveCompany.FivedayCompanyKOSDAQ()  # # 몇 일간 순매수 or 순매도 했는지 일 수 변수
print("------------------------")

# 3. 외국인 선물 수급 일수 가져오기(7일간) - C
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
Future_foreignBuying = Future_foreignBuying.futureForeign() # 몇 일간 순매수 or 순매도 했는지 일 수 변수
print("------------------------")

# 4. 달러 인덱스 7일치 확인 - C
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
successiveDollar = dollarIndex.dollarIndex()  # 몇 일간 연속으로 올랐는지 or 내렸는지 일 수 변수
print("------------------------")

# 5. 고객 예탁금 확인 - C
# 반환값 = 리스트(변동율+,-2.5% 이상 카운터, "xx 일간 연속 매도 or 매수"에서 xx 값)
CustomerDiposit_val = CustomerDiposit.customerDiposit()
print("------------------------")

# 6. 신용 잔고 확인 - C
# 반환값 = 리스트(변동율+,-2.5% 이상 카운터, "xx 일간 연속 매도 or 매수"에서 xx 값)
CustomerCredit_val = CustomerCredit.customerCredit()
print("------------------------")

# 7. 매국 10년물 채권금리 - C
## 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
TenYearsBonds_val = TenYearsBonds.america()
print("------------------------")

# 8. 한국 지수 EWY - C
EWY.EWY_Graph()

## 1,2,3,4,5 번의 조합 결과
if successiveDollar[0] == "+" and int(successiveDollar[1]) >= 3 and \
        Future_foreignBuying[0] == "-" and int(Future_foreignBuying[1]) >= 2 and \
        successiveForeginKOSPI[0] == "-" and int(successiveForeginKOSPI[1]) >= 2 and CustomerDiposit_val[0] <= -1:
    print("달러 인덱스 3일 연속 상승 + 외국인 선물 2일 연속 매도 + 외국인 현물 2일 이상 매도  + 예탁금 2.5% 빠짐 1번 이상 => 코스피 하락장")
    print("------------------------")

if successiveDollar[0] == "-" and int(successiveDollar[1]) >= 3 and \
        Future_foreignBuying[0] == "+" and int(Future_foreignBuying[1]) >= 2 and \
        successiveForeginKOSPI[0] == "+" and int(successiveForeginKOSDAQ[1]) >= 2 and CustomerDiposit_val[0] >= 1:
    print("달러 인덱스 3일 연속 하락 + 외국인 선물 2일 연속 매수 + 외국인 현물 2일 이상 매수 + + 예탁금 2.5% 증가 1번 이상 => 코스닥 상승장")
    print("------------------------")

# 7. 코스피 외인 매매금액과 코스피 상위 top10 종목의 외인 매매금액 비교하기(7일간)
print("<코스피 외인 매매금액과 top10 외인 매매금액 비교>(3% 이상)", end="")
KospiTopTen.kospiTopTen()
print("")
print("------------------------")

time.sleep(3)

# 8. 코스닥 외인 매매금액과 코스닥 상위 top10 종목의 외인 매매금액 비교하기(7일간)
print("<코스닥 외인 매매금액과 top10 외인 매매금액 비교>(3% 이상)", end="")
KosdaqTopTen.kosdaqTopTen()
print("")
print("------------------------")


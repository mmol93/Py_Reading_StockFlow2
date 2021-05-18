import successiveForegin
import successiveForegin2
import dollarIndex
import KdollarIndex
import Future_foreignBuying
import CustomerDiposit
import CustomerCredit
import KospiTopTen
import KosdaqTopTen
import datetime
import time
import successiveCompany
import successiveCompany2
import TenYearsBonds
import EWY
import averageLine

print("실시 날짜: " + str(datetime.datetime.now().strftime("%Y/%m/%d, %H:%M")))
# TEST

# 1. 외국인 연속 수급 일수 가져오기(7일간) - C
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
# 반환값: 7일치 누적 매도/매수 금액
successiveForeginKOSPI = successiveForegin.FivedayForeignKOSPI()    # 몇 일간 순매수 or 순매도 했는지 일 수 변수
successiveForeginKOSDAQ = successiveForegin.FivedayForeignKOSDAQ()  # 몇 일간 순매수 or 순매도 했는지 일 수 변수
print("------------------------")

# 1-2. 외국인 연속 수급 일수 가져오기(20일간) - C
# # 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
# 반환값: 20일치 누적 매도/매수 금액
successiveForeginKOSPI2 = successiveForegin2.TwldayForeignKOSPI()
successiveForeginKOSDAQ2 = successiveForegin2.TwldayForeignKOSDAQ()
print("------------------------")

# 2. 기관 연속 수급 일수 가져오기 (7일간)
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
# 반환값: 7일치 누적 매도/매수 금액
successiveCompanyKOSPI = successiveCompany.FivedayCompanyKOSPI()    # 몇 일간 순매수 or 순매도 했는지 일 수 변수
successiveCompanyKOSDAQ = successiveCompany.FivedayCompanyKOSDAQ()  # # 몇 일간 순매수 or 순매도 했는지 일 수 변수
print("------------------------")

# 2-2. 기관 연속 수급 일수 가져오기 (20일간)
# 반환값: 20일치 누적 매도/매수 금액
successiveCompanyKOSPI2 = successiveCompany2.TwldayCompanyKOSPI()
successiveCompanyKOSPI2 = successiveCompany2.TwldayCompanyKOSDAQ()
print("------------------------")

# 3. 외국인 선물 수급 일수 가져오기(7일간) - C
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
Future_foreignBuying = Future_foreignBuying.futureForeign() # 몇 일간 순매수 or 순매도 했는지 일 수 변수
print("------------------------")

# 4. 달러 인덱스 7일치 확인 - C
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
successiveDollar = dollarIndex.dollarIndex()  # 몇 일간 연속으로 올랐는지 or 내렸는지 일 수 변수

# 4-2. 한국 달러 인덱스 10일치 확인 - C
# 반환값: 10일간의 누적 %
successiveKDollar = KdollarIndex.KdollarIndex()
print("------------------------")

# 5. 고객 예탁금 확인 - C
# 반환값: 10일치 누적 %
CustomerDiposit_val = CustomerDiposit.customerDiposit()
print("------------------------")

# 6. 신용 잔고 확인 - C
# 반환값 = 리스트(변동율+,-2.5% 이상 카운터, "xx 일간 연속 매도 or 매수"에서 xx 값)
CustomerCredit_val = CustomerCredit.customerCredit()
print("------------------------")

# 7. 매국 10년물 채권금리 - C
## 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
# 반환값: 14일치 누적 %
TenYearsBonds_val = TenYearsBonds.america()
print("------------------------")

# 8. 한국 지수 EWY - C
EWY.EWY_Graph()
print("------------------------")

# 9. 코스피 외인 매매금액과 코스피 상위 top10 종목의 외인 매매금액 비교하기(7일간)
print("<코스피 외인 매매금액과 top10 외인 매매금액 비교>(2% 이상)", end="")
KospiTopTen.kospiTopTen()
print("")
print("------------------------")

time.sleep(3)

# 10. 코스닥 외인 매매금액과 코스닥 상위 top10 종목의 외인 매매금액 비교하기(7일간)
print("<코스닥 외인 매매금액과 top10 외인 매매금액 비교>(2% 이상)", end="")
KosdaqTopTen.kosdaqTopTen()
print("")
print("------------------------")

# 코스피의 평균선 구하기
averageLine.index("https://finance.daum.net/domestic/kospi", "kospi")

# 코스닥의 평균선 구하기
averageLine.index("https://finance.daum.net/domestic/kosdaq", "kosdaq")
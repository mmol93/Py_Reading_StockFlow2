import successiveForegin
import dollarIndex
import Future_foreignBuying

# 1. 외국인 수급 7일치 가져오기 - C
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
successiveForeginKOSPI = successiveForegin.FivedayForeignKOSPI()    # 몇 일간 순매수 or 순매도 했는지 변수
print("------------------------")
successiveForeginKOSDAQ = successiveForegin.FivedayForeignKOSDAQ()  # 몇 일간 순매수 or 순매도 했는지 변수
print("------------------------")

# 2. 외국인 선물 수급 7일치 가져오기
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
Future_foreignBuying = Future_foreignBuying.futureForeign() # 몇 일간 순매수 or 순매도 했는지 변수
print("------------------------")

# 3. 달러 인덱스 7일치 확인 - C
# 표기형식 예시 : 3일 상숭 = +3, 3일 하락 = -3
successiveDollar = dollarIndex.dollarIndex()  # 몇 일간 연속으로 올랐는지 or 내렸는지 변수
print("------------------------")

## 1,2,3 번의 조합 결과
# 달러 인덱스가 3일 이상 상승 &
if successiveDollar[0] == "+" and int(successiveDollar[1]) >= 3 and \
        Future_foreignBuying[0] == "-" and int(Future_foreignBuying[1]) >= 2 and \
        successiveForeginKOSPI[0] == "-" and int(successiveForeginKOSPI[1]) >= 2:
    print("달러 인덱스 상승 + 외국인 선물 2일 연속 매도 + 외국인 현물 2일 이상 매도 => 코스피 하락장")

if successiveDollar[0] == "+" and int(successiveDollar[1]) >= 3 and \
        Future_foreignBuying[0] == "-" and int(Future_foreignBuying[1]) >= 2 and \
        successiveForeginKOSPI[0] == "-" and int(successiveForeginKOSDAQ[1]) >= 2:
    print("달러 인덱스 상승 + 외국인 선물 2일 연속 매도 + 외국인 현물 2일 이상 매도 => 코스닥 하락장")

if successiveDollar[0] == "-" and int(successiveDollar[1]) >= 3 and \
        Future_foreignBuying[0] == "+" and int(Future_foreignBuying[1]) >= 2 and \
        successiveForeginKOSPI[0] == "+" and int(successiveForeginKOSPI[1]) >= 2:
    print("달러 인덱스 하락 + 외국인 선물 2일 연속 매수 + 외국인 현물 2일 이상 매수 => 코스피 상승장")

if successiveDollar[0] == "-" and int(successiveDollar[1]) >= 3 and \
        Future_foreignBuying[0] == "+" and int(Future_foreignBuying[1]) >= 2 and \
        successiveForeginKOSPI[0] == "+" and int(successiveForeginKOSDAQ[1]) >= 2:
    print("달러 인덱스 하락 + 외국인 선물 2일 연속 매수 + 외국인 현물 2일 이상 매수 => 코스닥 상승장")
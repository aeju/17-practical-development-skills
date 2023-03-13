# 타임 스탬프 : 컴퓨터가 시간을 표현하기 위해 사용하는 값 (1970.01.01 00:00:00 ~)
# 타임 스탬프 값 알려주는 사이트 : https://www.epochconverter.com/
# 타임 스탬프 : 단조시간(컴퓨터가 직접 계산하는 시간), 실제 시간

# 1초 미만의 시간 측정
import time

print("현재 시간(Unix epoch time): {0}".format(time.time()))
# 실제 시간(real time) = 벽 시계 시간(wall clock time) : 실제 세계의 시간과 항상 일치
# 한 달이 넘는 주기로 수행하는 작업(매달 1일), 특정 날짜에 반드시 실행해야 하는 작업등의 기준 시간으로 사용
# (단조 시간으로도 한 달을 잴 수 있지만, 30/31일/윤년도 염두에 두고 계산해야하므로, 한 달 이상 주기는 실제 시간 기준 사용하는 것이 좋음)

# 단조 시간처럼 시간 차이를 구하거나 일정한 간격을 측정하기 위해서 사용x

# 주기적으로 실제 시간을 축정한 후 정해진 시간이 됐을 때 루프를 종료
import datetime
import time

# t1 시간 기록 (특정 날짜)
t1 = datetime.datetime(
    year=2019, month=4, day=27, hour=13, minute=20, second=00
)

# 1초마다 시스템에서 제공하는 실제 시간을 가져온 다음 특정 날짜를 가리키는 t1과 비교
# 만약 현재 날짜가 t1을 지났다면 루프를 종료, 그렇지 않으면 같은 작업을 반복
while True:
    now = datetime.datetime.now()
    print("현재 시간: {0}".format(now))
    print("루프 만료 시간: {0}".format(t1))
    if t1 <= now:
        break

    time.sleep(1)
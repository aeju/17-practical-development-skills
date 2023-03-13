# 단조 시간(monotonic time) : 운영체제 or 하드웨어(CPU)에서 직접 계산하는 시간
# 실제 세계 시간과는 다르지만, 운영체제가 시작한 이후 시점부터 바뀌지 않는 특징
# 사용자가 직접 값 변경 가능
# 시스템 재부팅 이후, 값 초기화 -> 재부팅 전보다 현저히 낮은 값으로 바뀜

import time

# t1 시간 기록 (현재)
t1 = time.monotonic()

while True:
    # t2 시간 기록
    t2 = time.monotonic()
    # 이 루프가 3초 이상 실행된 경우 종료.
    if t2 >= t1 + 3:
        break

# 실제 시간 차이를 출력. 
print("t1={0}".format(t1))
print("t2={0}".format(t2))
print("diff={0}".format(t2-t1))

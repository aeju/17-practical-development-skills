# 실제 시간 사용할 때, 타임 존 설정을 꼭 확인해야 함 (여러 국가를 대상으로 하는 서비스 -> 두 서버 간 시간차이로 오작동 발생)
# 나라마다 사용하는 표준 시간이 다르기 때문 (한국 : UTC+9시간 기준)

import datetime

# 시스템 기본 시간
t1 = datetime.datetime.now()
# UTC 시간
t2 = datetime.datetime.now(tz=datetime.timezone.utc)

print("시스템 기본 시간: {0}".format(t1))
print("UTC 시간: {0}".format(t2))

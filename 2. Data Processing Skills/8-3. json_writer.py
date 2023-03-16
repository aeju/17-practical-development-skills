# JSON 파일 만들기

import json

# 유니코드 문자열을 명시하기 위해 u를 붙임.
message2 = {
    u'number': 12345,
    u'pi': 3.14,
    u'str': u'문자열 값',
    u'null_key': None,
    u'object': {
        u'str2': u'문자열 값 2',
        u'object2': {
            u'number2': 12345
        }
    },
    u'num_array': [1, 2, 3, 4, 5],
    u'str_array': [u'one', u'two', u'three', u'four', u'five']
}

# ensure_ascii=True 인 경우에는 아스키 코드가 아닌 모든 문자열을 \uXXXX 로 표기.
with open('message2.json', 'w', encoding='UTF8') as file:
    json.dump(message2, file, ensure_ascii=False)
    # 들여쓰기 추가 : 각 키마다 개행 문자(\n)가 자동으로 추가, 다른 프로그래밍 언어 = pretty
    json.dump(message2, file, ensure_ascii=False, indent=2)
    # 키 정렬까지 필요한 경우
    # json.dump(message2, file, ensure_ascii=False, indent=2, sort_keys=True)

# JSON 메시지를 만들 때 주의할 점
# 실무에서는 null을 사용하지 않는 게 좋음 (그 키가 어떤 형태의 데이터를 담고 있는지 알 수 없기 때문)
# -> 숫자 : "빈 키":0, 문자열: "빈 키": "", 객체: "빈 키": {}, 배열: "빈 키": []

# JSON 키 이름 형식 : 표준, 관례 x -> 하나의 규칙 정하고 통일해 사용하기
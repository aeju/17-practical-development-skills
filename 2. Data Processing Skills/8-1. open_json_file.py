"""
JSON(JavaScript Object Notation) :숫자, 문자, 참 또는 거짓 등 여러 형태의 데이터를 키(key)와 값(value)으로 구조화된 객체(object)에 담아 처리하는 규격
-> 텍스트 기반이기 때문에 사람이 쉽게 저장된 데이터를 읽고 수정할 수 있음 + 디버깅 편리
=> 생산성 높아짐 (서버-클라이언트 간 메시지 표준 규격 중 하나로 사용 중)

- 특징1) UTF-8 인코딩만 허용
- 특징2) 주석 지원 x (cf. XML, YAML : 주석 지원하는 메시지 규격)

ex. "number": 1234
- key : "문자열" / value: 콜론 뒤, JSON 객체/배열도 값으로 사용 가능 <- 8-1.json 두 번째 중괄호 데이터 "object"

- 문자 이스케이프 : 문자열 안에 "" 넣고 싶으면 -> \" (cf. \t:탭추가, \n:개행)
"""

# message1.json 읽는 코드
import json

def open_json_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return json.load(file)
        except ValueError as e:
            print('JSON 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


# message1.json 파일은 같은 디렉터리에 있어야 함.
json_data = open_json_file('8-1. message1.json')
if json_data:
    print(json_data)
# JSON 객체로부터 키와 값 읽기

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
if not json_data:
    # print(json_data)
    # 더 이상 로직을 진행할 수 없으므로 종료합니다.
    exit(0)

print(json_data)
# json_data : {'number': 12345, 'pi': 3.14, 'str': '문자열 값', 'null_key': None, 'object': {'str2': '문자열 값2', 'object2': {'number2': 12345}}, 'num_array': [1, 2, 3, 4, 5], 'str_array': ['one', 'two', 'three', 'four', 'five']}

# 정수
num_value = json_data['number']
# 실수
float_value = json_data['pi']
# 문자열
str_value = json_data['str']
# 빈 키(None)
empty_value = json_data['null_key']

print('num_value={0}'.format(num_value))
print('float_value={0}'.format(float_value))
print('str_value={0}'.format(str_value))
print('empty_value={0}'.format(empty_value))

# 객체 안 객체 접근
json_data2 = json_data['object']
print('json_data[\'object\'][\'str2\']={0}'.format(json_data2['str2']))

# 배열 접근
json_array = json_data['num_array']
for n in json_array:
    print('n={0}'.format(n))

# 'unknown_key'를 읽는 잘못된 방법
""" 
unknown_value = json_data['unknown_key']
print('unknown_value={0}'.format(unknown_value))
"""
# 오류 : 예외발생
# 해결책<2> : try-catch 구문으로 제어, 사용하는 모든 키가 존재하는지 검사

# 'unknown_key'를 읽는 올바른 방법 1
try:
    unknown_value = json_data['unknown_key']
    print('unknown_value={0}'.format(unknown_value))
except KeyError:
    print('\'unknwon_key\'는 존재하지 않습니다')

# 'unknown_key'를 읽는 올바른 방법 2
if 'unknwon_key' in json_data:
    unknown_value = json_data['unknown_key']
    print('unknown_value={0}'.format(unknown_value))
else:
    print('\'unknown_key\'는 존재하지 않습니다')

# 키 검사할 때, 키 존재 여부 + 키에 대응하는 값 올바른 형태인지 함께 검사
# -> assert 사용하여 JSON 메시지가 올바른 형태인지, 필요한 키가 모두 있는지 검사
# assert : 디버깅 환경에서만 동작

# float_value가 3 이상 3.2 미만인지 검사하는 코드
assert(3 <= float_value < 3.2)
# str_value 가 null이 아니고 문자열 길이가 0 이상인지 검사하는 코드
assert(str_value and len(str_value) > 0)
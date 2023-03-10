# 아스키 코드 : 처음으로 표준을 정립한 문자열 인코딩 방식
# ASCII : American Standard Code for Information Interchange

# 다음 코드를 실행하기 위해서 별도 모듈 필요 x

def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{0}".format(int(c)) for c in byte_data)

    print('\'' + text + '\' 문자열 길이: {0}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는 데 사용한 바이트 수: {0}'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))

print_text('Hello', 'ascii')
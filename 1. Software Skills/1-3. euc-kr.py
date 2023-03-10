# EUC-KR(CP949)
# 우리나라, 컴퓨터로 한글 표현하는 방법 -> EUC-KR 문자 집합(문자 하나 = 2바이트, 아스키 코드 -> 1바이트, 호환o)
# 모든 글자가 완성된 형태로만 존재하는 '완성형' 코드 (-> 표현할 수 없는 한글 일부 존재)
# 유니코드 2.0 : 초성, 중성, 종성 해당하는 코드 나눠 표현 (조합현 글자)


def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{0}".format(int(c)) for c in byte_data)

    print('\'' + text + '\' 문자열 길이: {0}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))


print_text('Hello', 'euc-kr')
print_text('안녕하세요', 'euc-kr')

# 문자열 인코딩 : 실제 문자열 길이와 컴퓨터가 할당하는 버퍼 크기는 항상 다를 수 있다
# (실제 문자열 길이 : 사람 눈에 보이는 문자 길이, 버퍼 길이 : 컴퓨터가 문자를 표현하는 데 사용한 바이트 수)
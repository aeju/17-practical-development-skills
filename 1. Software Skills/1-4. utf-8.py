# 과거 : 국가별로 독자적인 문자열 인코딩 방식 사용 (ex. EUC-KR)
# -> 전 세계 사용자를 대상으로 하는 프로그램 개발 : 언어별로 다른 인코딩 방식 사용 (골치 아픔)

# 문제 해결 : ISO, 유니코드 문자 집합(동일한 규칙으로 모든 언어 표현 가능)
# 최초 버전 1.0 : 1991년 제정, 현재 12.1버전 / 앞으로 계속 개정될 것
# 유니코드 문자집합 표현 문자열 인코딩 <3> : UTF-8, UTF-16, UTF-32

# UTF-8 : 8비트(1바이트)로 인코딩한다
# 아스키코드와 완벽하게 호환o, 표현하려는 문자에 따라 1바이트~16바이트
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{0}".format(int(c)) for c in byte_data)

    print('\''+ text + '\' 문자열 길이: {0}'.format(len(text)))
    print('\''+ text + '\' 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))


print_text('Hello', 'utf-8')
print_text('안녕하세요', 'utf-8')
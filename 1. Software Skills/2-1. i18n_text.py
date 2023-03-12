# 2. 다국어 처리
# i18n : 다국어를 지원하기 위해 만든 표준, 국제화(internationalization) 첫 문자(i)와 마지막 문자(n) 사이에 문자 18개가 있다는 의미
# -> 프로그램이 출력할 문장을 코드로부터 분리, 코드 수정, 재컴파일 없이 시스템/브라우저 설정에 따라 적절한 언어 출력 가능
# 프로그램 코드는 출력할 문장의 식별자만 지정하면 되고, 실제 문장은 별도 파일에서 관리 가능
# -> 더 이상 사용하지 않는 문장이나 누락된 문장들 자동으로 감지

# -*- coding: utf-8 -*-
# 다음 코드를 실행하기 위해서는 python-gettext 모듈 필요
# 초기화 과정
#import gettext
#translation_ko = gettext.translation(
#    domain='i18n_test', localedir='./locale', languages=['ko_KR'])


#translation_ko.install()

#print(_('Test message 1'))
#print('Test message 2')
#print(_('Test message 3'))

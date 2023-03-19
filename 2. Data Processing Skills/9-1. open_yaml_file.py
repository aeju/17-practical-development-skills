# 다음 코드를 실행하기 위해서는 pyyaml 모듈이 필요.
import yaml

def open_yaml_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return yaml.load(file, Loader=yaml.SafeLoader)
        except yaml.parser.ParserError as e:
            print('YAML 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None

# message1.yaml 파일은 같은 디렉터리에 있어야 함.
yaml_data = open_yaml_file('9-0. message1.yml')
if yaml_data:
    print(yaml_data)
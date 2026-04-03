#이름과 나아를 입력하면 다음과 같이 개월 수로 바꾸어 출력하는 프로그램을 작성하시오.

user_name = 0
user_age = 0

user_name = str(input('이름을 입력하세요 : '))
user_age = int(input('나이 입력 : '))
print('%s님이 태어난지 %d개월 되었습니다.' %user_name, (user_age*12))
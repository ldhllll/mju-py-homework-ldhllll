# 파일이름 : 나만의 정기 구독 비용 관리 시스템
# 작 성 자 : 이다현
#1. 월 사용 가능 금액 입력
form_one_budget= int(input("플랫폼 하나당 월 사용 가능 금액을 입력하세요: "))

#2. 구독 서비스 이름 입력_
platform1 = input("첫 번째 구독 서비스 이름을 입력하세요: ")
platform2 = input("두 번째 구독 서비스 이름을 입력하세요: ")
platform3 = input("세 번째 구독 서비스 이름을 입력하세요: ")

#3. 각 서비스의 월 비용 입력
price1 = int(input(f'{platform1}의 월 구독 비용을 입력하세요: '))
price2 = int(input(f'{platform2}의 월 구독 비용을 입력하세요: '))
price3 = int(input(f'{platform3}의 월 구독 비용을 입력하세요: '))

#4. 총 월 구독 비용, 플랫폼 월 사용 가능 금액 계산
total_cost = price1 + price2 + price3
avilable_cost = form_one_budget*3

#5. 결과 출력
print("[구독 서비스 이용 내역]")
print(f'{platform1}: {price1}원')
print(f'{platform2}: {price2}원')
print(f'{platform3}: {price3}원')

print(f'총 월 구독 비용: {total_cost}원')
print(f'월 사용 가능 금액: {available_cost}원')

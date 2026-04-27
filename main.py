# 파일이름 : 나만의 정기 구독 비용 관리 시스템
# 작 성 자 : 이다현
#1. 사용자 정보 입력
user = input("사용자 이름을 입력하세요:")
month_bud = int(input(f'{user}의 이번 달 사용 가능 금액을 입력하세요: '))

#2. 리스트 생성
platforms = []
prices = []
categories = []

#3. 구독 서비스 정보 입력
service_count = 3
total_cost = 0
for i in range(service_count):
  print() #줄띄우기
  platform = input(f'{i+1}번째 구독 서비스 이름을 입력하세요:')
  price = int(input(f'{platform}의 월 구독 비용을 입력하세요:'))
  category = input(f'{platform}의 종류를 입력하세요(예: OTT, 공부, GPT..<숫자입력불가>):')

  platforms.append(platform)
  prices.append(price)
  categories.append(category)

  total_cost += price

#4. 리스트 수정(후 3차 과제 반복문 때 더 심화할 예정)
check1 = input(f'혹시 구독 플랫폼 이름이나 월 구독 비용, 구독 서비스 종류를 잘못 입력하셨습니까?(Y/N):')
if check1 == 'Y':
  name =  input(f'확인하였습니다. 관련 구독 서비스 이름이 뭐였습니까?:')
  idx = platforms.index(name)
  if idx >= 0:
    check2 = input(f'구독 서비스 이름을 확인하였습니다. {name} 이름을 바꿀까요?(Y/N):')
      if check2 == 'Y':
        new_name = input(f'바꿀 이름을 입력하세요:')
        platforms.insert(idx, new_name)
        platforms.remove(name)
      if check2 == 'N' or check2 == 'Y':
        check3 = input(f'관련 구독 서비스의 월 구독 비용을 바꿀까요?(Y/N):')
        if check3 == 'Y':
          new_price = int(input(f'바꿀 구독 비용을 입력하세요:'))
          prices.insert(idx, new_price)
          prices.pop(idx)
        if check3 == 'Y' or check3 == 'N':
          check4 = input(f'관련 구독 서비스의 종류를 바꿀까요?(Y/N):')
          if check4 == 'Y':
            new_category = input(f'바꿀 구독 서비스의 종류를 입력하시오:')
            categories.insert(idx, new_category)
            categories.pop(idx)
          else:
            print(f'더 이상 바꿀 게 없습니다.')
        else:
            print(f'Y와 N중 하나만 입력하세요.')
      else:
        print(f'Y와 N중 하나만 입력하세요.')
  else:
    print(f'관련 구독 서비스 이름을 다시 입력하세요.:')
else:
  print(f'입력 수정 없음.')

#4. 결과 출력
print() #줄띄우기
print('='*20)
print(f'[{user}님의 정기 구독 이용 내역]')
print('='*20)
print(f'총 월 구독 비용:{total_cost:.0f}원')
print(f'가장 비싼 구독 비용:{max(prices)}원')
print(f'이번달 사용 가능 금액:{month_bud}원')

#5. 비교 및 판단
print('='*20)
print(f'[예산 확인 결과]')

if total_cost > month_bud:
  print(f'사용 가능 금액을 초과했습니다. 줄여야 합니다.')
elif total_cost == month_bud:
  print(f'사용 가능 금액과 정확히 같습니다.')
else:
  print(f'굿! 사용 가능 금액을 초과하지 않습니다.')
if max(prices) > month_bud /2:
  print(f'가장 비싼 구독 서비스의 비용이 예산에 비해 큰 편입니다.')
print('='*20)
#6. 계산 확인
if month_bud > 0 and total_cost > 0:
  print(f'시스템 종료.')
  star = float(input(f'시스템 만족도를 입력해주세요(10점 만점):'))
else:
  print(f'계산이 잘못되었습니다. 다시 한번 입력해주세요.')






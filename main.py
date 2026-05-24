# 파일이름 : 나만의 정기 구독 비용 관리 시스템
# 작 성 자 : 이다현

# 리스트 생성과 정의
platforms = []
prices = []
categories = []

month_bud = 0
total_cost = 0

# 유저 정보 확인
user = input("사용자 이름을 입력하세요:")

# 메뉴 출력 함수
while True:
  print() # 줄띄우기
  print("=" * 35)
  print("나만의 정기 구독 비용 관리 시스템")
  print('=' * 35)
  print("1. 월 사용 가능 금액 입력")
  print("2. 정기 구독 서비스 추가")
  print("3. 특정 구독 서비스 수정")
  print("4. 총 월 구독 비용 계산")
  print("5. 전체 구독 서비스 조회")
  print("6. 예산 초과 여부 확인")
  print("7. 종료")
  print("=" * 35)
  check= int(input('{user}가 원하는 메뉴를 입력하세요(숫자입력): '))
  if check == 7:
    break
#<함수 정의>
#1. 월 사용 가능 금액 입력 함수
def input_budget():
    global month_bud
    month_bud = int(input("플랫폼 하나당 월 사용 가능 금액을 입력하세요: "))
    print("월 사용 가능 금액이 입력되었습니다.")

#2. 정기 구독 서비스 추가 함수
def add_service(platforms, prices, categories):
      platform = input("구독 플랫폼 이름을 입력하세요: ")
      price = int(input(f"{platform}의 월 구독 비용을 입력하세요: "))
      category = input(f"{platform}의 종류를 입력하세요(예: OTT, 공부, GPT): ")
      platforms.append(platform)
      prices.append(price)
      categories.append(category)
      print("구독 서비스가 추가되었습니다.")
  
#3. 특정 구독 서비스 수정 함수
def update_service(platforms, prices, categories):
      if len(platforms) == 0:
        print("수정할 구독 서비스가 없습니다.")
        return
        
      else:
        modify = int(input('구독 플랫폼 이름을 수정하고 싶으시면 1, 구독 서비스 종류는 2, 월 구독 비용 수정은 3을 눌러주세요: '))
        if modify == 1:
           name = input("확인하였습니다. 관련 구독 서비스 이름이 무엇입니까?: ")
           if name in platforms:
            idx = platforms.index(name)
            print()
            print("[현재 구독 서비스 정보]")
            print("이름:", platforms[idx])
            new_name = input('이름을 어떻게 바꿀까요?: ')
            platforms.insert(idx, new_name)
            platforms.remove(name)
            print('이름을 바꿨습니다.')
            return
             
           else:
             print(f'{name}이 존재하지 않습니다.')
             return
             
        if modify == 2:
           name = input("확인하였습니다. 관련 구독 서비스 이름이 무엇입니까?: ")
           idx = platforms.index(name)
           print()
           print("[현재 구독 서비스 정보]")
           print(f'구독 서비스 종류: {categories[idx]}')
           new_category = input('종류를 어떻게 바꿀까요?: ')
           categories.remove(categories[idx])
           categories.insert(idx, new_category)
           print('종류를 바꿨습니다.')
           return
          
        if modify == 3:
           name = input("확인하였습니다. 관련 구독 서비스 이름이 무엇입니까?: ")
           idx = platforms.index(name)
           print()
           print("[현재 구독 서비스 정보]")
           print(f'구독 서비스 월 가격: {prices[idx]}')
           new_price = int(input('월 구독 가격을 어떻게 바꿀까요?: '))
           prices.remove(prices[idx])
           prices.insert(idx, new_price)
           print('가격을 바꿨습니다.')
           return
          

#4. 총 월 구독 비용 계산 함수
def total_month(prices):
  total_month = sum(prices)
  print(f'총 월 구독 비용은 {total_month}입니다.')

#5. 전체 구독 서비스 조회 함수
def update_service(platforms, prices, categories):
#6. 예산 초과 여부 확인 함수



# 월 사용 가능 금액 입력 실행
  if check == 1:
    input_budget()
    
# 정기 구독 서비스 추가 함수 실행
  if check == 2:
    add_service(platforms, prices, categories):
    
# 특정 구독 서비스 수정 함수 실행
  if check == 3:
    update_service(platforms, prices, categories):
      

  if name in platform_list:
    idx = platform_list.index(name)
    print()
    print("[현재 구독 서비스 정보]")
    print("이름:", platform_list[idx])
    print("월 구독 비용:", price_list[idx], "원")
    print("종류:", category_list[idx])

check2 = input(f"구독 서비스 이름을 확인하였습니다. {name} 이름을 바꿀까요?(Y/N): ")

    if check2 == "Y":
      new_name = input("바꿀 이름을 입력하세요: ")
      platform_list[idx] = new_name
      print("구독 서비스 이름이 수정되었습니다.")

    elif check2 == "N":
      print("구독 서비스 이름은 수정하지 않습니다.")

    else:
      print("Y와 N 중 하나만 입력하세요.")

      check3 = input("관련 구독 서비스의 월 구독 비용을 바꿀까요?(Y/N): ")

            if check3 == "Y":
                new_price = int(input("바꿀 구독 비용을 입력하세요: "))
                price_list[idx] = new_price
                print("월 구독 비용이 수정되었습니다.")

            elif check3 == "N":
                print("월 구독 비용은 수정하지 않습니다.")

            else:
                print("Y와 N 중 하나만 입력하세요.")

            check4 = input("관련 구독 서비스의 종류를 바꿀까요?(Y/N): ")

            if check4 == "Y":
                new_category = input("바꿀 구독 서비스의 종류를 입력하세요: ")
                category_list[idx] = new_category
                print("구독 서비스 종류가 수정되었습니다.")

            elif check4 == "N":
                print("구독 서비스 종류는 수정하지 않습니다.")

            else:
                print("Y와 N 중 하나만 입력하세요.")

        else:
            print("관련 구독 서비스 이름을 다시 입력하세요.")

    elif check1 == "N":
        print("입력 수정 없음.")

    else:
        print("Y와 N 중 하나만 입력하세요.")


# 구독 서비스 정보 입력
service_count = 3
total_cost = 0
for i in range(service_count):
  print() #줄띄우기
  platform = input(f'{i+1}번째 구독 서비스 이름을 입력하세요(입력 중단하려면 종료를 입력):')
  if platform == '종료'
    print(f'구독 서비스 입력을 중단합니다.')
    break

  price = int(input(f'{platform}의 월 구독 비용을 입력하세요:'))
  category = input(f'{platform}의 종류를 입력하세요(예: OTT, 공부, GPT..<숫자입력불가>):')

  platforms.append(platform)
  prices.append(price)
  categories.append(category)

  total_cost += price

#4. 리스트 수정(후 3차 과제 때 더 심화할 예정)
check1 = input(f'혹시 구독 플랫폼 이름이나 월 구독 비용, 구독 서비스 종류를 잘못 입력하셨습니까?(Y/N):')
if check1 == 'Y':
  name =  input(f'확인하였습니다. 관련 구독 서비스 이름이 뭐였습니까?:')
  if platforms.index(name) >= 0:
    idx= platforms.index(name)
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






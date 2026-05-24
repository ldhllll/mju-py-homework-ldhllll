# 파일이름 : 나만의 정기 구독 비용 관리 시스템
# 작 성 자 : 이다현

# 리스트 생성과 정의
platforms = []
prices = []
categories = []

sum(prices)= 0
month_bud = 0
total_cost = 0

# 유저 정보 확인
user = input("사용자 이름을 입력하세요:")


# 1. 월 사용 가능 금액 입력 함수
def input_budget():
    global month_bud

    month_bud = int(input("플랫폼 하나당 월 사용 가능 금액을 입력하세요: "))
    print("월 사용 가능 금액이 입력되었습니다.")


# 2. 정기 구독 서비스 추가 함수
def add_service(platforms, prices, categories):
    platform = input("구독 플랫폼 이름을 입력하세요: ")
    price = int(input(f"{platform}의 월 구독 비용을 입력하세요: "))
    category = input(f"{platform}의 종류를 입력하세요(예: OTT, 공부, GPT): ")

    platforms.append(platform)
    prices.append(price)
    categories.append(category)

    print("구독 서비스가 추가되었습니다.")


# 3. 특정 구독 서비스 수정 함수
def update_service(platforms, prices, categories):
    if len(platforms) == 0:
        print("수정할 구독 서비스가 없습니다.")
        return

    modify = int(input("구독 플랫폼 이름 수정은 1, 구독 서비스 종류 수정은 2, 월 구독 비용 수정은 3을 눌러주세요: "))

    if modify == 1:
        name = input("수정할 구독 서비스 이름을 입력하세요: ")

        if name in platforms:
            idx = platforms.index(name)

            print()
            print("[현재 구독 서비스 정보]")
            print("이름:", platforms[idx])

            new_name = input("이름을 어떻게 바꿀까요?: ")
            platforms[idx] = new_name

            print("이름을 바꿨습니다.")
        else:
            print(f"{name}이 존재하지 않습니다.")

    elif modify == 2:
        name = input("수정할 구독 서비스 이름을 입력하세요: ")

        if name in platforms:
            idx = platforms.index(name)

            print()
            print("[현재 구독 서비스 정보]")
            print(f"구독 서비스 종류: {categories[idx]}")

            new_category = input("종류를 어떻게 바꿀까요?: ")
            categories[idx] = new_category

            print("종류를 바꿨습니다.")
        else:
            print(f"{name}이 존재하지 않습니다.")

    elif modify == 3:
        name = input("수정할 구독 서비스 이름을 입력하세요: ")

        if name in platforms:
            idx = platforms.index(name)

            print()
            print("[현재 구독 서비스 정보]")
            print(f"구독 서비스 월 가격: {prices[idx]}원")

            new_price = int(input("월 구독 가격을 어떻게 바꿀까요?: "))
            prices[idx] = new_price

            print("가격을 바꿨습니다.")
        else:
            print(f"{name}이 존재하지 않습니다.")

    else:
        print("잘못된 수정 메뉴입니다.")


# 4. 총 월 구독 비용 계산 함수
def total_month(prices):
    if sum(prices) == 0:
        print("등록된 구독 서비스가 없습니다.")
        return 0
    else:
        total_cost = sum(prices)
        max_price = max(prices)
        min_price = min(prices)
      
        print()
        print("[총 월 구독 비용 계산 결과]")
        print(f"총 월 구독 비용: {total_cost}원")
        print(f"가장 비싼 구독 비용: {max_price}원")
        print(f"가장 저렴한 구독 비용: {min_price}원")

        return total_cost


# 5. 전체 구독 서비스 조회 함수
def all_service(platforms, prices, categories):
    if len(platforms) == 0:
        print("현재 등록된 구독 서비스가 없습니다.")
        return
    else:
        print()
        print("[현재 구독 서비스 정보]")
        for i in range(len(platforms)):
            print(f"{i + 1}. 이름: {platforms[i]} / 월 구독 비용: {prices[i]}원 / 종류: {categories[i]}")


# 6. 예산 초과 여부 확인 함수
def bud_check(month_bud, prices):
    if month_bud == 0:
        print("월 사용 가능 금액부터 입력하세요.")
        return

    elif len(prices) == 0:
        print("등록된 구독 서비스가 없습니다.")
        return
    else:
        total = sum(prices)
        print()
        print("[예산 확인 결과]")
        print(f"월 사용 가능 금액: {month_bud}원")
        print(f"총 월 구독 비용: {total}원")

        if month_bud > total:
            print("월 구독 비용 예산은 초과되지 않았습니다.")
        elif month_bud == total:
            print("월 구독 비용 예산과 동일합니다. 더 이상 구독 플랫폼을 추가하면 초과합니다.")
        else:
            print("월 구독 비용을 초과하였습니다. 구독 플랫폼을 줄이세요.")


# 메뉴 출력 및 실행
while True:
    print()
    print("=" * 35)
    print("나만의 정기 구독 비용 관리 시스템")
    print("=" * 35)
    print("1. 월 사용 가능 금액 입력")
    print("2. 정기 구독 서비스 추가")
    print("3. 특정 구독 서비스 수정")
    print("4. 총 월 구독 비용 계산")
    print("5. 전체 구독 서비스 조회")
    print("6. 예산 초과 여부 확인")
    print("7. 종료")
    print("=" * 35)

    check = int(input(f"{user}가 원하는 메뉴를 입력하세요(숫자입력): "))

    if check == 1:
        input_budget()

    elif check == 2:
        add_service(platforms, prices, categories)

    elif check == 3:
        update_service(platforms, prices, categories)
    elif check == 4:
        total_cost = total_month(prices)
        print(f'총 월 구독 비용은 {total_cost}입니다.')
        print(f'최고 구독 가격은 {max(prices)}입니다.')
        print(f'최소 구독 가격은 {min(prices)}입니다.')
    elif check == 5:
        all_service(platforms, prices, categories)

    elif check == 6:
        bud_check(month_bud, prices)
    elif check == 7:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴입니다. 다시 입력하세요.")


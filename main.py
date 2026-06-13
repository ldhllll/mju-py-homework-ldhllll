# 파일이름 : 나만의 정기 구독 비용 관리 시스템
# 작 성 자 : 이다현
 
# 리스트 생성
data = []  # 이중 리스트 생성: 모든 구독 정보를 하나의 리스트에 저장
 
month_bud = 0   # 플랫폼 하나당 월 사용 가능 금액 (전역변수)
total_cost = 0  # 총 월 구독 비용 (전역변수)
 
# 유저 이름 입력
user = input("사용자 이름을 입력하세요: ")
 
 
# 1. 월 사용 가능 금액 입력 함수
def input_budget():
    global month_bud
 
    # [예외 처리] 숫자가 아닌 문자를 입력했을 때 ValueError 처리
    try:
        month_bud = int(input("플랫폼 하나당 월 사용 가능 금액을 입력하세요: "))
        print("월 사용 가능 금액이 입력되었습니다.")
    except ValueError:
        print("숫자만 입력할 수 있습니다. 다시 시도해주세요.")
 
 
# 2. 정기 구독 서비스 추가 함수
def add_service():
    # [예외 처리] 구독 비용 입력 시 문자를 입력했을 때 ValueError 처리
    try:
        platform = input("구독 플랫폼 이름을 입력하세요: ")
        price = int(input(f"{platform}의 월 구독 비용을 입력하세요: "))
        category = input(f"{platform}의 종류를 입력하세요(예: OTT, 공부, GPT): ")
 
        # [이름, 가격, 종류] 형태 append
        data.append([platform, price, category])
        print("구독 서비스가 추가되었습니다.")
    except ValueError:
        print("구독 비용은 숫자만 입력할 수 있습니다. 다시 시도해주세요.")
 
 
# 3. 특정 구독 서비스 수정 함수
def update_service():
    if len(data) == 0:
        print("수정할 구독 서비스가 없습니다.")
        return
 
    # [예외 처리] 수정 메뉴 번호 입력 시 문자 입력 방지
    try:
        modify = int(input("구독 플랫폼 이름 수정은 1, 구독 서비스 종류 수정은 2, 월 구독 비용 수정은 3을 눌러주세요: "))
    except ValueError:
        print("숫자만 입력할 수 있습니다.")
        return
 
    name = input("수정할 구독 서비스 이름을 입력하세요: ")
 
    idx = -1
    for i in range(len(data)):
        if data[i][0] == name:
            idx = i
            break
 
    if idx == -1:
        print(f"'{name}'이(가) 존재하지 않습니다.")
        return
 
    if modify == 1:
        print(f"\n[현재 이름] {data[idx][0]}")
        new_name = input("새 이름을 입력하세요: ")
        data[idx][0] = new_name
        print("이름을 수정했습니다.")
 
    elif modify == 2:
        print(f"\n[현재 종류] {data[idx][2]}")
        new_category = input("새 종류를 입력하세요: ")
        data[idx][2] = new_category
        print("종류를 수정했습니다.")
 
    elif modify == 3:
        # [예외 처리] 가격 수정 시 문자 입력 방지
        try:
            print(f"\n[현재 가격] {data[idx][1]}원")
            new_price = int(input("새 월 구독 가격을 입력하세요: "))
            data[idx][1] = new_price
            print("가격을 수정했습니다.")
        except ValueError:
            print("가격은 숫자만 입력할 수 있습니다.")
 
    else:
        print("잘못된 수정 메뉴입니다.")
 
 
# 4. 총 월 구독 비용 계산 함수
def total_month():
    global total_cost
 
    if len(data) == 0:
        print("등록된 구독 서비스가 없습니다.")
        return 0
 
    # 이중 리스트에서 각 항목의 가격만 꺼내어 합산
    prices = [item[1] for item in data]
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
def all_service():
    if len(data) == 0:
        print("현재 등록된 구독 서비스가 없습니다.")
        return
 
    headers = ["이름", "월 구독 비용(원)", "종류"]
 
    print()
    print("[현재 구독 서비스 정보]")
    print("-" * 40)
 
    # 외부 for: 각 구독 항목 순회 / 내부 for: 항목 내 필드 순회
    for i, item in enumerate(data):
        print(f"{i + 1}번 구독 서비스:")
        for j in range(len(item)):
            if j == 1:
                print(f"  {headers[j]}: {item[j]}원")
            else:
                print(f"  {headers[j]}: {item[j]}")
    print("-" * 40)
 
 
# 6. 예산 초과 여부 확인 함수
def bud_check():
    if month_bud == 0:
        print("플랫폼 하나당 월 사용 가능 금액부터 입력하세요.")
        return
 
    if len(data) == 0:
        print("등록된 구독 서비스가 없습니다.")
        return
 
    prices = [item[1] for item in data]
    total = sum(prices)
    limit = month_bud * len(data)
 
    print()
    print("[예산 확인 결과]")
    print(f"플랫폼 하나당 월 사용 가능 금액: {month_bud}원")
    print(f"구독 플랫폼 수: {len(data)}개")
    print(f"총 사용 가능 예산: {limit}원")
    print(f"총 월 구독 비용: {total}원")
 
    if total > limit:
        print("사용가능 금액을 초과합니다. 줄여야 합니다.")
    elif total == limit:
        print("월 구독 비용 예산과 동일합니다. 더 이상 추가하면 초과합니다.")
    else:
        print("사용가능 금액을 초과하지 않습니다.")
 
 
# 7. 특정 구독 서비스 삭제 함수
def delete_service():
    if len(data) == 0:
        print("삭제할 구독 서비스가 없습니다.")
        return
 
    all_service()
    name = input("삭제할 구독 서비스 이름을 입력하세요: ")
 
    # 2D 리스트에서 이름(인덱스 0)으로 검색 후 삭제
    for i in range(len(data)):
        if data[i][0] == name:
            data.pop(i)
            print(f"'{name}' 서비스가 삭제되었습니다.")
            return
 
    print(f"'{name}'이(가) 존재하지 않습니다.")
 
 
# 8. 파일 저장 함수 - 종료 시 data를 CSV 파일로 저장
def save_to_file():
    with open("구독목록.csv", "w", encoding="utf-8") as f:
        f.write("플랫폼 이름,월 구독 비용,종류\n")
        # 2D 리스트의 각 항목을 CSV 한 줄로 저장
        for item in data:
            f.write(f"{item[0]},{item[1]},{item[2]}\n")
    print("구독 목록이 '구독목록.csv' 파일에 저장되었습니다.")
 
 
# 9. 파일 불러오기 함수 - 프로그램 시작 시 기존 저장 파일 로드
def load_from_file():
    # [예외 처리] 저장 파일이 없을 때 FileNotFoundError 처리
    try:
        with open("구독목록.csv", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # 헤더(첫 줄) 제외하고 읽기
            for line in lines[1:]:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                # [이름, 가격(정수), 종류] 형태로 append
                data.append([parts[0], int(parts[1]), parts[2]])
        print(f"기존 구독 목록을 불러왔습니다. (총 {len(data)}개)")
    except FileNotFoundError:
        print("저장된 구독 목록 파일이 없습니다. 새로 시작합니다.")
 
 
load_from_file()
 
# 메뉴 출력
while True:
    print()
    print("=" * 35)
    print("  나만의 정기 구독 비용 관리 시스템")
    print("=" * 35)
    print("1. 플랫폼 하나당 월 사용 가능 금액 입력")
    print("2. 정기 구독 서비스 추가")
    print("3. 특정 구독 서비스 수정")
    print("4. 총 월 구독 비용 계산")
    print("5. 전체 구독 서비스 조회")
    print("6. 예산 초과 여부 확인")
    print("7. 특정 구독 서비스 삭제")
    print("8. 종료")
    print("=" * 35)
 
    # [예외 처리] 메뉴 선택 시 문자 입력 방지
    try:
        check = int(input(f"{user}가 원하는 메뉴를 입력하세요(숫자입력): "))
    except ValueError:
        print("숫자만 입력할 수 있습니다. 다시 입력하세요.")
        continue
 
    if check == 1:
        input_budget()
 
    elif check == 2:
        add_service()
 
    elif check == 3:
        update_service()
 
    elif check == 4:
        total_month()
 
    elif check == 5:
        all_service()
 
    elif check == 6:
        bud_check()
 
    elif check == 7:
        delete_service()
 
    elif check == 8:
        save_to_file()
        print("프로그램을 종료합니다.")
        break
 
    else:
        print("잘못된 메뉴입니다. 다시 입력하세요.")

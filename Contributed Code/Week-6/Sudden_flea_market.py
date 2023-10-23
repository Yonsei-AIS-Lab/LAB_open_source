class Gun:
    def __init__(self, name, damage, fire_rate, accuracy, recoil, ammo, gun_type, price):
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate
        self.accuracy = accuracy
        self.recoil = recoil
        self.ammo = ammo
        self.gun_type = gun_type
        self.price = price

# 총 정보 초기화
guns = [
    Gun("AK-47", 45, 72, 87, 85, "30/120", "돌격소총", 1000),
    Gun("M4A1 Carbine", 32, 82, 88, 44, "30/120", "돌격소총", 1500),
    Gun("SIG556", 37, 82, 86, 50, "30/120", "돌격소총", 2000),
    Gun("TRG-21", 100, 0, 100, 85, "5/20", "저격소총", 3000),
    Gun("Winchester m73", 100, 9, 100, 85, "3/18", "저격소총", 3000),
    Gun("컴뱃보우", 100, 0, 98, 70, "1/40", "저격소총", 2000)
]

player_points = 5000  # 초기 포인트 설정
player_inventory = []  # 플레이어 보유 총 리스트

# 메뉴 함수 정의
def show_menu():
    print("\n메뉴:")
    print("1. 총 목록 출력")
    print("2. 총 구매")
    print("3. 총 판매")
    print("4. 종료")
    print("5. 총 조회")

# 게임 루프
while True:
    show_menu()
    choice = input("원하는 작업을 선택하세요: ").strip()

    if choice == '4':
        print("게임 종료")
        break
    elif choice == '1':
        print("\n가능한 총 목록:")
        for i, gun in enumerate(guns, 1):
            print(f"{i}. {gun.name} - 가격: {gun.price} 포인트")
    elif choice == '2':
        print("\n가능한 총 목록:")
        for i, gun in enumerate(guns, 1):
            print(f"{i}. {gun.name} - 가격: {gun.price} 포인트")
        buy_choice = input("구매할 총을 선택하세요 (또는 '취소'): ").strip()
        if buy_choice == '취소':
            continue
        if buy_choice.isdigit():
            buy_choice = int(buy_choice)
            if 1 <= buy_choice <= len(guns):
                selected_gun = guns[buy_choice - 1]
                if player_points >= selected_gun.price:
                    player_points -= selected_gun.price
                    player_inventory.append(selected_gun)
                    print(f"{selected_gun.name}을(를) 구매하셨습니다!")
                else:
                    print("포인트가 부족하여 총을 구매할 수 없습니다.")
            else:
                print("잘못된 선택입니다.")
        else:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
    elif choice == '3':
        if len(player_inventory) > 0:
            print("\n판매할 총 목록:")
            for i, gun in enumerate(player_inventory, 1):
                print(f"{i}. {gun.name} - 가격: {gun.price // 2} 포인트")
            sell_choice = input("판매할 총을 선택하세요 (또는 '취소'): ").strip()
            if sell_choice == '취소':
                continue
            if sell_choice.isdigit():
                sell_choice = int(sell_choice)
                if 1 <= sell_choice <= len(player_inventory):
                    sold_gun = player_inventory.pop(sell_choice - 1)
                    player_points += sold_gun.price // 2
                    print(f"{sold_gun.name}을(를) 판매하셨습니다. 받은 포인트: {sold_gun.price // 2} 포인트")
                else:
                    print("잘못된 선택입니다.")
            else:
                print("잘못된 입력입니다. 숫자를 입력하세요.")
        else:
            print("보유한 총이 없습니다.")
    elif choice == '5':
        print("\n가능한 총 목록:")
        for i, gun in enumerate(guns, 1):
            print(f"{i}. {gun.name} - 가격: {gun.price} 포인트")
        inspect_gun_choice = input("조회할 총을 선택하세요 (또는 '취소'): ").strip()
        if inspect_gun_choice == '취소':
            continue
        if inspect_gun_choice.isdigit():
            inspect_gun_choice = int(inspect_gun_choice)
            if 1 <= inspect_gun_choice <= len(guns):
                inspected_gun = guns[inspect_gun_choice - 1]
                print(f"\n총 이름: {inspected_gun.name}")
                print(f"데미지: {inspected_gun.damage}")
                print(f"발사 속도: {inspected_gun.fire_rate}")
                print(f"정확도: {inspected_gun.accuracy}")
                print(f"반동: {inspected_gun.recoil}")
                print(f"탄약: {inspected_gun.ammo}")
                print(f"총 종류: {inspected_gun.gun_type}")
                print(f"가격: {inspected_gun.price} 포인트")
            else:
                print("잘못된 선택입니다.")
        else:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
    else:
        print("잘못된 선택입니다. 다시 선택하세요.")

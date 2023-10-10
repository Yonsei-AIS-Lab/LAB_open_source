from vending_machine import VendingMachine

def main():
    vending_machine = VendingMachine()

    while True:
        print("\n자판기 메뉴:")
        print("1. 음료수 목록 표시")
        print("2. 금액 투입")
        print("3. 음료수 구매")
        print("4. 잔액 확인")
        print("5. 종료")
        print("6. 음료수 추가 (관리자 모드)")
        choice = input("작업을 선택하세요: ")

        if choice == '5':
            print("프로그램을 종료합니다.")
            break

        if choice == '1':
            vending_machine.display_products()
        elif choice == '2':
            amount = int(input("투입할 금액을 입력하세요: "))
            vending_machine.insert_money(amount)
            print("금액이 투입되었습니다.")
        elif choice == '3':
            product_name = input("구매할 음료수 이름을 입력하세요: ")
            result = vending_machine.purchase(product_name)
            print(result)
        elif choice == '4':
            balance = vending_machine.check_balance()
            print(balance)
        elif choice == '6':
            # 음료수를 추가할 수 있는 관리자 모드
            product_name = input("추가할 음료수 이름을 입력하세요: ")
            product_price = input("추가할 음료수 금액을 입력하세요: ")
            vending_machine.add_drink(product_name, product_price)
        else:
            print("올바른 선택이 아닙니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
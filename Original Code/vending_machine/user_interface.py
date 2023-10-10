from vending_machine import VendingMachine

def main():
    vending_machine = VendingMachine()

    while True:
        vending_machine.display_products()
        print(vending_machine.check_balance())
        print("자판기 메뉴:")
        print("1. 금액 투입")
        print("2. 음료수 구매")
        print("3. 종료")
        choice = input("작업을 선택하세요: ")

        if choice == '3':
            print("프로그램을 종료합니다.")
            break

        elif choice == '1':
            amount = int(input("투입할 금액을 입력하세요: "))
            vending_machine.insert_money(amount)
            print("금액이 투입되었습니다.")
        elif choice == '2':
            product_name = input("구매할 음료수 이름을 입력하세요: ")
            result = vending_machine.purchase(product_name)
            print(result)
        else:
            print("올바른 선택이 아닙니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
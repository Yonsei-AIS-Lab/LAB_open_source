class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} 원이 입금되었습니다. 현재 잔액: {self.balance} 원")
        else:
            print("유효한 금액을 입력하세요.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} 원이 출금되었습니다. 현재 잔액: {self.balance} 원")
            else:
                print("잔액이 부족합니다.")
        else:
            print("유효한 금액을 입력하세요.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"계좌번호: {self.account_number}, 소유자: {self.owner}, 잔액: {self.balance} 원"

def main():
    accounts = []

    while True:
        print("\n은행 계좌 관리 프로그램")
        print("1. 계좌 생성")
        print("2. 입금")
        print("3. 출금")
        print("4. 계좌 조회")
        print("5. 종료")

        choice = input("선택: ")

        if choice == '1':
            account_number = input("계좌번호: ")
            owner = input("소유자 이름: ")
            account = BankAccount(account_number, owner)
            accounts.append(account)
            print("계좌가 생성되었습니다.")
        elif choice == '2':
            account_number = input("입금할 계좌번호: ")
            amount = float(input("입금할 금액: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    break
            else:
                print("계좌를 찾을 수 없습니다.")
        elif choice == '3':
            account_number = input("출금할 계좌번호: ")
            amount = float(input("출금할 금액: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.withdraw(amount)
                    break
            else:
                print("계좌를 찾을 수 없습니다.")
        elif choice == '4':
            account_number = input("조회할 계좌번호: ")
            for account in accounts:
                if account.account_number == account_number:
                    print(account)
                    break
            else:
                print("계좌를 찾을 수 없습니다.")
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 옵션을 선택하세요.")

if __name__ == "__main__":
    main()

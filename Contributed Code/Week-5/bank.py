class BankAccount:
    def __init__(self, account_number, owner, password, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.password = password  # 비밀번호 속성 추가
        self.balance = balance

    def deposit(self, amount, password):
        if password != self.password:  # 비밀번호 확인
            print("비밀번호가 틀렸습니다.")
            return
        
        if amount > 0:
            self.balance += amount
            print(f"{amount} 원이 입금되었습니다. 현재 잔액: {self.balance} 원")
        else:
            print("유효한 금액을 입력하세요.")

    def withdraw(self, amount, password):
        if password != self.password:  # 비밀번호 확인
            print("비밀번호가 틀렸습니다.")
            return
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} 원이 출금되었습니다. 현재 잔액: {self.balance} 원")
            else:
                print("잔액이 부족합니다.")
        else:
            print("유효한 금액을 입력하세요.")

    def get_balance(self, password):
        if password != self.password:  # 비밀번호 확인
            print("비밀번호가 틀렸습니다.")
            return None
        return self.balance

    def __str__(self):
        return f"계좌번호: {self.account_number}, 소유자: {self.owner}, 잔액: {self.balance} 원"

def main():
    accounts = []
    admin_password = "admin" # 기본 패스워드

    while True:
        print("\n은행 계좌 관리 프로그램")
        print("1. 계좌 생성")
        print("2. 입금")
        print("3. 출금")
        print("4. 계좌 조회")
        print("5. 종료")
        print("6. 직원") # 새 옵션 추가

        choice = input("선택: ")

        if choice == '1':
            account_number = input("계좌번호: ")
            owner = input("소유자 이름: ")
            password = input("비밀번호 설정: ")  # 비밀번호 설정 추가
            account = BankAccount(account_number, owner, password)
            accounts.append(account)

            print("계좌가 생성되었습니다.")
            for account in accounts:
                if account.account_number == account_number:
                    print("다른 계좌번호를 사용하세요.")
                    break
            else:
                account = BankAccount(account_number, owner)
                accounts.append(account)
                print("계좌가 생성되었습니다.")
                
        elif choice == '2':
            account_number = input("입금할 계좌번호: ")
            password = input("비밀번호 입력: ")  # 비밀번호 입력 추가
            amount = float(input("입금할 금액: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.deposit(amount, password)  # 비밀번호 전달 추가
                    break
            else:
                print("계좌를 찾을 수 없습니다.")
        elif choice == '3':
            account_number = input("출금할 계좌번호: ")
            password = input("비밀번호 입력: ")  # 비밀번호 입력 추가
            amount = float(input("출금할 금액: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.withdraw(amount, password)  # 비밀번호 전달 추가
                    break
            else:
                print("계좌를 찾을 수 없습니다.")
        elif choice == '4':
            account_number = input("조회할 계좌번호: ")
            password = input("비밀번호 입력: ")  # 비밀번호 입력 추가
            for account in accounts:
                if account.account_number == account_number:
                    if account.get_balance(password) is not None:  # 비밀번호 전달 추가
                        print(account)
                    break
            else:
                print("계좌를 찾을 수 없습니다.")
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        elif choice == '6':
            admin_password_input = input("관리자 비밀번호를 입력하세요: ")
            if admin_password_input == admin_password:
                while True:
                    print("\n직원 메뉴")
                    print("1. 전체 계좌 조회")
                    print("2. 관리자 비밀번호 변경")
                    print("3. 계좌 삭제")
                    print("4. 돌아가기")

                    admin_choice = input("선택: ")

                    if admin_choice == '1':
                        print("\n전체 계좌 정보")
                        if accounts == []:
                            print("등록된 계좌가 없습니다.")
                        else:
                            print("\n계좌번호 / 이름 / 잔액")
                            for account in accounts:
                                print(f"{account.account_number} / {account.owner} / {account.balance}")
                    elif admin_choice == '2':
                        admin_password = input("새로운 관리자 비밀번호를 입력하세요: ")
                        print("관리자 비밀번호가 변경되었습니다.")
                    elif admin_choice == '3':
                        deleted_account = input("삭제할 계좌번호를 입력하세요: ")
                        for account in accounts:
                            if account.account_number == deleted_account:
                                accounts.remove(account)
                                print("삭제 완료")
                                break
                            else:
                                print("계좌를 찾을 수 없습니다.")
                    elif admin_choice == '4':
                        break
                    else:
                        print("올바른 옵션을 선택하세요.")
            else:
                print("잘못된 비밀번호입니다. 다시 시도하세요.")
        else:
            print("올바른 옵션을 선택하세요.")

if __name__ == "__main__":
    main()
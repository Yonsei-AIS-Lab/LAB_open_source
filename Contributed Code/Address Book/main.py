from contacts import Contacts
import signal # signal 모듈을 import
import sys  # sys 모듈을 import

def main():
    contacts = Contacts()

    # Ctrl-C 처리 함수
    def signal_handler(signal, frame):
        print("\n프로그램을 종료합니다.")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)  # Ctrl-C 누르면 signal_handler 함수 호출
    
    while True:
        print("주소록 관리 프로그램")
        print("1. 전체 주소록 보기")
        print("2. 주소록에 연락처 추가")
        print("3. 주소록에서 연락처 검색")
        print("4. 프로그램 종료")

        choice = input("선택: ")

        if choice == "1":
            contacts.display_contacts()
        elif choice == "2":
            name = input("이름: ")
            phone = input("전화번호: ")
            email = input("이메일: ")
            contacts.add_contact(name, phone, email)
        elif choice == "3":
            search_term = input("검색어: ")
            contacts.search_contacts(search_term)
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()

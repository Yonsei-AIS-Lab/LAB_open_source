from contacts import Contacts

def main():
    contacts = Contacts()

    while True:
        print("주소록 관리 프로그램")
        print("1. 전체 주소록 보기")
        print("2. 주소록에 연락처 추가")
        print("3. 주소록에 연락처 삭제")
        print("4. 주소록에서 연락처 검색")
        print("5. 프로그램 종료")

        choice = input("선택: ")

        if choice == "1":
            contacts.display_contacts()
        elif choice == "2":
            name = input("이름: ")
            phone = input("전화번호: ")
            email = input("이메일: ")
            contacts.add_contact(name, phone, email)
        elif choice == "3": # 삭제하는 코드 추가함.
            contacts.display_contacts()
            delete_index = int(input('삭제하고 싶은 번호를 입력하세요: ')) - 1 # 번호를 idx로 변환하기 위해 1을 빼줌.
            contacts.delete_contact(delete_index)
        elif choice == "4":
            search_term = input("검색어: ")
            contacts.search_contacts(search_term)
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()

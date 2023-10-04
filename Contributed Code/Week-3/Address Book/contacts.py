from file_operations import read_contacts, save_contacts

class Contacts:
    def __init__(self):
        self.contacts = read_contacts() # self.contacts는 'list' 타입 변수

    def display_contacts(self):
        if self.contacts: # Python에서 리스트는 비어있을 경우 False를 반환함.
            for contact in self.contacts:
                print(contact)
        else:
            print("주소록이 비어 있습니다.")

    def add_contact(self, name, phone, email):
        if not name or not phone or not email:  # 어느 하나라도 비어 있으면
            print("이름, 전화번호, 이메일중에 비어있는 곳이 있습니다.")
            return

        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)
        save_contacts(self.contacts)
        print("연락처가 추가되었습니다.")

    def search_contacts(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact["name"].lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("일치하는 연락처가 없습니다.")

    def delete_contact(self, idx):
        """
        연락처를 삭제하는 함수를 구현하였습니다.
        """
        del_contact = self.contacts.pop(idx)
        print(f'{del_contact["name"]}님의 연락처를 삭제했습니다.')
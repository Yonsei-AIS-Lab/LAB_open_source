from file_operations import read_contacts, save_contacts

class Contacts:
    def __init__(self):
        self.contacts = read_contacts()

    def display_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("주소록이 비어 있습니다.")

    def add_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)
        try:
            save_contacts(self.contacts)
            print("연락처가 추가되었습니다.")
        except Exception as e:
            print(f"연락처 추가 중 오류가 발생했습니다 : {e}")

    def search_contacts(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact["name"].lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("일치하는 연락처가 없습니다.")

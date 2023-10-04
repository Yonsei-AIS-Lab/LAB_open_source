CONTACTS_FILE = "./contacts.txt" # 비어있는 contacts.txt를 열 경우 에러가 발생함, 그리고 ./을 contacts.txt 앞에 붙여서 경로를 정확히 명시함

def read_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return eval(file.read())
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        file.write(repr(contacts))

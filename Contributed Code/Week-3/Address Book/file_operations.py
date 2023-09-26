CONTACTS_FILE = "./contacts.txt" # 비어있는 contacs.txt에 [] 넣어야 오류가 안 남.

def read_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return eval(file.read())
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        file.write(repr(contacts))

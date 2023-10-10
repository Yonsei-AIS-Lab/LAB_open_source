import os

# 텍스트 파일 관리 클래스 정의
class TextFileManager:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.current_file = None

    def create_file(self, filename):
        try:
            with open(os.path.join(self.current_directory, filename), 'w') as file:
                print(f"{filename} 파일이 생성되었습니다.")
        except Exception as e:
            print(f"파일 생성 중 오류 발생: {str(e)}")

    def set_current_file(self, filename):
        file_path = os.path.join(self.current_directory, filename)
        if os.path.exists(file_path):
            self.current_file = filename
            print(f"현재 작업 중인 파일: {filename}")
        else:
            print(f"파일 '{filename}'이(가) 존재하지 않습니다. 먼저 파일을 생성하세요.")

    def write_to_file(self, content):
        if self.current_file:
            try:
                with open(os.path.join(self.current_directory, self.current_file), 'a') as file:
                    file.write(content + '\n')
                print("내용이 파일에 추가되었습니다.")
            except Exception as e:
                print(f"파일에 내용 추가 중 오류 발생: {str(e)}")
        else:
            print("작업 중인 파일이 없습니다. 먼저 파일을 선택하세요.")

    def search_file(self, keyword):
        if self.current_file:
            try:
                with open(os.path.join(self.current_directory, self.current_file), 'r') as file:
                    lines = file.readlines()
                    matching_lines = [line.strip() for line in lines if keyword in line]
                if matching_lines:
                    print(f"'{keyword}'를 포함하는 내용을 찾았습니다:")
                    for line in matching_lines:
                        print(line)
                else:
                    print(f"'{keyword}'를 포함하는 내용을 찾을 수 없습니다.")
            except Exception as e:
                print(f"파일 검색 중 오류 발생: {str(e)}")
        else:
            print("작업 중인 파일이 없습니다. 먼저 파일을 선택하세요.")

    def display_file_content(self):
        if self.current_file:
            try:
                with open(os.path.join(self.current_directory, self.current_file), 'r') as file:
                    content = file.read()
                print(f"\n{self.current_file}의 내용:")
                print(content)
            except Exception as e:
                print(f"파일 읽기 중 오류 발생: {str(e)}")
        else:
            print("작업 중인 파일이 없습니다. 먼저 파일을 선택하세요.")

def main():
    file_manager = TextFileManager()
    
    while True:
        print("\n파일 관리 및 검색 도구")
        print("1. 파일 생성")
        print("2. 현재 파일 선택")
        print("3. 파일에 내용 추가")
        print("4. 파일에서 검색")
        print("5. 파일 내용 출력")
        print("6. 종료")

        choice = input("선택: ")

        if choice == "1":
            filename = input("생성할 파일 이름을 입력하세요: ")
            file_manager.create_file(filename)
        elif choice == "2":
            filename = input("작업할 파일 이름을 입력하세요: ")
            file_manager.set_current_file(filename)
        elif choice == "3":
            content = input("파일에 추가할 내용을 입력하세요: ")
            file_manager.write_to_file(content)
        elif choice == "4":
            keyword = input("검색할 키워드를 입력하세요: ")
            file_manager.search_file(keyword)
        elif choice == "5":
            file_manager.display_file_content() # 새로운 메뉴 추가
        elif choice == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()

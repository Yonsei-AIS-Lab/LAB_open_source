class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def view_tasks(self):
        if not self.tasks:
            print("할 일이 없습니다.")
        else:
            print("할 일 목록:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def edit_task(self, task_index, new_task):
        if task_index >= 1 and task_index <= len(self.tasks):
            self.tasks[task_index - 1] = new_task

def main():
    to_do_list = ToDoList()
    
    while True:
        print("\n할 일을 선택하세요:")
        print("1. 할 일 추가")
        print("2. 할 일 삭제")
        print("3. 할 일 목록 보기")
        print("4. 할 일 수정")
        print("5. 종료")

        choice = input("선택: ")

        if choice == "1":
            task = input("추가할 할 일을 입력하세요: ")
            to_do_list.add_task(task)
        elif choice == "2":
            task = input("삭제할 할 일을 입력하세요: ")
            to_do_list.remove_task(task)
        elif choice == "3":
            to_do_list.view_tasks()
        elif choice == "4":
            task_index = int(input("수정할 할 일의 번호를 입력하세요: "))
            new_task = input("새로운 할 일을 입력하세요: ")
            to_do_list.edit_task(task_index, new_task)
        elif choice == "5":
            print("애플리케이션을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()

class Student:
    def __init__(self, student_id, name, score=0):
        self.student_id = student_id
        self.name = name
        self.score = score

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} 학생 정보가 추가되었습니다.")

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student(self, student_id, new_score):
        student = self.search_student(student_id)
        if student:
            student.score = new_score
            print(f"{student.name} 학생의 성적이 업데이트되었습니다.")
        else:
            print("학생을 찾을 수 없습니다.")

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            print(f"{student.name} 학생 정보가 삭제되었습니다.")
        else:
            print("학생을 찾을 수 없습니다.")

    def evaluate_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            if student.score >= 90:
                return "우수"
            elif student.score >= 70:
                return "보통"
            else:
                return "미흡"
        else:
            return "학생을 찾을 수 없습니다."

def main():
    student_manager = StudentManager()

    while True:
        print("\n학생 성적 관리 프로그램")
        print("1. 학생 정보 추가")
        print("2. 학생 정보 검색")
        print("3. 학생 정보 수정")
        print("4. 학생 정보 삭제")
        print("5. 학생 성적 평가")
        print("6. 전체 학생 정보 출력")
        print("7. 종료")

        choice = input("선택: ")

        if choice == '1':
            student_id = input("학번: ")
            name = input("이름: ")
            score = int(input("성적: "))
            student = Student(student_id, name, score)
            student_manager.add_student(student)
        elif choice == '2':
            student_id = input("검색할 학번: ")
            student = student_manager.search_student(student_id)
            if student:
                print(f"학번: {student.student_id}, 이름: {student.name}, 성적: {student.score}")
            else:
                print("학생을 찾을 수 없습니다.")
        elif choice == '3':
            student_id = input("성적을 수정할 학생의 학번: ")
            new_score = int(input("새로운 성적: "))
            student_manager.update_student(student_id, new_score)
        elif choice == '4':
            student_id = input("삭제할 학생의 학번: ")
            student_manager.delete_student(student_id)
        elif choice == '5':
            student_id = input("성적을 평가할 학생의 학번: ")
            evaluation = student_manager.evaluate_student(student_id)
            if evaluation:
                print(f"학생의 성적 평가: {evaluation}")
            else:
                print("학생을 찾을 수 없습니다.")
        elif choice == '6':
            print("\n전체 학생 정보")
            for student in student_manager.students:
                print(f"학번: {student.student_id}, 이름: {student.name}, 성적: {student.score}")
        elif choice == '7':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 옵션을 선택하세요.")

if __name__ == "__main__":
    main()

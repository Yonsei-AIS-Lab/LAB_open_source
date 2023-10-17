class Student:
    def __init__(self, student_id, name, score=0):
        self.student_id = student_id
        self.name = name
        self.score = score

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        existing_student = self.search_student(student.student_id)
        if existing_student:
            print(f"이미 존재하는 학번 ({student.student_id})입니다. 추가할 수 없습니다.")
        else:
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

    def update_student_name(self, student_id, new_name):
        student = self.search_student(student_id)
        if student:
            student.name = new_name
            print(f"학생의 이름이 {student.name} 으로 업데이트되었습니다.")
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
        
    def get_statistics(self):
        if not self.students:
            return "등록된 학생이 없습니다."

        total_score = 0
        highest_score = -1
        highest_student = None
        lowest_score = float('inf')
        lowest_student = None

        for student in self.students:
            total_score += student.score    # 평균을 찾기 위해 더하기
            if student.score > highest_score:   # 가장 높은 성적을 가진 학생을 찾기
                highest_score = student.score
                highest_student = student
            if student.score < lowest_score:    # 가장 낮은 성적을 가진 학생을 찾기
                lowest_score = student.score
                lowest_student = student

        average_score = total_score / len(self.students)
        return f" \n평균 점수 : {average_score:.2f} \n=============\n 최고 점수: \n 이름: {highest_student.name} \n 학번: {highest_student.student_id} \n 성적 : {highest_student.score} \n=============\n 최저 점수: \n 이름: {lowest_student.name} \n 학번: {lowest_student.student_id} \n 성적: {lowest_student.score}"

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
        print("7. 통계")
        print("8. 종료")

        choice = input("선택: ")

        if choice == '1':
            student_id = input("학번: ")
            name = input("이름: ")
            try:
                score = int(input("성적: "))
            except ValueError: # int 값 이외에 다른 값을 입력할 경우, 에러 핸들링
                print("올바른 성적을 입력하세요.")
                continue  # 다시 반복문으로 돌아가게 함
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
            print("수정하려는 항목을 선택해주세요.")
            print("1. 학생 이름 정보")
            print("2. 학생 성적 정보")
            choice_update = input("선택: ")
            
            if choice_update == '1':
                new_name = input("새로운 이름: ")
                student_manager.update_student_name(student_id, new_name)
            elif choice_update == '2':
                try:
                    new_score = int(input("새로운 성적: "))
                    student_manager.update_student(student_id, new_score)
                except ValueError:
                    print("올바른 숫자로 성적을 입력해주세요.")
            else:
                print("올바른 옵션을 선택하세요.")

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
            print(student_manager.get_statistics())
        elif choice == '8':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 옵션을 선택하세요.")

if __name__ == "__main__":
    main()

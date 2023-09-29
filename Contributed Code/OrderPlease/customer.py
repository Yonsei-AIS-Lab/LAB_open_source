# 고객 클래스를 정의합니다.
class Customer:
    # 초기화 메서드에서 고객 ID, 이름, 이메일을 인스턴스 변수로 설정합니다.
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id  # 고객 ID
        self.name = name  # 이름
        self.email = email  # 이메일

    # 객체를 문자열로 표현할 때 사용하는 메서드입니다.
    def __str__(self):
        return f"고객 ID: {self.customer_id}, 이름: {self.name}, 이메일: {self.email}"

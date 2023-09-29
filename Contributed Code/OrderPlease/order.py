# 주문 클래스를 정의합니다.
class Order:
    # 초기화 메서드에서 주문 ID, 고객, 총 금액을 인스턴스 변수로 설정합니다.
    def __init__(self, order_id, customer, total_amount):
        self.order_id = order_id  # 주문 ID
        self.customer = customer  # 고객 (Customer 객체)
        self.total_amount = total_amount  # 총 금액

    # 객체를 문자열로 표현할 때 사용하는 메서드입니다.
    def __str__(self):
        return f"주문 ID: {self.order_id}, 고객: {self.customer}, 총 금액: ₩{self.total_amount:.2f}"

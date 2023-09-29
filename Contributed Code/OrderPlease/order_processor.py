# Order 클래스를 import 합니다.
from order import Order

# 주문 처리 클래스를 정의합니다.
class OrderProcessor:
    # 초기화 메서드에서 주문 리스트를 인스턴스 변수로 설정합니다.
    def __init__(self):
        self.orders = []  # 주문 리스트

    # 고객과 주문 항목을 받아 새로운 주문을 만들고, 이를 리스트에 추가하는 메서드입니다.
    def place_order(self, customer, order_items):
        # 총 금액은 각 항목의 가격과 수량을 곱한 값들의 합계입니다.
        total_amount = sum(item["price"] * item["quantity"] for item in order_items)
        
        # 새로운 주문 ID는 현재 주문 리스트의 길이에 1을 더한 값입니다.
        order_id = len(self.orders) + 1
        
        # 새 Order 객체를 생성합니다. 
        new_order = Order(order_id, customer, total_amount)
        
        # 이 객체를 orders 리스트에 추가합니다.
        self.orders.append(new_order)
        
        return new_order

    # 모든 주문을 출력하는 메서드입니다. 
    def list_orders(self):
        for order in self.orders:
            print(order)

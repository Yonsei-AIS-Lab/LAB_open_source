"""
이 코드는 간단한 주문 처리 시스템을 모방하는 프로그램으로, 고객 정보 관리 및 주문 처리를 중심으로 기능을 제공합니다. 
프로그램은 고객 정보를 입력하고, 주문을 생성하며, 현재까지의 주문 목록을 출력하는 기능을 포함합니다. 
각 고객과 주문은 해당하는 클래스를 통해 관리되며, main.py에서 가상의 고객을 생성하고 주문을 처리하여 시스템 동작을 시뮬레이션합니다. 
이 코드는 간단한 학습 및 이해를 위한 예시로 활용될 수 있으며, 실제 프로덕션 환경에서는 데이터베이스와 확장된 기능이 필요할 것입니다.
"""

from customer import Customer
from order import Order
from order_processor import OrderProcessor

if __name__ == "__main__":
    # 고객 생성
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer2 = Customer(2, "Bob", "bob@example.com")

    # 주문 처리기 생성
    order_processor = OrderProcessor()

    # 주문 생성
    order1 = order_processor.place_order(customer1, [{"item": "Product A", "price": 20, "quantity": 2},
                                                      {"item": "Product B", "price": 30, "quantity": 1}])

    order2 = order_processor.place_order(customer2, [{"item": "Product C", "price": 15, "quantity": 3},
                                                      {"item": "Product D", "price": 25, "quantity": 2}])

    # 주문 목록 확인
    print("List of Orders:")
    order_processor.list_orders()

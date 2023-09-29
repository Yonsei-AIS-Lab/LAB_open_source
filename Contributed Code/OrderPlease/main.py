"""
이 코드는 간단한 주문 처리 시스템을 모방하는 프로그램으로, 고객 정보 관리 및 주문 처리를 중심으로 기능을 제공합니다. 
프로그램은 고객 정보를 입력하고, 주문을 생성하며, 현재까지의 주문 목록을 출력하는 기능을 포함합니다. 
각 고객과 주문은 해당하는 클래스를 통해 관리되며, main.py에서 가상의 고객을 생성하고 주문을 처리하여 시스템 동작을 시뮬레이션합니다. 
이 코드는 간단한 학습 및 이해를 위한 예시로 활용될 수 있으며, 실제 프로덕션 환경에서는 데이터베이스와 확장된 기능이 필요할 것입니다.
"""

# 필요한 클래스를 import 합니다.
from customer import Customer
from order_processor import OrderProcessor

# 이 파이썬 스크립트가 메인으로 실행될 때만 아래의 코드를 실행합니다.
if __name__ == "__main__":
    # OrderProcessor 객체를 생성합니다.
    order_processor=OrderProcessor()

    # 무한 루프를 시작합니다. 사용자가 '3'을 입력하여 프로그램을 종료하기 전까지 계속됩니다.
    while True:
        print("1. 고객 추가 및 주문")
        print("2. 주문 목록 보기")
        print("3. 종료")

        # 사용자로부터 선택사항을 입력받습니다.
        choice=input("선택사항을 입력하세요:")

        # 고객 추가 및 주문
        if choice=='1':
            id=input("고객 ID를 입력하세요:")
            name=input("고객 이름을 입력하세요:")
            email=input("고객 이메일을 입력하세요:")
            new_customer=Customer(id,name,email)  # 새로운 Customer 객체 생성

            order_items=[]  # 주문 항목 리스트 초기화
            while True:
                print("1.상품 추가")
                print("2.주문 완료")
                item_choice=input("선택사항을 입력하세요:")

                if item_choice=='1':
                    item_name=input("상품 이름을 입력하세요:")
                    item_price=float(input("상품 가격을 입력하세요:"))
                    quantity=int(input("주문 수량을 입력하세요:"))
                    order_items.append({"item":item_name,"price":item_price,"quantity":quantity})  # 상품 정보 저장

                elif item_choice=='2':
                    break  # 상품 추가 루프 종료
        
            new_order=order_processor.place_order(new_customer,order_items)  # 새로운 Order 객체 생성 및 저장
            
        elif choice=='2':  # 모든 주문 목록 출력
            print("주문 목록:")
            order_processor.list_orders()
            
        elif choice=='3':  # 프로그램 종료
            break

        else:  # 잘못된 선택사항에 대한 처리
	        print("잘못된 선택입니다!")

class Order:
    def __init__(self, order_id, customer, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.total_amount = total_amount

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer.name}, Total Amount: ${self.total_amount:.2f}"
    # __str__메서드에서 주문의 고객 정보를 출력하려고 할 때 'Customer'객체를 그대로 출력하려고 하고 있으므로
    # Customer 클래스에 __str__메서드를 이용해 고객의 이름을 출력하도록 변경
    # 위 코드에서는 Order의 __str__ 메서드에서 self.customer 대신 self.customer.name을 사용하여 고객의 이름만 출력하도록 수정
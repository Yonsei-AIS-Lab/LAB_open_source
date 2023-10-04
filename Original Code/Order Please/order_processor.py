from order import Order

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def place_order(self, customer, order_items):
        if not order_items:
            raise ValueError("주문 항목이 비어 있습니다.")

        total_amount = sum(item["price"] * item["quantity"] for item in order_items)
        order_id = len(self.orders) + 1
        new_order = Order(order_id, customer, order_items, total_amount)
        self.orders.append(new_order)
        return new_order
    
    def list_orders(self):
        if not self.orders:
            print("주문이 없습니다.")
        else:
            for order in self.orders:
                print(order)

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def place_order(self, customer, order_items):
        total_amount = sum(item["price"] * item["quantity"] for item in order_items)
        order_id = len(self.orders) + 1
        new_order = Order(order_id, customer, total_amount)
        self.orders.append(new_order)
        return new_order

    def list_orders(self):
        for order in self.orders:
            print(order)

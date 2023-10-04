class Order:
    def __init__(self, order_id, customer, order_items, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.ordered_items = order_items
        self.total_amount = total_amount

    def __str__(self):
        order_info = f"Order ID: {self.order_id}, Customer: {self.customer}, Total Amount: {self.total_amount}"
        item_info = "\n".join([f"Item: {item['item']}, Price: ${item['price']:.2f}, Quantity: {item['quantity']}"
                              for item in self.ordered_items])
        return order_info + "\n" + item_info + "\n"
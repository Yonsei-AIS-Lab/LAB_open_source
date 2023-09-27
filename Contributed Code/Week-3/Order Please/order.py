class Order:
    def __init__(self, order_id, customer, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.total_amount = total_amount

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer}, Total Amount: ${self.total_amount:.2f}"
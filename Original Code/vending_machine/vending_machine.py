class VendingMachine:
    def __init__(self):
        self.products = {
            '콜라': 1500,
            '사이다': 1200,
            '오렌지 주스': 1800,
            '물': 1000,
        }
        self.balance = 0

    def display_products(self):
        print("음료수 목록:")
        for i, (product, price) in enumerate(self.products.items()):
            print(f"{i + 1}. {product}: {price}원")

    def insert_money(self, amount):
        self.balance += amount

    def purchase(self, product_number):
        product_names = list(self.products.keys())
        if 1 <= product_number <= len(product_names):
            product_name = product_names[product_number - 1]
            price = self.products[product_name]
            if self.balance >= price:
                self.balance -= price
                return f"{product_name}을 구매했습니다."
            else:
                return "잔액이 부족합니다."
        else:
            return "해당 제품은 판매하지 않습니다."

    def check_balance(self):
        return f"잔액: {self.balance}원"
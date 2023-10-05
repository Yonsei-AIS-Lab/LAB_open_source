class VendingMachine:
    def __init__(self):
        self.products = {
            '콜라': [1500,5],
            '사이다': [1200,5],
            '오렌지 주스': [1800,5],
            '물': [1000,5],
        }
        self.balance = 0

    def display_products(self):
        print("<음료수>")
        for product, info in self.products.items():
            if info[1] == 0:
                print(f"{product}: {info[0]}원 -품절-")
            else:        
                print(f"{product}: {info[0]}원")

    def insert_money(self, amount):
        self.balance += amount

    def purchase(self, product_name):
        if (product_name in self.products) and (self.products[product_name][1] > 0):
            info = self.products[product_name]
            if self.balance >= info[0]:
                self.balance -= info[0]
                info[1] -= 1
                return f"{product_name}을 구매했습니다."
            else:
                return "잔액이 부족합니다."
        else:
            return "해당 제품은 판매하지 않거나 품절입니다."

    def check_balance(self):
        return f"\n잔액: {self.balance}원"
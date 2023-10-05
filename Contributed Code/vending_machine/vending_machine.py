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
        for product, price in self.products.items():
            print(f"{product}: {price}원")

    def insert_money(self, amount):
        self.balance += amount

    def purchase(self, product_name):
        if product_name in self.products:
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
    
    def return_change(self):
        change = self.balance
        change_str = "거스름돈: "
        
        num_1000 = change // 1000
        if num_1000 > 0:
            change_str += f"1000원 {num_1000}개, "
            change %= 1000
        
        num_500 = change // 500
        if num_500 > 0:
            change_str += f"500원 {num_500}개, "
            change %= 500
        
        num_100 = change // 100
        if num_100 > 0:
            change_str += f"100원 {num_100}개, "
            change %= 100
        
        num_50 = change // 50
        if num_50 > 0:
            change_str += f"50원 {num_50}개, "
            change %= 50
        
        num_10 = change // 10
        if num_10 > 0:
            change_str += f"10원 {num_10}개"
        
        self.balance = 0  # 잔액 초기화
        return change_str

import numpy as np

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    num1 = int(input("첫 번째 정수를 입력하세요: "))
    num2 = int(input("두 번째 정수를 입력하세요: "))

    gcd_result = gcd(num1, num2)

    print(f"{num1}와 {num2}의 최대 공약수는 {gcd_result}입니다.")

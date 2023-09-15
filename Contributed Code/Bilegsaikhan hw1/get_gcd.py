import numpy as np

def gcd(a, b):
    a, b = abs(a), abs(b)  # 입력을 양수로 바꾼다
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:    # 입력이 정수인지 확인한다
        num1 = int(input("첫 번째 정수를 입력하세요: "))
        num2 = int(input("두 번째 정수를 입력하세요: "))

        gcd_result = gcd(num1, num2)

        print(f"{num1}와 {num2}의 최대 공약수는 {gcd_result}입니다.")
    except ValueError:
        print("정수를 입력하세요.")

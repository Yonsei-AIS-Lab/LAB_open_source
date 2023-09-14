#numpy 모듈 사용안함 import numpy as np
def gcd(a, b): #try except 예외처리
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:
        num1 = int(input("첫 번째 정수를 입력하세요: "))
        num2 = int(input("두 번째 정수를 입력하세요: "))

        gcd_result = gcd(num1, num2)

        print(f"{num1}와 {num2}의 최대 공약수는 {gcd_result}입니다.")
    except ValueError:
        print("잘못된 입력입니다. 정수만 입력 가능합니다.")

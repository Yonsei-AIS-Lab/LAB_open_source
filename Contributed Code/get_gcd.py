import numpy as np

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    # 두 정수의 gcd를 구할 때, 두 수 모두 0이 되면 안된다.
    # 그래서 예외처리를 수행할 것이다.
    while(True):
        num1 = int(input("첫 번째 정수를 입력하세요: "))
        num2 = int(input("두 번째 정수를 입력하세요: "))
        if num1 == 0 and num2 == 0: # 만약 두 수 모두 0일 경우
            print("both of the numbers cannot be 0s. try something else!")
        else:
            break

    gcd_result = gcd(num1, num2)

    print(f"{num1}와 {num2}의 최대 공약수는 {gcd_result}입니다.")
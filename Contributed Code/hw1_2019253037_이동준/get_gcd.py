# 사용자가 정수가 아닌 값을 입력하면 ValueError가 발생, 예외를 처리하는 코드를 추가


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    while True:
        try:
            num1 = int(input("첫 번째 정수를 입력하세요: "))
            break
        except ValueError:
            print("유효한 정수를 입력하세요.")

    while True:
        try:
            num2 = int(input("두 번째 정수를 입력하세요: "))
            break
        except ValueError:
            print("유효한 정수를 입력하세요.")

    gcd_result = gcd(num1, num2)

    print(f"{num1}와 {num2}의 최대 공약수는 {gcd_result}입니다.")

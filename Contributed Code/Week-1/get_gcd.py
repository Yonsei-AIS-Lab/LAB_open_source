def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:
        num1 = int(input("첫 번째 정수를 입력하세요: "))
        num2 = int(input("두 번째 정수를 입력하세요: "))
    except ValueError:
        print("양수만 입력해주세요")
        exit()

    if num1 < 0 or num2 < 0:
        print("양수만 입력해주세요")
        exit()

    gcd_result = gcd(num1, num2)

    print(f"{num1}와 {num2}의 최대 공약수는 {gcd_result}입니다.")
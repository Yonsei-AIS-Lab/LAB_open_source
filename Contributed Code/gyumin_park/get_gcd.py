def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:
        num1 = int(input("첫 번째 정수를 입력하세요: "))
        num2 = int(input("두 번째 정수를 입력하세요: "))

        if num1 < 0 or num2 < 0:
            print("양의 정수(0포함)만 입력하세요.")
        else:
            gcd_result = gcd(num1, num2)
            print(f"{num1}와 {num2}의 최대 공약수는 {gcd_result}입니다.")
    except ValueError:
        print("정수를 입력하세요(정수가 아니거나 음수는 오류입니다).")
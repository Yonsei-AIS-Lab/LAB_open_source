def fact(num) -> int:
    """
    정수의 factorial 연산을 하는 함수.
    num: 음이 아닌 정수
    """
    factorial = 1
    for i in range(1, num + 1):
            factorial *= i
    return factorial

if __name__ == "__main__":
    num = int(input("양의 정수를 입력하세요: "))

    if num < 0:
        print("음수는 팩토리얼을 계산할 수 없습니다.")
    else:
        factorial = fact(num) # factorial 함수 사용

        print(f"{num}! = {factorial}")
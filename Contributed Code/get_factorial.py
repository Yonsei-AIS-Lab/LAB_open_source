if __name__ == "__main__":
    try:
        num = int(input("양의 정수를 입력하세요: "))
        factorial = 1

        if num < 0:
            print("음수는 팩토리얼을 계산할 수 없습니다.")
        elif num == 0:
            print("0! = 1")
        else:
            factorial = 1
            for i in range(1, num + 1):
                factorial *= i

            print(f"{num}! = {factorial}")
    except ValueError:
        print("올바른 정수를 입력하세요.")
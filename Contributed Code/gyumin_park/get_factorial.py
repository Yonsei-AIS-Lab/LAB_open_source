if __name__ == "__main__":
    num = input("양의 정수를 입력하세요: ")
    factorial = 1

    if num.isdigit():
        input = int(num)

        if input < 0:
            print("음수는 팩토리얼을 계산할 수 없습니다.")
        else:
            for i in range(1, input + 1):
                factorial *= i

            print(f"{input}! = {factorial}")
    else:
        print("양의 정수가 아닙니다, 양의 정수(0포함)를 입력하세요.")

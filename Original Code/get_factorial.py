if __name__ == "__main__":
    while True:
        try:
            num = int(input("양의 정수를 입력하세요: "))
            if num >= 0:
                break
            else:
                print("음수는 입력할 수 없습니다. 다시 시도하세요.")
        except ValueError:
            print("유효한 정수를 입력하세요.")

    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print(f"{num}! = {factorial}")

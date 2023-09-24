if __name__ == "__main__":
    try:
        num = int(input("양의 정수를 입력하세요: "))
        if num <= 0:
            print("양의 정수를 입력하세요.")
        else:
            factorial = 1
            for i in range(1, num + 1):
                factorial *= i

            print(f"{num}! = {factorial}")
    except ValueError:
        print("정수를 입력하세요.")

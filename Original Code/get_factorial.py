if __name__ == "__main__":
    num = int(input("양의 정수를 입력하세요: "))
    factorial = 1

    if num < 0:
        print("음수는 팩토리얼을 계산할 수 없습니다.")
    else:
        for i in range(1, num + 1):
            factorial *= i

        print(f"{num}! = {factorial}")

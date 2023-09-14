if __name__ == "__main__": #try except 예외처리
    try:
        num = int(input("양의 정수를 입력하세요: "))
        factorial = 1

        if num < 0:
            print("음수는 팩토리얼을 계산할 수 없습니다.")
        elif num == 0:
            print("0! = 1")
        else:
            for i in range(1, num + 1):
                factorial *= i

            print(f"{num}! = {factorial}")
    except ValueError: #양수가 아닌 정수 입력시 처리
        print("잘못된 입력입니다. 양의 정수만 입력 가능합니다.")

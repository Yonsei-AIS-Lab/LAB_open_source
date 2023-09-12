def divide(a, b):
    result = a / b
    return result

def main():
    numbers = [15, -5, 0, 12, 3]

    # devisor가 0일 경우 다시 입력 받는 예외 처리 코드를 추가했습니다.
    while(True):
        divisor = int(input("divisor: "))
        if divisor == 0: # divisor가 0인 경우
            print("divisor cannot be 0, please try a different number!")
        else: # devisor가 0이 아닌 경우
            break

    for num in numbers:
        result = divide(num, divisor)

        if result > 5:
            print("Result is greater than 5.")
        else:
            print("Result is smaller than 5.")

if __name__ == "__main__":
    main()
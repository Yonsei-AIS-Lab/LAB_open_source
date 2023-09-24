def divide(a, b):
    if b==0: # 0 으로 나눌 수  없기 때문에
        result = 'INF'
    else:
        result = a / b
    return result

def main():
    numbers = [15, -5, 0, 12, 3]
    divisor = 2

    for num in numbers:
        result = divide(num, divisor)

        if result > 5:
            print("Result is greater than 5.")
        elif result == 'INF':
            print("Can't divide by zero.")
        elif result == 5:
            print("Result is equal to 5.") # 답이 5일 경우를 추가했음
        else:
            print("Result is smaller than 5.")

if __name__ == "__main__":
    main()

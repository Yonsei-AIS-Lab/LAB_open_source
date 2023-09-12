def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."

def main():
    numbers = [15, -5, 0, 12, 3]
    divisor = 2

    for num in numbers:
        result = divide(num, divisor)

        if result > 5:
            print("Result is greater than 5.")
        else:
            print("Result is smaller than 5.")

if __name__ == "__main__":
    main()

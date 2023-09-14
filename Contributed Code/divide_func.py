def divide(a, b):  #예외처리
    try:
        return a / b
    except ZeroDivisionError:
        print("ZeroDivisionError")
        return None

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



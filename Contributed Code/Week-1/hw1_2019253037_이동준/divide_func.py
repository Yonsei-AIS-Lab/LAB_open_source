def divide(a, b):
    #0으로 나누면 none을 리턴
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("ZeroDivisionError.")
        return None

def main():
    numbers = [15, -5, 0, 12, 3]
    divisor = 0 #2에서 0으로 바꿈

    for num in numbers:
        result = divide(num, divisor)

        if result is None:            
            continue

        if result > 5:
            print("Result is greater than 5.")
        else:
            print("Result is smaller than 5.")

if __name__ == "__main__":
    main()

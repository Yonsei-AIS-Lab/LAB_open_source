def divide(a, b):
    if b == 0:
        return None
    result = a / b
    return result

def main():
    numbers = [15, -5, 0, 12, 3]
    divisor = 2

    for num in numbers:
        result = divide(num, divisor)
        
        if result is None:
            print("It can't be divided by zero.")
        elif result > 5:
            print("Result is greater than 5.")
        else:
            print("Result is smaller than 5.")

if __name__ == "__main__":
    main()


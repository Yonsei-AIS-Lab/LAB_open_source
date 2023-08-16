def divide(a, b):
    result = a / b
    return result

def main():
    numbers = [10, 5, 0, 8, 3]
    divisor = 2

    for num in numbers:
        result = divide(num, divisor)
        print(f"Result of {num} divided by {divisor}: {result}")

        if result > 5:
            print("Result is greater than 5.")
        elif result < 0:
            print("Result is negative.")
        else:
            print("Result is neither greater than 5 nor negative.")

if __name__ == "__main__":
    main()

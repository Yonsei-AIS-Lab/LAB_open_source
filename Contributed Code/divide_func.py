def divide(a, b):
    result = a / b
    return result

def main():
    numbers = [15, -5, 0, 12, 3]
    while(True):
        divisor = int(input("divisor: "))
        if divisor == 0:
            print("divisor cannot be 0, please try a different number!")
        else:
            break

    for num in numbers:
        result = divide(num, divisor)

        if result > 5:
            print("Result is greater than 5.")
        else:
            print("Result is smaller than 5.")

if __name__ == "__main__":
    main()
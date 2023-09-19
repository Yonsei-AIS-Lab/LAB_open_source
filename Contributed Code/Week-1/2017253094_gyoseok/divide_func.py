def divide(a, b):
    result = a / b
    return result

def main():
    numbers = [15, -5, 0, 12, 3]
    divisor = 2

    for num in numbers:
        try:
            result = divide(num, divisor)        
            if result > 5:
                print("Result is greater than 5.")
            else:
                print("Result is smaller than 5.")
                
        except ValueError as v:
            print('오류:', e)
        except ZeroDivisionError as e:
            print('오류:', e)

if __name__ == "__main__":
    main()

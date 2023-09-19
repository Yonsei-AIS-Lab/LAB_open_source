if __name__ == "__main__":
    try:#추가: int가 아닌 잘못된 타입이 입력되었을 경우 예외처리
        num = int(input("양의 정수를 입력하세요: "))
        factorial = 1
    
        if num < 0:
            raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.") #수정: 예외처리 형식에 맞게 변경
        elif num == 0:
            print("0! = 1")
        else:
            for i in range(1, num + 1):
                factorial *= i

            print(f"{num}! = {factorial}")
    except ValueError as e:
        print('오류발생:',e)

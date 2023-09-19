def get_list_element(data_list, index):
    if type(index) != type(1): #추가: 인덱스 타입이 잘못 입력되었을 때 예외처리
        return "인덱스 타입이 잘못 되었습니다."
    elif index < 0 or index >= len(data_list):
        return "Index out of range."
    element = data_list[index]
    
    return element

if __name__ == "__main__":
    my_list = [1, 2, 3]
    index = 5

    result = get_list_element(my_list, index)
    print(result)

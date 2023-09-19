import numpy as np

def get_list_element(data_list, index):
    if index < 0 or index >= len(data_list):
        raise ValueError("Index out of range.")
    element = data_list[index]
    return element

if __name__ == "__main__":
    my_list = np.arange(1, 100)
    try:  #추가: 인덱스 타입이 잘못 입력되었을 때 예외처리
        index = int(input("Enter an index: "))
        result = get_list_element(my_list, index)
        print(result)
    except ValueError as e:
        print('에러:',e)

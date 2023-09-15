import numpy as np

def get_list_element(data_list, index):
    try:
        element = data_list[index]
    except:
        element = "리스트 범위내의 인덱스를 입력하세요."
    return element

if __name__ == "__main__":
    my_list = np.arange(1, 100)
    index = int(input())

    result = get_list_element(my_list, index)
    print(result)

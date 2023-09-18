import numpy as np

def get_list_element(data_list, index):
    if 0 <= index < len(data_list):
        return data_list[index]
    else:
        return None

if __name__ == "__main__":
    my_list = np.arange(1, 100)
    index = int(input())

    result = get_list_element(my_list, index)
    if result is None:
        print("인덱스가 범위를 벗어났습니다")
    else:
        print(result)

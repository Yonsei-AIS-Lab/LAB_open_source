import numpy as np

def get_list_element(data_list, index):
    try:
        element = data_list[index]
        return element
    except IndexError:
        return None

if __name__ == "__main__":
    my_list = np.arange(1, 100)
    try:
        index = int(input("인덱스를 입력하세요: "))
        result = get_list_element(my_list, index)

        if result is not None:
            print(result)
        else:
            print("인덱스가 리스트 범위를 벗어났습니다.")
    except ValueError:
        print("올바른 정수를 입력하세요.")
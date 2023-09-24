import numpy as np


def get_list_element(data_list, index):
    try:
        element = data_list[index]
        return element
    except IndexError:
        print("인덱스 범위를 벗어났습니다.")
        return None


if __name__ == "__main__":
    my_list = np.arange(1, 100)

    while True:
        try:
            index = int(input("인덱스를 입력하세요: "))
            break
        except ValueError:
            print("정수를 입력하세요.")

    result = get_list_element(my_list, index)
    if result is not None:
        print(result)

#numpy 모듈 사용안함 import numpy as np
def get_list_element(data_list, index): #try except 예외처리
    try:
        element = data_list[index]
        return element
    except IndexError:
        print("IndexError")
        return None

if __name__ == "__main__":
    my_list = [1, 2, 3]
    index = 5

    result = get_list_element(my_list, index)
    
    if result is not None:
        print(result)

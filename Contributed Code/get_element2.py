import numpy as np

def get_list_element(data_list, index):
    element = data_list[index]
    
    return element

if __name__ == "__main__":
    my_list = np.arange(1, 100)
    len_mylist = len(my_list)
    
    # Index out of range에 대한 예외처리 코드 추가
    print(f"Instruction: input a number from 0 ~ {len_mylist-1}")
    
    while (True):
        index = int(input("input: "))
        if 0 <= index <= len_mylist-1: # 조건을 만족한다면 break하기
            break
        else:
            print("Follow the instruction!")

    result = get_list_element(my_list, index)
    print(f"result: {result}")
    
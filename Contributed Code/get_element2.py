import numpy as np

def get_list_element(data_list, index): #try except 예외처리
    try:
        element = data_list[index]
        return element
    except IndexError:
        print("IndexError")
        return None

if __name__ == "__main__":
    my_list = np.arange(1, 100)
    
    try:
        index = int(input())
        
        result = get_list_element(my_list, index)
        
        if result is not None:
            print(result)
            
    except ValueError:
        print("ValueError : 정수 입력 주의")

def get_list_element(data_list, index):
    element = data_list[index]
    
    return element

if __name__ == "__main__":
    my_list = [1, 2, 3]
    len_mylist = len(my_list)
    
    # Out of index에 대한 예외 처리 코드를 추가했습니다.
    while(True):
        index = int(input(f"input an integer below {len_mylist} and above -1:"))
        if index >= len_mylist:
            print(f"your input is not below {len_mylist}, try a smaller number")
        elif index < 0:
            print(f"your input is below than 0, try a bigger number")
        else:
            break

    result = get_list_element(my_list, index)
    print(result)
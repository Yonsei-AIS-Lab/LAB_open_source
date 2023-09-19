def get_list_element(data_list, index):
    try:
        element = data_list[index]
    except IndexError:
        element = "인덱스 범위가 넘어갔습니다."
    
    return element

if __name__ == "__main__":
    my_list = [1, 2, 3]
    index = 3

    result = get_list_element(my_list, index)
    print(result)
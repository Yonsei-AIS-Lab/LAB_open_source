def get_list_element(data_list, index):

    try:
        element = data_list[index]
        return element
    except IndexError:
        return "인덱스가 범위를 벗어났습니다."

if __name__ == "__main__":
    my_list = [1, 2, 3]
    index = 5

    result = get_list_element(my_list, index)
    print(result)
def get_list_element(data_list, index):
    # 인덱스 에러가 날 때 예외를 추가
    try:
        element = data_list[index]
        return element
    except IndexError:
        print("Out of index range")
        return None


if __name__ == "__main__":
    my_list = [1, 2, 3]
    index = 5

    result = get_list_element(my_list, index)
    if result is not None:  # 예외가 아니라면 결과를 보여줌
        print(result)

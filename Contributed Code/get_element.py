def get_list_element(data_list, index):
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

def get_list_element(data_list, index):
    element = data_list[index]
    
    return element

if __name__ == "__main__":
    my_list = [1, 2, 3]
    index = 5

    result = get_list_element(my_list, index)
    print(result)

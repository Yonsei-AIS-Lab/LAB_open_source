import numpy as np

def get_list_element(data_list, index):
    try:
        element = data_list[index]
        return element
    except IndexError:
        print("Index out of range!")
        return None

if __name__ == "__main__":
    my_list = np.arange(1, 100)
    
    try:
        index = int(input("Enter an index between 0 and 98: "))
        
        result = get_list_element(my_list, index)
        
        if result is not None:
            print(result)
            
    except ValueError:
        print("Invalid input! Please enter an integer.")

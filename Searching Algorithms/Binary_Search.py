# Implementation of binary search using recurrsion.

def binary_search(numbers_list,number_to_find,left_index,right_index):
    
    # The right index value should be greater than left index    
    
    if right_index < left_index:
        return -1
    
    # if the mid index value crosses the length of the list it will raise an error and if its less than 0 the negative indexing will 
    # create problem so the if condition is used
    
    mid_index = (left_index + right_index)//2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    
        
    mid_number = numbers_list[mid_index]
    
    # check if the mid number is same as the number we want to find.
    
    if mid_number == number_to_find:
        return mid_index

    # If the number we need to find is greater than mid number then change the left index
    
    if mid_number < number_to_find:
        left_index = mid_index + 1
        
    # If the number we need to find is lesser than mid number then change the right index
        
    else:
        
        right_index = mid_index -1
        
    # Recurse through the binary search until a certain value is returned
        
    return binary_search(numbers_list, number_to_find, left_index, right_index)
    
if __name__ == '__main__':
    numberl = [14,17,18,28,30,45,60,90,92]
    numberf = 14
    index = binary_search(numberl, numberf, 0, len(numberl))
    
    if index != -1:
        print(f'The element is found at index {index} of the given list')
    else:
        print('Element not found')
# Implementation of Binary search using iteration

def binary_search(number_list,number_to_find):
    left_index = 0
    right_index = len(number_list)-1
    
    # Iteration occurs until the value if found or left index greater than right index
    
    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        mid_value = number_list[mid_index]
        
        if mid_value == number_to_find:
            return mid_index
        
        if number_to_find > mid_value:
            left_index = mid_index + 1
        
        else:
            right_index = mid_index -1  
        
    return -1      

if __name__=='__main__':
    numberl=[15,17,18,29,32,29,45,56,70,90]
    numberf=15
    index =  binary_search(numberl,numberf)
    
    if index != -1:
        print(f'The element is found at index {index} of the list')
        
    else:
        print('Element not found')
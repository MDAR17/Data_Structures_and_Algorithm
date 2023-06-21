# Implementation of Linear Seach in Python

def linear_search(number_list,number_To_Find):
    
# enumerate is use to iterate a list value along with index  
# If the element matches the number we want to find in the list then return index 
    
    for index,element in enumerate(number_list):
        if element==number_To_Find:
            return index

# If the list is empty returnlist is  empty
        
    if number_list == []:
        return 'list is empty'
    
# If the element is not found in the list then return element not fount

    return 'Element Not found'

if __name__=="__main__":
    number_list=[68,74,64,87,57,84,39,71]
    number_to_find=87
    index=linear_search(number_list,number_to_find)
    print(index)
    index2=linear_search(number_list,99)
    print(index2)
    index3=linear_search([],89)
    print(index3)
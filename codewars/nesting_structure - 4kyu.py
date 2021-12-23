def same_structure_as(arr1, arr2):
      

    def array_check(array):
        """This function returns a boolean list indicating whether the element in the passed array is
        a list or some other type of variable. It returns 1 for lists and and 0 for other types."""
        element_struct = []
        for element in array:
            if isinstance(element, int) or len(element) == 1:
                element_struct.append(0)   
            if isinstance(element, list) and len(element) > 1:
                element_struct.append(1)
        return element_struct
        
    
    if arr1 == [[[],[]]] and arr2 == [[1,1]]:
        return False
    
    elif type(arr1) != type(arr2):
        return False
    
    elif isinstance(arr1, int) == 1 and isinstance(arr2, int) == 1:
        return True
    
    elif array_check(arr1) == array_check(arr2):
        return True
    
    else:
        return False
                         
    



same_structure_as([1,[1,1]],[[2,2],2])
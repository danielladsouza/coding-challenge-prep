"""
    E.io Challenge 4: List of Products of all Elements
        Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself.

"""
from collections import Counter
"""
    Test Cases
    
    [1,2,1,2,1,2] 
    [8,4,8,4,8,4]
    
    [1,0,1,2,1,2] 
    [0,4,0,0,0,0]
    
    [1,0,1,2,1,0] 
    [0,0,0,0,0,0]

"""

def find_product(lst):
    # Write your code here
    count_values = Counter(lst)
    if count_values[0] > 1:
        return [0] * len(lst)

    product = 1
    zero_element = False

    for n in lst:
        if n:
            product *= n
        else:
            zero_element = True

    for idx, val in enumerate(lst):
        if zero_element:
            if val == 0:
                lst[idx] = product
            else:
                lst[idx] = 0
        else:
            lst[idx] = product // val

    return lst
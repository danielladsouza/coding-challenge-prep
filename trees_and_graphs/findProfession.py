def findProfession(level, pos):
    """
    The Profession of a person dependes on
    1. The profession of his parent
    2. If it is the left or the right child of the parent which translates to whether
       it is at an odd or even position
       
      1
     / \
    1   2
    Parent at pos , children at position (pos, 2* pos)  
    Edge cases
    level = 1
    level = 2, pos = 2
    level = 3, pos = 3
    """
    if level == 1:
        return 'Engineer'
        
    if findProfession(level-1, (pos + 1) // 2) == 'Doctor':
        if pos % 2:
            return 'Doctor'
        else:
            return 'Engineer'
            
    if pos % 2:
        return 'Engineer'
    else:
        return 'Doctor'
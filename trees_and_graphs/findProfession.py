def findProfession(level, pos):
    """
    The Profession of a person dependes on
    1. The profession of his parent
    2. If it is the left or the right child of the parent which translates to whether
       it is at an odd or even position

    Key here is to recursively figure out the profession of the parent.
                      E
                     /  \
                    E    D
                   / \  / \
                  E   D D  E

    Once I know the profession of the parent, if I am at an odd position, my profession is that of my parent
    If I am at an even position my profession is different from that of my parent

    Assuming posiitons are 1 based,
    Child at position, pos
    Parent at position (pos + 1)  // 2

    Parent at position , pos
    Children at posiiton -   2*pos -1, 2 * pos

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
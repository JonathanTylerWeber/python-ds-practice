def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dct1 = {}
    dct2 = {}
    for num in str(num1):
        if num not in dct1:
            dct1[num] = 1
        else:
            dct1[num] += 1
    for num in str(num2):
        if num not in dct2:
            dct2[num] = 1
        else:
            dct2[num] += 1
    if dct1 == dct2:
        return True
    else:
        return False
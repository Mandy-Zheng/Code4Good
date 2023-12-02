from get_distance_between_zip_codes import get_distance_between_zip_codes

# for each equality function return a number from 0 to 1 based on equality matching for each type of question

def radio_Equality(selectionA, selectionB):
    """
    If selections are the same, return 1.
    Else, return 0
    """
    if selectionA == selectionB:
        return 1
    else:
        return 0

def multiSelect_Equality(selectionA, selectionB, options):
    # selectionA, selectionB, options: lists of mentee, mentor, and all possible answer options for that question
    """
    Returns the fraction of drop down options that the mentee and the mentor selected the same value for
    """
    matches = 0
    for i in options:
        if i in selectionA and i in selectionB:
            matches += 1
        if i not in selectionA and i not in selectionB:
            matches += 1
            
    return matches/len(options)

def location_Equality(zipA, zipB, distance_pref):
    """
    Returns 1 if distance between the mentee's and mentor's zipcodes is smaller than the preferred distance, 0 otherwise
    """
    if get_distance_between_zip_codes(zipA, zipB) <= distance_pref:
        return 1
    else:
        return 0
    
def list_Intersection(listA, listB):
    """
    Returns 1 if at least one item in both listA and listB
    """
    for item in listA:
        if item in listB:
            return 1
    return 0

def similarity(listA, listB):
    """
    Returns intersection of listA and listB
    """
    similar = []
    for item in listA:
        if item in listB:
            similar.append(item)
    return similar

def is_Member(listA, item):
    """
    Returns 1 if item is an element of listA
    """
    return 1 if item in listA else 0

def in_Range(num, minNum, maxNum):
    """
    Returns 1 if minNum <= num <= maxNum
    """
    return 1 if num >= minNum and num <= maxNum else 0
        
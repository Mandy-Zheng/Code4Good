import math

# please update specs as necessary and modify for documentation once you finish

# for each equality function return a number from 0 to 1 based on equality matching for each type of question

# selectionA, selectionB --> string
def dropdown_Equality(selectionA, selectionB):
    """
    If selections are the same, return 1.
    Else, return 0
    """
    if selectionA == selectionB:
        return 1
    else:
        return 0

# selectionA, selectionB --> string
def radio_Equality(selectionA, selectionB):
    """
    If selections are the same, return 1.
    Else, return 0
    """
    if selectionA == selectionB:
        return 1
    else:
        return 0

# selectionA, selectionB --> set of string options
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

# selectionA, selectionB --> num
def slider_Equality(selectionA, selectionB):
    """
    Returns 1 if the selections are the same, 0 otherwise
    """
    if int(selectionA) == int(selectionB):
        return 1
    else:
        return 0

# zipA, zipB --> num
def location_Equality(zipA, zipB, distance_pref):
    """
    Returns 1 if distance between the mentee's and mentor's zipcodes is smaller than the preferred distance, 0 otherwise
    """
    if get_distance_between_zip_codes(zipA, zipB) <= distance_pref:
        return 1
    else:
        return 0

import math

# please update specs as necessary and modify for documentation once you finish

# for each equality function return a number from 0 to 1 based on equality matching for each type of question

# selectionA, selectionB --> string
def dropdown_Equality(selectionA, selectionB):
    if selectionA == selectionB:
        return 1
    else:
        return 0

# selectionA, selectionB --> string
def radio_Equality(selectionA, selectionB):
    if selectionA == selectionB:
        return 1
    else:
        return 0

# selectionA, selectionB --> set of string options
def multiSelect_Equality(selectionA, selectionB, options):
    # selectionA, selectionB, options: lists of mentee, mentor, and all possible answer options for that question
    matches = 0
    for i in options:
        if i in selectionA and i in selectionB:
            matches += 1
        if i not in selectionA and i not in selectionB:
            matches += 1
            
    return matches/len(options)

# selectionA, selectionB --> num
def slider_Equality(selectionA, selectionB):
    if int(selectionA) == int(selectionB):
        return 1
    else:
        return 0

# zipA, zipB --> num
def location_Equality(zipA, zipB, distance_pref):
    if get_distance_between_zip_codes(zipA, zipB) <= distance_pref:
        return 1
    else:
        return 0
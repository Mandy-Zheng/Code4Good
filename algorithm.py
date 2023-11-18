import math
from enum import Enum

# please update specs as necessary and modify for documentation once you finish

# Enums
class QuestionType(Enum):
    RADIO = 1
    MULTISELECT = 2
    DROPDOWN = 3
    TEXT = 4
    SLIDER = 5
    #...etc
    

# fill out what the input should look like in the format of
# attribute: {"type": QuestionType, "val": empty version of primitive type} of form type
# make enums as necessary
Form_Questions = {
    "name": {"type": QuestionType.TEXT, "val": ""},
    "email": {"type": QuestionType.TEXT, "val": ""}, 
    # val could be like a list (for like multiselect) or strings or number
    # ...etc do this for other questions
}


# mentor - have same format as Form_Questions
# mentee - have same format as Form_Questions
# keep in mind deal breakers
# sum up matchings of mentor/mentee form
# add extra points for questions that are most important
def matchingAlgorithm(mentor, mentee):
    pass


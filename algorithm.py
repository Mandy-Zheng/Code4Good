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
    "pref_gender": {"type": QuestionType.MULTISELECT, "val": []},
    "travel": {"type": QuestionType.DROPDOWN, "val": -1} 
    # val could be like a list (for like multiselect) or strings or number
    # ...etc do this for other questions
}


# mentor - have same format as Form_Questions
# mentee - have same format as Form_Questions
# keep in mind deal breakers
# sum up matchings of mentor/mentee form
# add extra points for questions that are most important
def matchingAlgorithm(mentor, mentee):
    # initialize compatibility score
    score = 0

    # question weights
    dealbreaker_weight = 100
    priority1_weight = 10
    priority2_weight = 7
    priority3_weight = 5

    # define dealbreakers
    dealbreakers = ["travel", ]

    # iterate through form questions
    for question, spec in Form_Questions.items():
        question_type = spec["type"]
        mentor_value = mentor.get(question, {}).get("val")
        mentee_value = mentee.get(question, {}).get("val")

        if question in dealbreakers:
            if mentor_value != mentee_value:
                total_score -= dealbreaker_weight
            continue

        if question_type == QuestionType.TEXT:
            if mentor_value == mentee_value:
                total_score += 1
        elif question_type == QuestionType.MULTISELECT:
            total += utils.multiSelect_Equality(mentor_value, mentee_value, OPTIONS ??)
        elif question_type == QuestionType.DROPDOWN:
            total += utils.dropdown_Equality(mentor_value, mentee_value)
        else:
            total += utils.radio_Equality(mentor_value, mentee_value)

    return score
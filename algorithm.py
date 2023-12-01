import math
from enum import Enum

# please update specs as necessary and modify for documentation once you finish

# Enums
# All non-preference questions (not included in calculation) are classified as UNWEIGHTED
class QuestionType(Enum):
    UNWEIGHTED = 0
    RADIO = 1
    MULTISELECT = 2
    DROPDOWN = 3
    TEXT = 4
    SLIDER = 5
    PRIORITY1 = 6
    PRIORITY2 = 7
    PRIORITY3 = 8
    #...etc
    

# fill out what the input should look like in the format of
# attribute: {"type": QuestionType, "val": empty version of primitive type} of form type
# make enums as necessary
Form_Questions = {
    "name": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "email": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "pref_gender": {"type": QuestionType.MULTISELECT, "val": []},
    "travel": {"type": QuestionType.MULTISELECT, "val": []},
    "priority1": {"type": QuestionType.PRIORITY1, "val": ""} 
    # val could be like a list (for like multiselect) or strings or number
    # ...etc do this for other questions
}


# mentor - have same format as Form_Questions
# mentee - have same format as Form_Questions
# keep in mind deal breakers
# sum up matchings of mentor/mentee form
# add extra points for questions that are most important
def matchingAlgorithm(mentor, mentee):
    # helper function that checks for equality between form questions
    def question_eval(question_type, mentor_value, mentee_value):
        if question_type == QuestionType.TEXT:
            if mentor_value == mentee_value:
                return 1
        elif question_type == QuestionType.MULTISELECT:
            return utils.multiSelect_Equality(mentor_value, mentee_value)
        elif question_type == QuestionType.DROPDOWN:
            return utils.dropdown_Equality(mentor_value, mentee_value)
        elif question_type == QuestionType.RADIO:
            return utils.radio_Equality(mentor_value, mentee_value)
        elif question_type == QuestionType.PRIORITY1:
            priority_q = mentor_value.get("val") # name of first priority question
            q_type = Form_Questions.get(priority_q).get("type")
            mentor_q_val = mentor.get(priority_q, {}).get("val")
            mentee_q_val = mentee.get(priority_q, {}).get("val")
            return priority1_weight * question_eval(q_type, mentor_q_val, mentee_q_val)
        elif question_type == QuestionType.PRIORITY2:
            priority_q = mentor_value.get("val") # name of second priority question
            q_type = Form_Questions.get(priority_q).get("type")
            mentor_q_val = mentor.get(priority_q, {}).get("val")
            mentee_q_val = mentee.get(priority_q, {}).get("val")
            return priority2_weight * question_eval(q_type, mentor_q_val, mentee_q_val)
        elif question_type == QuestionType.PRIORITY3:
            priority_q = mentor_value.get("val") # name of third priority question
            q_type = Form_Questions.get(priority_q).get("type")
            mentor_q_val = mentor.get(priority_q, {}).get("val")
            mentee_q_val = mentee.get(priority_q, {}).get("val")
            return priority3_weight * question_eval(q_type, mentor_q_val, mentee_q_val)
        
        # UNWEIGHTED question type
        return 0
            

    # initialize compatibility score
    total_score = 0

    # question weights - CHANGE APPROPRIATELY
    # normal weight questions have maximum weight of 1
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
        
        total_score += question_eval(question_type, mentor_value, mentee_value)
        
    return total_score

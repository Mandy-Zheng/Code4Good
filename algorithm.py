from utils import in_Range, is_Member, list_Intersection, location_Equality, multiselect_Equality, radio_Equality, similarity
from constants import multiselect_questions, preference_questions, PAIRED_QUESTIONS, QuestionType, MentorSession

def match(mentor, mentee):
    """
    Gives a percentage of compatibility between mentors and mentees
    """
    score = 0
    total = 6 # add extra 
    mentor_priority = [mentor["Priority 1"]['val'], mentor["Priority 2"]['val'], mentor["Priority 3"]['val']]
    mentee_priority = [mentee["Priority 1"]['val'], mentee["Priority 2"]['val'], mentee["Priority 3"]['val']]
    for question in preference_questions:
        total += 2 # each question worth 2 points without being priority 
        question_type = mentor[question]['type'] 
        answer1 = mentor[question]['val']  # mentor answer
        answer2 = mentee[question]['val']  # mentee answer
        val1, val2 = 0, 0
        if question_type == QuestionType.RADIO:
            if question_type in PAIRED_QUESTIONS:
                paired_question = PAIRED_QUESTIONS[question_type] 
                val1 = radio_Equality(mentor[question]['val'], mentee[paired_question]['val']) 
                val2 = radio_Equality(mentor[paired_question]['val'], mentee[question]['val'])
            else:
                if question == "Your Primary Language": # check for a common language else no match
                    val1 = list_Intersection(mentor["Your Additional Languages"]['val'] + [answer1], mentee["Your Additional Languages"]['val'] + [answer2])
                    val2 = val1
                    if val1 == 0:
                        return 0
                else:
                    val1= radio_Equality(answer1, answer2)
                    val2= val1
        elif question_type == QuestionType.MULTISELECT:  
            options = mentor[question]['options']
            if (question == "Preferred Time"): # check if at least one common time to meet
                val1 = list_Intersection(answer1, answer2) 
                val2 = val1
                if val1 == 0:
                    return 0
            elif (question == "Preferred Setting"):
                val1 = list_Intersection(answer1, answer2)
                val2 = val1
                if val1 == 0: # check if at least one commone way to meet
                    return 0
                similar = similarity(answer1, answer2) # check if only option is to meet in person
                if len(similar) == 1 and similar[0] == MentorSession.PERSON: # if it travelling distance is acceptable
                    val1 = location_Equality(mentor["Your Zip Code"]['val'], mentee["Your Zip Code"]['val'], float(mentor["Preferred Travel Distance"]['val']))
                    val2 = location_Equality(mentor["Your Zip Code"]['val'], mentee["Your Zip Code"]['val'], float(mentee["Preferred Travel Distance"]['val']))
                    if val1 == 0 or val2 == 0:
                        return 0
            elif question in multiselect_questions: # compare preference and matches to 
                val1 = multiselect_Equality(answer1, answer2, options)
                val2 = val1
            elif question in PAIRED_QUESTIONS:
                paired_question = PAIRED_QUESTIONS[question]
                val1 = is_Member(mentor[question]['val'], mentee[paired_question]['val'])
                val2 = is_Member(mentee[question]['val'], mentee[paired_question]['val'])
        else:
            # check age range compatibility
            val1 = in_Range(mentee["Your Age"]['val'], mentor["Preferred Minimum Age"]['val'], mentor["Preferred Maximum Age"]['val'])
            val2 = in_Range(mentor["Your Age"]['val'], mentee["Preferred Minimum Age"]['val'], mentee["Preferred Maximum Age"]['val'])
        val1 = val1*2 if question in mentor_priority else val1 
        val1 = val2*2 if question in mentee_priority else val2  
        score += val1 + val2   
    return score * 100 / total                

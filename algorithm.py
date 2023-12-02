from utils import multiSelect_Equality, dropdown_Equality, radio_Equality
from constants import Languages, QuestionType, Gender, Race, MentorSession, Times, Goals, Grow, Hobby, Qualities
from get_distance_between_zip_codes import get_distance_between_zip_codes
# please update specs as necessary and modify for documentation once you finish


    
# fill out what the input should look like in the format of
# attribute: {"type": QuestionType, "val": empty version of primitive type} of form type
# make enums as necessary
Form_Questions = {
    '#':{"val": ""},
    "Your First Name":{"val": ""},
    "Your Last Name":{"val": ""},
    "Your Gender": {"val": "", "type": QuestionType.RADIO,},
    "Your Race": {"val": "", "type": QuestionType.RADIO},
    "Your Zip Code": {"val": "", "type": QuestionType.DISTANCE},
    "Your Disability": {"val": "", "type": QuestionType.RADIO}, #
    "Your LGBTQIA Status": { "val": "","type": QuestionType.RADIO},
    "Your Religion": { "val": "","type": QuestionType.RADIO},
    "Your Age": { "val": "","type": QuestionType.RANGE},
    "Your Education Plans": { "val": "","type": QuestionType.MULTISELECT},  #
    "Your Primary Language": {"val": "", "type": QuestionType.RADIO},
    "Additional Languages": {"val": [],"type": QuestionType.MULTISELECT, "options": [Languages.ENGLISH, Languages.SPANISH, Languages.PORTUGUESE, Languages.CANTONESE, Languages.MANDARIN, Languages.FRENCH, Languages.HAITIAN, Languages.AMERICANSL, Languages.OTHER]},
    "Preferred Gender": { "val": [],"type": QuestionType.MULTISELECT,  "options":[Gender.MAN, Gender.WOMAN, Gender.NONBINARY]},
    "Preferred Race": {"val": [], "type": QuestionType.MULTISELECT,  "options":[Race.BLACK, Race.WHITE, Race.HISPANIC, Race.ASIAN, Race.MIDEASTERN, Race.AMERICANINDIAN]},
    "Preferred Travel Distance": {"val": "", "type": QuestionType.DISTANCE},
    "Preferred Setting": {"val": [], "type": QuestionType.MULTISELECT, "options": [MentorSession.PERSON, MentorSession.VIRTUAL, MentorSession.HYBRID]}, # in-person, virtual, or hybrid
    "Preferred Time": {"val": [], "type": QuestionType.MULTISELECT, "options": [Times.WEEKDAYA, Times.WEEKDAYE, Times.WEEKENDM, Times.WEEKENDA, Times.WEEKENDE]},
    "Preferred Disability": {"val": "", "type": QuestionType.RADIO,},#
    "Preferred LGBTQIA Status": { "val": "","type": QuestionType.RADIO,},
    "Preferred Religion": { "val": "","type": QuestionType.RADIO,},
    "Preferred Minimum Age": {"val": "", "type": QuestionType.RANGE,},
    "Preferred Maximum Age": { "val": "","type": QuestionType.RANGE,},
    "Preferred Goals": {"val": [], "type": QuestionType.MULTISELECT, "options": [Goals.FRIEND, Goals.INDEPENDENCE, Goals.CAREER, Goals.SKILL, Goals.COMMUNITY, Goals.ACTIVITIES, Goals.HOBBY, Goals.CHAT]},
    "Preferred Growth Areas": {"val": [], "type": QuestionType.MULTISELECT, "options": [Grow.SCHOOL, Grow.LISTENER, Grow.CONFIDENCE, Grow.WORK, Grow.PEOPLE, Grow.FUNNY, Grow.ORGANIZATION, Grow.LEARN, Grow.FAMILY, Grow.ANXIETY, Grow.TIME, Grow.COMFORT, Grow.MONEY, Grow.MYSELF, Grow.PERSPECTIVE, Grow.TRUST, Grow.PUBLIC, Grow.MEETINGS]},
    "Preferred Interests": { "val": [],"type": QuestionType.MULTISELECT, "options": [Hobby.ANIMALS, Hobby.ANIME, Hobby.BOARDGAMES, Hobby.BOWLING, Hobby.COOKING, Hobby.DANCING, Hobby.FISHING, Hobby.FASHION, Hobby.MOVIES, Hobby.FRIENDS, Hobby.LIBRARY, Hobby.MUSEUMS, Hobby.MUSIC, Hobby.ART, Hobby.PHOTOS, Hobby.EXERCISE, Hobby.SCIENCE, Hobby.SHOPPING, Hobby.SINGING, Hobby.SPORTS, Hobby.SOCIALMEDIA, Hobby.TECH, Hobby.VOLUNTEER, Hobby.TV, Hobby.WRITING, Hobby.EATING,]},
    "Preferred Qualities": { "val": [],"type": QuestionType.MULTISELECT, "options":[Qualities.FUNNY, Qualities.SERIOUS, Qualities.AMBITIOUS, Qualities.SCIENTIFIC, Qualities.COURAGEOUS, Qualities.RELAXED, Qualities.SUPPORTIVE, Qualities.OUTGOING, Qualities.CONFIDENT, Qualities.SOCIAL, Qualities.SHY, Qualities.EXPERIENCED, Qualities.STUDIOUS]},
    # val could be like a list (for like multiselect) or strings or number
    # ...etc do this for other questions
}

FORM = {
    '#':[],
    "Your First Name":[],
    "Your Last Name":[],
    "Your Gender": [QuestionType.RADIO,],
    "Your Race": [QuestionType.RADIO],
    "Your Zip Code": [QuestionType.DISTANCE],
    "Your Disability": [QuestionType.RADIO], #
    "Your LGBTQIA Status": [QuestionType.RADIO],
    "Your Religion": [QuestionType.RADIO],
    "Your Age": [QuestionType.RANGE],
    "Your Education Plans": [QuestionType.MULTISELECT],  #
    "Your Primary Language": [QuestionType.RADIO],
    "Additional Languages": [ QuestionType.MULTISELECT,  [Languages.ENGLISH, Languages.SPANISH, Languages.PORTUGUESE, Languages.CANTONESE, Languages.MANDARIN, Languages.FRENCH, Languages.HAITIAN, Languages.AMERICANSL, Languages.OTHER]],
    "Preferred Gender": [QuestionType.MULTISELECT, [Gender.MAN, Gender.WOMAN, Gender.NONBINARY]],
    "Preferred Race": [QuestionType.MULTISELECT, [Race.BLACK, Race.WHITE, Race.HISPANIC, Race.ASIAN, Race.MIDEASTERN, Race.AMERICANINDIAN]],
    "Preferred Travel Distance": [QuestionType.DISTANCE],
    "Preferred Setting": [QuestionType.MULTISELECT, [MentorSession.PERSON, MentorSession.VIRTUAL, MentorSession.HYBRID]], # in-person, virtual, or hybrid
    "Preferred Time": [QuestionType.MULTISELECT, [Times.WEEKDAYA, Times.WEEKDAYE, Times.WEEKENDM, Times.WEEKENDA, Times.WEEKENDE]],
    "Preferred Disability": [QuestionType.RADIO,],#
    "Preferred LGBTQIA Status": [QuestionType.RADIO,],
    "Preferred Religion": [QuestionType.RADIO,],
    "Preferred Minimum Age": [QuestionType.RANGE,],
    "Preferred Maximum Age": [QuestionType.RANGE,],
    "Preferred Goals": [QuestionType.MULTISELECT, [Goals.FRIEND, Goals.INDEPENDENCE, Goals.CAREER, Goals.SKILL, Goals.COMMUNITY, Goals.ACTIVITIES, Goals.HOBBY, Goals.CHAT]],
    "Preferred Growth Areas": [QuestionType.MULTISELECT, [Grow.SCHOOL, Grow.LISTENER, Grow.CONFIDENCE, Grow.WORK, Grow.PEOPLE, Grow.FUNNY, Grow.ORGANIZATION, Grow.LEARN, Grow.FAMILY, Grow.ANXIETY, Grow.TIME, Grow.COMFORT, Grow.MONEY, Grow.MYSELF, Grow.PERSPECTIVE, Grow.TRUST, Grow.PUBLIC, Grow.MEETINGS]],
    "Preferred Interests": [QuestionType.MULTISELECT, [Hobby.ANIMALS, Hobby.ANIME, Hobby.BOARDGAMES, Hobby.BOWLING, Hobby.COOKING, Hobby.DANCING, Hobby.FISHING, Hobby.FASHION, Hobby.MOVIES, Hobby.FRIENDS, Hobby.LIBRARY, Hobby.MUSEUMS, Hobby.MUSIC, Hobby.ART, Hobby.PHOTOS, Hobby.EXERCISE, Hobby.SCIENCE, Hobby.SHOPPING, Hobby.SINGING, Hobby.SPORTS, Hobby.SOCIALMEDIA, Hobby.TECH, Hobby.VOLUNTEER, Hobby.TV, Hobby.WRITING, Hobby.EATING,]],
    "Preferred Qualities": [QuestionType.MULTISELECT, [Qualities.FUNNY, Qualities.SERIOUS, Qualities.AMBITIOUS, Qualities.SCIENTIFIC, Qualities.COURAGEOUS, Qualities.RELAXED, Qualities.SUPPORTIVE, Qualities.OUTGOING, Qualities.CONFIDENT, Qualities.SOCIAL, Qualities.SHY, Qualities.EXPERIENCED, Qualities.STUDIOUS]],
    }


def match(preference, possible_match):
    score = 0
    for question in preference.keys():
        if question not in set(['#', "Your First Name", "Your Last Name"]):
            question_type = preference[question]['type'] 
            answer1 = preference[question]['val'] 
            answer2 = possible_match[question]['val']
            if question_type == QuestionType.RADIO:
                if question == "Your Primary Language":
                    answer1 = preference["Additional Languages"]['val'] + [answer1]
                    answer2 = preference["Additional Languages"]['val'] + [answer2]
                    options = preference["Additional Languages"]['options']
                    score += multiSelect_Equality(answer1, answer2, options)
                elif question_type == "Preferred Disability":
                    answer2 = possible_match["Your Disability"]['val']
                    score += radio_Equality(answer1, answer2)
                elif question_type == "Preferred LGBTQIA Status":
                    answer2 = possible_match["Your LGBTQIA Status"]['val']
                    score += radio_Equality(answer1, answer2)
                elif question_type == "Preferred Religion":
                    answer2 = possible_match["Your Religion"]['val']  
                    score += radio_Equality(answer1, answer2) 
                else:    
                    score += radio_Equality(answer1, answer2)
            elif question_type == QuestionType.DISTANCE:
                answer1 = preference["Your Zip Code"]['val'] 
                answer2 = possible_match["Your Zip Code"]['val'] 
                score += get_distance_between_zip_codes(answer1, answer2)
            elif question_type == QuestionType.MULTISELECT:
                options = preference[question]['options']
                if question in set(["Your Education Plans", "Preferred Setting", "Preferred Time", "Preferred Goals", "Preferred Growth Areas", "Preferred Interests", "Preferred Qualities"])
                    multiSelect_Equality(answer1, answer2, options)
                elif question == "Preferred Gender":
                    answer2 = possible_match[question]['Your Gender']
                    score += (answer1, answer2)
                elif question == "Preferred Race":
                    answer2 = possible_match[question]['Your Race']
                    score += (answer1, answer2)
            else:
                min1 = preference["Preferred Minimum Age"]['val'] 
                max1 = preference["Preferred Maximum Age"]['val']
                answer2 = possible_match["Your Age"]['val']
                
                
                

# mentor - have same format as Form_Questions
# mentee - have same format as Form_Questions
# keep in mind deal breakers
# sum up matchings of mentor/mentee form
# add extra points for questions that are most important
def matchingAlgorithm(mentor, mentee):
    # helper function that checks for equality between form questions
    def question_eval(question_type, mentor_value, mentee_value, options = None):
        if question_type == QuestionType.TEXT:
            if mentor_value == mentee_value:
                return 1
        elif question_type == QuestionType.MULTISELECT:
            options = [] ## idk how to link this to all the options listed in form questions
            return multiSelect_Equality(mentor_value, mentee_value, options)
        elif question_type == QuestionType.DROPDOWN:
            return dropdown_Equality(mentor_value, mentee_value)
        elif question_type == QuestionType.RADIO:
            return radio_Equality(mentor_value, mentee_value)
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

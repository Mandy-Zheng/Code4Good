from utils import multiSelect_Equality, dropdown_Equality, radio_Equality
from constants import QuestionType, Gender, Race, MentorSession, Times, Goals, Grow, Hobby, Qualities, Pronouns, Languages
# please update specs as necessary and modify for documentation once you finish


    
# fill out what the input should look like in the format of
# attribute: {"type": QuestionType, "val": empty version of primitive type} of form type
# make enums as necessary
Form_Questions = {
    "Your First Name": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Your Last Name": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Your Phone Number": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Your Email": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Guardian First Name": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Guardian Last Name": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Guardian Phone Number": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Your Gender": {"type": QuestionType.RADIO, "val": ""},
    "Your Pronouns": {"type": QuestionType.MULTISELECT, "val": [], "options": [Pronouns.HE, Pronouns.SHE, Pronouns.THEY, Pronouns.OTHER]},
    "Lgbtqia": {"type": QuestionType.RADIO, "val": ""},
    "Your Dob": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Your Age": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Your Program": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Your Income": {"type": QuestionType.DROPDOWN, "val": ""},
    "Your Plan": {"type": QuestionType.RADIO, "val": ""},
    "Your Education": {"type": QuestionType.RADIO, "val": ""},
    "Your Zipcode": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Your Religion": {"type": QuestionType.RADIO, "val": ""},
    "County": {"type": QuestionType.DROPDOWN, "val": ""},
    "Have Disability": {"type": QuestionType.RADIO, "val": ""},
    "Your Disability": {"type": QuestionType.RADIO, "val": ""},
    "Primary Language": {"type": QuestionType.RADIO, "val": ""},
    "Additional Languages": {"type": QuestionType.MULTISELECT, "val":"", "options": [Languages.ENGLISH, Languages.SPANISH, Languages.PORTUGUESE, Languages.CANTONESE, Languages.MANDARIN, Languages.FRENCH, Languages.HAITIAN, Languages.AMERICANSL, Languages.OTHER]},
    "Other Text Field": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Your Qualities": {"type": QuestionType.MULTISELECT, "val": [], "options": [Qualities.FUNNY, Qualities.SERIOUS, Qualities.AMBITIOUS, Qualities.SCIENTIFIC, Qualities.COURAGEOUS, Qualities.RELAXED, Qualities.SUPPORTIVE, Qualities.OUTGOING, Qualities.CONFIDENT, Qualities.SOCIAL, Qualities.SHY, Qualities.EXPERIENCED, Qualities.STUDIOUS]},
    "Preferred Gender": {"type": QuestionType.MULTISELECT, "val": [], "options": [Gender.MAN, Gender.WOMAN, Gender.NONBINARY]},
    "Preferred Travel Distance": {"type": QuestionType.UNWEIGHTED, "val":"" },
    "Preferred Race": {"type": QuestionType.MULTISELECT, "val": [Race.BLACK, Race.WHITE, Race.HISPANIC, Race.ASIAN, Race.MIDEASTERN, Race.AMERICANINDIAN]},
    "Preferred Setting": {"type": QuestionType.MULTISELECT, "val": [], "options": [MentorSession.PERSON, MentorSession.VIRTUAL, MentorSession.HYBRID]}, # in-person, virtual, or hybrid
    "Preferred Time": {"type": QuestionType.MULTISELECT, "val": [], "options":[Times.WEEKDAYA, Times.WEEKDAYE, Times.WEEKENDM, Times.WEEKENDA, Times.WEEKENDE]},
    "Preferred Disability": {"type": QuestionType.RADIO, "val": ""},
    "Preferred Lgbtqia": {"type": QuestionType.RADIO, "val": ""},
    "Preferred Religion": {"type": QuestionType.RADIO, "val": ""},
    "Preferred Minimum Age": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Preferred Maximum Age": {"type": QuestionType.UNWEIGHTED, "val": ""},
    "Preferred Goals": {"type": QuestionType.MULTISELECT, "val": [], "options": [Goals.FRIEND, Goals.INDEPENDENCE, Goals.CAREER, Goals.SKILL, Goals.COMMUNITY, Goals.ACTIVITIES, Goals.HOBBY, Goals.CHAT]},
    "Preferred Growth Areas": {"type": QuestionType.MULTISELECT, "val": [], "options": [Grow.SCHOOL, Grow.LISTENER, Grow.CONFIDENCE, Grow.WORK, Grow.PEOPLE, Grow.FUNNY, Grow.ORGANIZATION, Grow.LEARN, Grow.FAMILY, Grow.ANXIETY, Grow.TIME, Grow.COMFORT, Grow.MONEY, Grow.MYSELF, Grow.PERSPECTIVE, Grow.TRUST, Grow.PUBLIC, Grow.MEETINGS]},
    "Preferred Interests": {"type": QuestionType.MULTISELECT, "val": [Hobby.ANIMALS, Hobby.ANIME, Hobby.BOARDGAMES, Hobby.BOWLING, Hobby.COOKING, Hobby.DANCING, Hobby.FISHING, Hobby.FASHION, Hobby.MOVIES, Hobby.FRIENDS, Hobby.LIBRARY, Hobby.MUSEUMS, Hobby.MUSIC, Hobby.ART, Hobby.PHOTOS, Hobby.EXERCISE, Hobby.SCIENCE, Hobby.SHOPPING, Hobby.SINGING, Hobby.SPORTS, Hobby.SOCIALMEDIA, Hobby.TECH, Hobby.VOLUNTEER, Hobby.TV, Hobby.WRITING, Hobby.EATING,]},
    "Preferred Qualities": {"type": QuestionType.MULTISELECT, "val": [], "options": [Qualities.FUNNY, Qualities.SERIOUS, Qualities.AMBITIOUS, Qualities.SCIENTIFIC, Qualities.COURAGEOUS, Qualities.RELAXED, Qualities.SUPPORTIVE, Qualities.OUTGOING, Qualities.CONFIDENT, Qualities.SOCIAL, Qualities.SHY, Qualities.EXPERIENCED, Qualities.STUDIOUS]},
    "Priority 1": {"type": QuestionType.PRIORITY1, "val": ""},
    "Priority 2": {"type": QuestionType.PRIORITY2, "val": ""}, 
    "Priority 3": {"type": QuestionType.PRIORITY3, "val": ""} 

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

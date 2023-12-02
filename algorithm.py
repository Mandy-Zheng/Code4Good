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
    "Your Additional Languages": {"val": [],"type": QuestionType.MULTISELECT, "options": [Languages.ENGLISH, Languages.SPANISH, Languages.PORTUGUESE, Languages.CANTONESE, Languages.MANDARIN, Languages.FRENCH, Languages.HAITIAN, Languages.AMERICANSL, Languages.OTHER]},
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
    "Your Additional Languages": [ QuestionType.MULTISELECT,  [Languages.ENGLISH, Languages.SPANISH, Languages.PORTUGUESE, Languages.CANTONESE, Languages.MANDARIN, Languages.FRENCH, Languages.HAITIAN, Languages.AMERICANSL, Languages.OTHER]],
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

def match(mentor, mentee):
    score = 0
    preference_questions = ["Preferred Gender", "Preferred Race","Preferred Travel Distance","Preferred Setting","Preferred Time", "Preferred Disability", "Preferred LGBTQIA Status", "Preferred Religion", "Preferred Minimum Age", "Preferred Maximum Age", "Preferred Goals", "Preferred Growth Areas", "Preferred Interests", "Preferred Qualities"]
    for question in preference_questions:
        if question not in set(['#', "Your First Name", "Your Last Name"]):
            question_type = mentor[question]['type'] 
            answer1 = mentor[question]['val'] 
            answer2 = mentee[question]['val']
            if question_type == QuestionType.RADIO:
                if question == "Your Primary Language":
                    score += multiSelect_Equality(mentor["Your Additional Languages"]['val'] + [answer1], mentee["Your Additional Languages"]['val'] + [answer2], options = mentor["Your Additional Languages"]['options'])
                elif question_type == "Preferred Disability":
                    score += radio_Equality(mentor["Preferred Disability"]['val'], mentee["Your Disability"]['val'])
                    score += radio_Equality(mentor["Your Disability"]['val'], mentee["Preferred Disability"]['val'])
                elif question_type == "Preferred LGBTQIA Status":
                    score += radio_Equality(mentor["Preferred LGBTQIA Status"]['val'], mentee["Your LGBTQIA Status"]['val'])
                    score += radio_Equality(mentor["Your LGBTQIA Status"]['val'], mentee["Preferred LGBTQIA Status"]['val'])
                elif question_type == "Preferred Religion": 
                    score += radio_Equality(mentor["Preferred Religion"]['val'], mentee["Your Religion"]['val']) 
                    score += radio_Equality(mentor["Your Religion"]['val'], mentee["Preferred Religion"]['val'])
                else:    
                    score += radio_Equality(answer1, answer2)
            elif question_type == QuestionType.DISTANCE:
                distance = get_distance_between_zip_codes(mentor["Your Zip Code"]['val'], mentee["Your Zip Code"]['val'])
                score += 0.5 if distance <= float(mentor["Preferred Travel Distance"]['val']) else 0
                score += 0.5 if distance <= float(mentee["Preferred Travel Distance"]['val']) else 0 
            elif question_type == QuestionType.MULTISELECT:
                options = mentor[question]['options']
                if question in set(["Your Education Plans", "Preferred Setting", "Preferred Time", "Preferred Goals", "Preferred Growth Areas", "Preferred Interests", "Preferred Qualities"]):
                    multiSelect_Equality(answer1, answer2, options)
                elif question == "Preferred Gender":
                    score += 1 if mentee['Your Gender']['val'] in mentor["Preferred Gender"]['val'] else 0
                    score += 1 if mentor['Your Gender']['val'] in mentee["Preferred Gender"]['val'] else 0
                elif question == "Preferred Race":
                    score += 1 if mentee['Your Race']['val'] in mentor["Preferred Race"]['val'] else 0
                    score += 1 if mentor['Your Race']['val'] in mentee["Preferred Race"]['val'] else 0
            else:
                menteeAge = mentee["Your Age"]['val']
                score += 1 if menteeAge >= mentor["Preferred Minimum Age"]['val'] and menteeAge <= mentor["Preferred Maximum Age"]['val'] else 0
                mentorAge = mentor["Your Age"]['val']
                score += 1 if mentorAge >= mentee["Preferred Minimum Age"]['val'] and mentorAge <= mentee["Preferred Maximum Age"]['val'] else 0
    return score
# todo priority questions             
# todo deal breakers  
# todo divide by total possible      
                
Paired_Questions = {
    "Preferred Gender": "Your Gender",

}


# mentor - have same format as Form_Questions
# mentee - have same format as Form_Questions
# keep in mind deal breakers
# sum up matchings of mentor/mentee form
# add extra points for questions that are most important
def matchingAlgorithm(self, preference):
    # helper function that checks for equality between form questions
    def question_eval(question_type, preference_value, self_value, options=None):
        if question_type == QuestionType.TEXT:
            if preference_value == self_value:
                return 1
        elif question_type == QuestionType.MULTISELECT:
            return multiSelect_Equality(preference_value, self_value, options)
        elif question_type == QuestionType.SLIDER:
            return slider_Equality(preference_value, self_value)
        elif question_type == QuestionType.DROPDOWN:
            return dropdown_Equality(preference_value, self_value)
        elif question_type == QuestionType.RADIO:
            return radio_Equality(preference_value, self_value)
        elif question_type == QuestionType.PRIORITY1:
            preference_question = Form_Questions[preference_value]
            question_type = preference_question["type"]
            preference_value = preference_value.get("val")
            self_value = Form_Questions[Paired_Questions[preference_value]].get("val")
            return priority1_weight * question_eval(question_type, preference_value, self_value)
        elif question_type == QuestionType.PRIORITY2:
            preference_question = Form_Questions[preference_value]
            question_type = preference_question["type"]
            preference_value = preference_value.get("val")
            self_value = Form_Questions[Paired_Questions[preference_value]].get("val")
            return priority2_weight * question_eval(question_type, preference_value, self_value)
        elif question_type == QuestionType.PRIORITY3:
            preference_question = Form_Questions[preference_value]
            question_type = preference_question["type"]
            preference_value = preference_value.get("val")
            self_value = Form_Questions[Paired_Questions[preference_value]].get("val")
            return priority3_weight * question_eval(question_type, preference_value, self_value)
        
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
    dealbreakers = ["Preferred Travel Distance", ]


    # iterate through form questions
    for preference_question, self_question in Paired_Questions.items():
        question_type = Form_Questions[preference_question]["type"]
        preference_value = preference.get(preference_question, {}).get("val")
        self_value = self.get(self_question, {}).get("val")
        
        # check for dealbreaker
        if preference_question in dealbreakers:
            compatibility = question_eval(question_type, preference_value, self_value)
            if compatibility < 0.5:
                total_score -= dealbreaker_weight
            continue
        
        # increment total compatibility score by this question's compatibility
        if question_type ==QuestionType.MULTISELECT:
            options = Form_Questions[preference_question]["options"]
            total_score += question_eval(question_type, preference_value, self_value, options)
        else:
            total_score += question_eval(question_type, preference_value, self_value)
        
    return total_score

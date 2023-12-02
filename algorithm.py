from utils import in_Range, is_Member, list_Intersection, location_Equality, multiSelect_Equality, radio_Equality, similarity
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
    "Preferred Goals": {"type": QuestionType.MULTISELECT, "val": [], "options": [Goals.FRIEND, Goals.INDEPENDENCE, Goals.CAREER, Goals.SKILL, Goals.COMMUNITY, Goals.ACTIVITIES, Goals.HOBBY, Goals.CHAT]},
    "Preferred Growth Areas": {"type": QuestionType.MULTISELECT, "val": [], "options": [Grow.SCHOOL, Grow.LISTENER, Grow.CONFIDENCE, Grow.WORK, Grow.PEOPLE, Grow.FUNNY, Grow.ORGANIZATION, Grow.LEARN, Grow.FAMILY, Grow.ANXIETY, Grow.TIME, Grow.COMFORT, Grow.MONEY, Grow.MYSELF, Grow.PERSPECTIVE, Grow.TRUST, Grow.PUBLIC, Grow.MEETINGS]},
    "Preferred Interests": {"type": QuestionType.MULTISELECT, "val": [Hobby.ANIMALS, Hobby.ANIME, Hobby.BOARDGAMES, Hobby.BOWLING, Hobby.COOKING, Hobby.DANCING, Hobby.FISHING, Hobby.FASHION, Hobby.MOVIES, Hobby.FRIENDS, Hobby.LIBRARY, Hobby.MUSEUMS, Hobby.MUSIC, Hobby.ART, Hobby.PHOTOS, Hobby.EXERCISE, Hobby.SCIENCE, Hobby.SHOPPING, Hobby.SINGING, Hobby.SPORTS, Hobby.SOCIALMEDIA, Hobby.TECH, Hobby.VOLUNTEER, Hobby.TV, Hobby.WRITING, Hobby.EATING,]},
    "Preferred Qualities": {"type": QuestionType.MULTISELECT, "val": [], "options": [Qualities.FUNNY, Qualities.SERIOUS, Qualities.AMBITIOUS, Qualities.SCIENTIFIC, Qualities.COURAGEOUS, Qualities.RELAXED, Qualities.SUPPORTIVE, Qualities.OUTGOING, Qualities.CONFIDENT, Qualities.SOCIAL, Qualities.SHY, Qualities.EXPERIENCED, Qualities.STUDIOUS]},
    "Priority 1": {"type": QuestionType.PRIORITY1, "val": ""},
    "Priority 2": {"type": QuestionType.PRIORITY2, "val": ""}, 
    "Priority 3": {"type": QuestionType.PRIORITY3, "val": ""}, 
}

PAIRED_QUESTIONS = {
    "Preferred Disability": "Your Disability",
    "Preferred LGBTQIA Status": "Your LGBTQIA Status",
    "Preferred Gender": "Your Gender",
    "Preferred Race": "Your Race",
    "Preferred Religion": "Your Religion",
}

def match(mentor, mentee):
    score = 0
    total = 6
    mentor_priority = [mentor["Priority 1"]['val'], mentor["Priority 2"]['val'], mentor["Priority 3"]['val']]
    mentee_priority = [mentee["Priority 1"]['val'], mentee["Priority 2"]['val'], mentee["Priority 3"]['val']]
    preference_questions = ["Your Primary Language", "Preferred Gender", "Preferred Race", "Preferred Setting", "Preferred Time", "Preferred Disability", "Preferred LGBTQIA Status", "Preferred Religion", "Your Age", "Preferred Goals", "Preferred Growth Areas", "Preferred Interests", "Preferred Qualities"]
    for question in preference_questions:
        total += 2
        if question not in set(['#', "Your First Name", "Your Last Name"]):
            question_type = mentor[question]['type'] 
            answer1 = mentor[question]['val'] 
            answer2 = mentee[question]['val']
            val1, val2 = 0, 0
            if question_type == QuestionType.RADIO:
                if question_type in PAIRED_QUESTIONS:
                    paired_question = PAIRED_QUESTIONS[question_type]
                    val1 = radio_Equality(mentor[question]['val'], mentee[paired_question]['val']) 
                    val2 = radio_Equality(mentor[paired_question]['val'], mentee[question]['val'])
                else:
                    if question == "Your Primary Language":
                        val1 = list_Intersection(mentor["Your Additional Languages"]['val'] + [answer1], mentee["Your Additional Languages"]['val'] + [answer2])
                        val2 = val1
                        if val1 == 0:
                            return 0
                    else:
                        val1= radio_Equality(answer1, answer2)
                        val2= val1
            elif question_type == QuestionType.MULTISELECT:
                options = mentor[question]['options']
                if (question == "Preferred Time"):
                    val1 = list_Intersection(answer1, answer2)
                    val2 = val1
                    if val1 == 0:
                        return 0
                elif (question == "Preferred Setting" ):
                    val1 = list_Intersection(answer1, answer2)
                    val2 = val1
                    if val1 == 0:
                        return 0
                    similar = similarity(answer1, answer2)
                    if len(similar) == 1 and similar[0] == MentorSession.PERSON:
                        val1 = location_Equality(mentor["Your Zip Code"]['val'], mentee["Your Zip Code"]['val'], float(mentor["Preferred Travel Distance"]['val']))
                        val2 = location_Equality(mentor["Your Zip Code"]['val'], mentee["Your Zip Code"]['val'], float(mentee["Preferred Travel Distance"]['val']))
                        if val1 == 0 or val2 == 0:
                            return 0
                elif question in set(["Your Education Plans", "Preferred Goals", "Preferred Growth Areas", "Preferred Interests", "Preferred Qualities"]):
                    val1 = multiSelect_Equality(answer1, answer2, options)
                    val2 = val1
                elif question in PAIRED_QUESTIONS:
                    paired_question = PAIRED_QUESTIONS[question]
                    val1 = is_Member(mentor[question]['val'], mentee[paired_question]['val'])
                    val2 = is_Member(mentee[question]['val'], mentee[paired_question]['val'])
            else:
                val1 = in_Range(mentee["Your Age"]['val'], mentor["Preferred Minimum Age"]['val'], mentor["Preferred Maximum Age"]['val'])
                val2 = in_Range(mentor["Your Age"]['val'], mentee["Preferred Minimum Age"]['val'], mentee["Preferred Maximum Age"]['val'])
            val1 = val1*2 if question in mentor_priority else val1 
            val1 = val2*2 if question in mentee_priority else val2  
            score += val1 + val2   
    return score * 100 / total                


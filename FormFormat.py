from constants import Gender, Goals, Grow, Hobby, Languages, MentorSession, Qualities, QuestionType, Race, Times


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
    "Priority 1": [QuestionType.PRIORITY1],
    "Priority 2": [QuestionType.PRIORITY2],
    "Priority 3": [QuestionType.PRIORITY3],
    }

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


    

from constants import Goals, Grow, Hobby, Languages, MentorSession, Pronouns, Qualities, QuestionType, Times

My_INFO = {"Your Gender": [QuestionType.RADIO,],
    "Your Race": [QuestionType.RADIO],
    "Your Zip Code": [QuestionType.DISTANCE],
    "Preferred Setting": [QuestionType.MULTISELECT, [MentorSession.PERSON, MentorSession.VIRTUAL, MentorSession.HYBRID]], # in-person, virtual, or hybrid
    "Preferred Time": [QuestionType.MULTISELECT, [Times.WEEKDAYA, Times.WEEKDAYE, Times.WEEKENDM, Times.WEEKENDA, Times.WEEKENDE]],
    "Your Disability": [QuestionType.RADIO], #
    "Your LGBTQIA Status": [QuestionType.RADIO],
    "Your Religion": [QuestionType.RADIO],
    "Your Age": [QuestionType.RANGE],
    "Preferred Goals": [QuestionType.MULTISELECT, [Goals.FRIEND, Goals.INDEPENDENCE, Goals.CAREER, Goals.SKILL, Goals.COMMUNITY, Goals.ACTIVITIES, Goals.HOBBY, Goals.CHAT]],
    "Preferred Growth Areas": [QuestionType.MULTISELECT, [Grow.SCHOOL, Grow.LISTENER, Grow.CONFIDENCE, Grow.WORK, Grow.PEOPLE, Grow.FUNNY, Grow.ORGANIZATION, Grow.LEARN, Grow.FAMILY, Grow.ANXIETY, Grow.TIME, Grow.COMFORT, Grow.MONEY, Grow.MYSELF, Grow.PERSPECTIVE, Grow.TRUST, Grow.PUBLIC, Grow.MEETINGS]],
    "Preferred Interests": [QuestionType.MULTISELECT, [Hobby.ANIMALS, Hobby.ANIME, Hobby.BOARDGAMES, Hobby.BOWLING, Hobby.COOKING, Hobby.DANCING, Hobby.FISHING, Hobby.FASHION, Hobby.MOVIES, Hobby.FRIENDS, Hobby.LIBRARY, Hobby.MUSEUMS, Hobby.MUSIC, Hobby.ART, Hobby.PHOTOS, Hobby.EXERCISE, Hobby.SCIENCE, Hobby.SHOPPING, Hobby.SINGING, Hobby.SPORTS, Hobby.SOCIALMEDIA, Hobby.TECH, Hobby.VOLUNTEER, Hobby.TV, Hobby.WRITING, Hobby.EATING,]],
    "Your Qualities": [QuestionType.MULTISELECT, [Qualities.FUNNY, Qualities.SERIOUS, Qualities.AMBITIOUS, Qualities.SCIENTIFIC, Qualities.COURAGEOUS, Qualities.RELAXED, Qualities.SUPPORTIVE, Qualities.OUTGOING, Qualities.CONFIDENT, Qualities.SOCIAL, Qualities.SHY, Qualities.EXPERIENCED, Qualities.STUDIOUS]],
    "Your Education Plans": [QuestionType.MULTISELECT], 
    "Your Primary Language": [QuestionType.RADIO],
    "Your Additional Languages": [ QuestionType.MULTISELECT,  [Languages.ENGLISH, Languages.SPANISH, Languages.PORTUGUESE, Languages.CANTONESE, Languages.MANDARIN, Languages.FRENCH, Languages.HAITIAN, Languages.AMERICANSL, Languages.OTHER]],
    }

import csv
from algorithm import match, matchingAlgorithm
from constants import Gender, Goals, Grow, Hobby, Languages, MentorSession, Pronouns, Qualities, QuestionType, Race, Times
# Specify the path to your CSV file

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

list_response_questions = ["Your Additional Languages","Preferred Gender","Preferred Race","Preferred Setting","Preferred Time","Preferred Goals", "Preferred Growth Areas", "Preferred Interests", "Preferred Qualities"]

mentee_csv = './Data/Mentee.csv'
mentee_forms = []
# Open the CSV file and create a CSV reader object
with open(mentee_csv, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    count = 0
    # Iterate through rows and print each row
    columns = {}
    for row in reader:
        if(count):
            response = {}
            for field in columns.keys():
                question_format = FORM[columns[field]]
                if columns[field] in set(['#', "Your First Name", "Your Last Name"]):
                    response[columns[field]] = {"val": row[field].strip()}
                else:
                    response_entry = {"type": question_format[0], "options": question_format[1]} if len(question_format) > 1 else {"type": question_format[0]}
                    response_entry['val'] = [word.strip() for word in row[field].split('-')] if columns[field] in list_response_questions else row[field].strip()
                    response[columns[field]] = response_entry
            mentee_forms.append(response)
        else:
            for field in range(len(row)):
                if row[field] in FORM:
                    columns[field] = row[field]         
        count+=1
  
mentor_csv = './Data/Mentor.csv'
mentor_forms=[]
with open(mentor_csv, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    count = 0
    # Iterate through rows and print each row
    columns = {}
    for row in reader:
        if(count):
            response = {}
            for field in columns.keys():
                question_format = FORM[columns[field]]
                if columns[field] in set(['#', "Your First Name", "Your Last Name"]):
                    response[columns[field]] = {"val": row[field].strip()}
                else:
                    response_entry = {"type": question_format[0], "options": question_format[1]} if len(question_format) > 1 else {"type": question_format[0]}
                    response_entry['val'] = [word.strip() for word in row[field].split('-')] if columns[field] in list_response_questions else row[field].strip()
                    response[columns[field]] = response_entry
            mentor_forms.append(response)
        else:
            for field in range(len(row)):
                if row[field] in FORM:
                    columns[field] = row[field]         
        count+=1

mentee_mentor_match = {}
for mentee in mentee_forms:
    candidates = []
    menteeName = mentee["Your First Name"]['val'] + ' '+ mentee["Your Last Name"]['val']
    for mentor in mentor_forms:
        mentorName = mentor["Your First Name"]['val'] +' '+ mentor["Your Last Name"]['val']
        score = match(mentor, mentee)
        candidates.append((score, mentorName))
    print(menteeName, candidates)
    mentee_mentor_match[menteeName] = sorted(candidates, reverse = True)

print(mentee_mentor_match)
        


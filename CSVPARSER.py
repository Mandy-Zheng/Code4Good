import csv
from algorithm import matchingAlgorithm
from constants import Gender, Goals, Grow, Hobby, Languages, MentorSession, Pronouns, Qualities, QuestionType, Race, Times
# Specify the path to your CSV file
mentee_csv = './Data/Mentee.csv'
mentee_forms=['#',"Your First Name","Your Last Name","Your Gender","Your Pronouns","Your Lgbtqia Status","Your Race","Your Dob","Your Age","Your Student Status","Your Employer","Your Income","Your Zipcode","Your County","Have Disability","Your Disability","Your Primary Language","Your Primary Language Other","Your Additional Languages","Your Additional Languages Other","Your Religion","Your Qualities","Preferred Gender","Preferred Race","Preferred Travel Distance","Preferred Setting","Preferred Time","Preferred Education","Preferred Disability","Preferred Lgbtqia","Preferred Religion","Preferred Minimum Age","Preferred Maximum Age","Preferred Goals","Preferred Growth Areas","Preferred Interests","Preferred Qualities","Priority 1","Priority 2","Priority 3","Background Check"]

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
                    response_entry['val'] = [word.strip() for word in row[field].split('-')] if '-' in row[field] else row[field].strip()
                    response[columns[field]] = response_entry
            mentee_forms.append(response)
        else:
            for field in range(len(row)):
                if row[field] in FORM:
                    columns[field] = row[field]         
        count+=1
    print(mentee_forms)

print("=======================")
       
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
            for field in range(len(row)):
                if(field in columns):
                    question_format = FORM[columns[field]]
                    if columns[field] in set(['#', "Your First Name", "Your Last Name"]):
                        response[columns[field]] = {"val": row[field].strip()}
                    else:
                        response_entry = {"type": question_format[0]}
                        if len(question_format) > 1:
                            response_entry['options'] = question_format[1]
                        response_entry['val'] = row[field].strip()
                        if '-' in row[field]:
                            response_entry['val'] = [word.strip() for word in row[field].split('-')]
                        response[columns[field]] = response_entry
            mentor_forms.append(response)
        else:
            for field in range(len(row)):
                if row[field] in FORM:
                    columns[field] = row[field]         
        count+=1
    print(mentor_forms)

# for mentee in mentee_forms:
#     max_score = 0
#     for mentor in mentor_forms:
#         matchingAlgorithm(mentee, mentor)
        


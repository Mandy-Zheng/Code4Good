import csv
from algorithm import matchingAlgorithm
from constants import Gender, Goals, Grow, Hobby, MentorSession, Qualities, QuestionType, Race, Times
# Specify the path to your CSV file
mentee_csv = './Data/Mentee.csv'
mentee_forms=[]
headers = ['Your First Name', 'Your Last Name', 'Your Phone Number', 'Your Email', 'Guardian Phone Number', 'Your Gender', 'Your Race', 'Your Dob', 'Your Age', 'Your Program', 'Your Income', 'Your Plan', 'Your Education', 'Your Zipcode', 'County', 'Have Disability', 'Your Disability', 'Primary Language', 'Additional Languages', 'Your Religion', 'Your Qualities', 'Mentor Gender', 'Mentor Race', 'Travel Distance', 'Mentoring Setting', 'Mentoring Time', 'Mentor Disability', 'Mentor Lgtbqia', 'Mentor Religion', 'Mentor Age', 'Interests', 'Hobbies', 'Personality', 'Important Factor 1', 'Important Factor 2', 'System', 'Source', 'Screen', 'Updated', 'Created']
headers = ['Your First Name', 'Your Last Name', 'Your Email', 'Mentor Gender', 'Mentor Race', 'Travel Distance', 'Mentoring Setting', 'Mentoring Time', 'Mentor Disability', 'Mentor Lgtbqia', 'Mentor Religion', 'Mentor Age', 'Interests', 'Hobbies', 'Personality', 'Important Factor 1', 'Important Factor 2', 'Important Factor 3']
Fields = [ "name", "email","pref_gender", "pref_race", "travel","mentoring_relationship", "availability","similar_disability","mentee_disability","LGBTQIA","similar_religion","mentee_religion","pref_min_age","pref_max_age","goals","grow","hobbies","qualities","priority1","priority2","priority3" ]

Questions = {
    "name": [QuestionType.UNWEIGHTED],
    "email": [QuestionType.UNWEIGHTED],
    "pref_gender": [QuestionType.MULTISELECT, [Gender.MAN, Gender.WOMAN, Gender.NONBINARY]],
    "travel": [QuestionType.UNWEIGHTED],
    "pref_race": [QuestionType.MULTISELECT, [Race.BLACK, Race.WHITE, Race.HISPANIC, Race.ASIAN, Race.MIDEASTERN, Race.AMERICANINDIAN]],
    "mentoring_relationship": [QuestionType.MULTISELECT, [MentorSession.PERSON, MentorSession.VIRTUAL, MentorSession.HYBRID]], # in-person, virtual, or hybrid
    "availability": [QuestionType.MULTISELECT, [Times.WEEKDAYA, Times.WEEKDAYE, Times.WEEKENDM, Times.WEEKENDA, Times.WEEKENDE]],
    "similar_disability": [QuestionType.RADIO],
    "mentee_disability": [QuestionType.RADIO],
    "LGBTQIA": [QuestionType.RADIO],
    "similar_religion": [QuestionType.RADIO],
    "mentee_religion": [QuestionType.RADIO],
    "pref_min_age": [QuestionType.UNWEIGHTED],
    "pref_max_age": [QuestionType.UNWEIGHTED],
    "goals": [QuestionType.MULTISELECT, [Goals.FRIEND, Goals.INDEPENDENCE, Goals.CAREER, Goals.SKILL, Goals.COMMUNITY, Goals.ACTIVITIES, Goals.HOBBY, Goals.CHAT]],
    "grow": [QuestionType.MULTISELECT, [Grow.SCHOOL, Grow.LISTENER, Grow.CONFIDENCE, Grow.WORK, Grow.PEOPLE, Grow.FUNNY, Grow.ORGANIZATION, Grow.LEARN, Grow.FAMILY, Grow.ANXIETY, Grow.TIME, Grow.COMFORT, Grow.MONEY, Grow.MYSELF, Grow.PERSPECTIVE, Grow.TRUST, Grow.PUBLIC, Grow.MEETINGS]],
    "hobbies": [QuestionType.MULTISELECT, [Hobby.ANIMALS, Hobby.ANIME, Hobby.BOARDGAMES, Hobby.BOWLING, Hobby.COOKING, Hobby.DANCING, Hobby.FISHING, Hobby.FASHION, Hobby.MOVIES, Hobby.FRIENDS, Hobby.LIBRARY, Hobby.MUSEUMS, Hobby.MUSIC, Hobby.ART, Hobby.PHOTOS, Hobby.EXERCISE, Hobby.SCIENCE, Hobby.SHOPPING, Hobby.SINGING, Hobby.SPORTS, Hobby.SOCIALMEDIA, Hobby.TECH, Hobby.VOLUNTEER, Hobby.TV, Hobby.WRITING, Hobby.EATING,]],
    "qualities": [QuestionType.MULTISELECT, [Qualities.FUNNY, Qualities.SERIOUS, Qualities.AMBITIOUS, Qualities.SCIENTIFIC, Qualities.COURAGEOUS, Qualities.RELAXED, Qualities.SUPPORTIVE, Qualities.OUTGOING, Qualities.CONFIDENT, Qualities.SOCIAL, Qualities.SHY, Qualities.EXPERIENCED, Qualities.STUDIOUS]],
    "priority1": [QuestionType.PRIORITY1],
    "priority2": [QuestionType.PRIORITY2], 
    "priority3": [QuestionType.PRIORITY3] 

    # val could be like a list (for like multiselect) or strings or number
    # ...etc do this for other questions
}


# Open the CSV file and create a CSV reader object
with open(mentee_csv, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    count = 0
    mentee_forms = []
    # Iterate through rows and print each row
    for row in reader:
        if(count):
            print(row)
        count+=1
        
mentor_csv = './Data/Mentor.csv'
mentor_forms=[]

headers = ['Your First Name', 'Your Last Name', 'Your Phone Number', 'Your Email', 'Guardian Phone Number', 'Your Gender', 'Your Race', 'Your Dob', 'Your Age', 'Your Program', 'Your Income', 'Your Plan', 'Your Education', 'Your Zipcode', 'County', 'Have Disability', 'Your Disability', 'Primary Language', 'Additional Languages', 'Your Religion', 'Your Qualities', 'Mentor Gender', 'Mentor Race', 'Travel Distance', 'Mentoring Setting', 'Mentoring Time', 'Mentor Disability', 'Mentor Lgtbqia', 'Mentor Religion', 'Mentor Age', 'Interests', 'Hobbies', 'Personality', 'Important Factor 1', 'Important Factor 2', 'System', 'Source', 'Screen', 'Updated', 'Created']
["name", "email","pref_gender","travel","pref_race", "mentoring_relationship"]
# Open the CSV file and create a CSV reader object
with open(mentor_csv, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    count = 0
    mentor_forms = []
    # Iterate through rows and print each row
    for row in reader:
        if(count):
            print(row)
        count+=1

for mentee in mentee_forms:
    max_score = 0
    for mentor in mentor_forms:
        matchingAlgorithm(mentee, mentor)
        


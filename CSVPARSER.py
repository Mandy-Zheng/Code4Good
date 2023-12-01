import csv
from algorithm import matchingAlgorithm
from constants import Gender, Goals, Grow, Hobby, MentorSession, Qualities, QuestionType, Race, Times
# Specify the path to your CSV file
mentee_csv = './Data/Mentee.csv'
mentee_forms=[]
headers = ['#', 'Your First Name', 'Your Last Name', 'Your Phone Number', 'Your Email', 'Guardian First Name', 'Guardian Last Name', 'Guardian Phone Number', 'Your Gender', 'Your Pronouns', 'Lgbtqia', 'Your Race', 'Your Dob', 'Your Age', 'Your Program', 'Your Income', 'Your Plan', 'Your Education', 'Your Zipcode', 'County', 'Have Disability', 'Your Disability', 'Primary Language', 'Primary Language Other', 'Additional Languages', 'Additional Languages Other', 'Your Religion', 'Your Qualities', 'Mentor Gender', 'Mentor Race', 'Travel Distance', 'Mentoring Setting', 'Mentoring Time', 'Mentor Disability', 'Mentor Lgtbqia', 'Mentor Religion', 'Minimum Age', 'Maximum Age', 'Interests', 'Hobbies', 'Personality', 'Important Factor 1', 'Important Factor 2', 'Important Factor 3', 'System', 'Source', 'Screen', 'Updated', 'Created']
'Mentor Disability', 'Mentor Lgtbqia', 'Mentor Religion', 'Minimum Age', 'Maximum Age', 'Interests', 'Hobbies', 'Personality', 'Important Factor 1', 'Important Factor 2', 'Important Factor 3', 'System', 'Source', 'Screen', 'Updated', 'Created'
Questions = {
    "name": [QuestionType.UNWEIGHTED],
    'Your Email': [QuestionType.UNWEIGHTED],
    'Mentor Gender': [QuestionType.MULTISELECT, [Gender.MAN, Gender.WOMAN, Gender.NONBINARY]],
    'Travel Distance': [QuestionType.UNWEIGHTED],
    'Mentor Race': [QuestionType.MULTISELECT, [Race.BLACK, Race.WHITE, Race.HISPANIC, Race.ASIAN, Race.MIDEASTERN, Race.AMERICANINDIAN]],
    'Mentoring Setting': [QuestionType.MULTISELECT, [MentorSession.PERSON, MentorSession.VIRTUAL, MentorSession.HYBRID]], # in-person, virtual, or hybrid
    'Mentoring Time': [QuestionType.MULTISELECT, [Times.WEEKDAYA, Times.WEEKDAYE, Times.WEEKENDM, Times.WEEKENDA, Times.WEEKENDE]],
    'Your Disability': [QuestionType.RADIO],
    'Mentor Disability': [QuestionType.RADIO],
    "Lgbtqia": [QuestionType.RADIO],
    "LGBTQIA": [QuestionType.RADIO],
    "Your Religion": [QuestionType.RADIO],
    "Mentor Religion": [QuestionType.RADIO],
    'Minimum Age': [QuestionType.UNWEIGHTED],
    'Maximum Age': [QuestionType.UNWEIGHTED],
    "goals": [QuestionType.MULTISELECT, [Goals.FRIEND, Goals.INDEPENDENCE, Goals.CAREER, Goals.SKILL, Goals.COMMUNITY, Goals.ACTIVITIES, Goals.HOBBY, Goals.CHAT]],
    "grow": [QuestionType.MULTISELECT, [Grow.SCHOOL, Grow.LISTENER, Grow.CONFIDENCE, Grow.WORK, Grow.PEOPLE, Grow.FUNNY, Grow.ORGANIZATION, Grow.LEARN, Grow.FAMILY, Grow.ANXIETY, Grow.TIME, Grow.COMFORT, Grow.MONEY, Grow.MYSELF, Grow.PERSPECTIVE, Grow.TRUST, Grow.PUBLIC, Grow.MEETINGS]],
    'Hobbies': [QuestionType.MULTISELECT, [Hobby.ANIMALS, Hobby.ANIME, Hobby.BOARDGAMES, Hobby.BOWLING, Hobby.COOKING, Hobby.DANCING, Hobby.FISHING, Hobby.FASHION, Hobby.MOVIES, Hobby.FRIENDS, Hobby.LIBRARY, Hobby.MUSEUMS, Hobby.MUSIC, Hobby.ART, Hobby.PHOTOS, Hobby.EXERCISE, Hobby.SCIENCE, Hobby.SHOPPING, Hobby.SINGING, Hobby.SPORTS, Hobby.SOCIALMEDIA, Hobby.TECH, Hobby.VOLUNTEER, Hobby.TV, Hobby.WRITING, Hobby.EATING,]],
    'Personality': [QuestionType.MULTISELECT, [Qualities.FUNNY, Qualities.SERIOUS, Qualities.AMBITIOUS, Qualities.SCIENTIFIC, Qualities.COURAGEOUS, Qualities.RELAXED, Qualities.SUPPORTIVE, Qualities.OUTGOING, Qualities.CONFIDENT, Qualities.SOCIAL, Qualities.SHY, Qualities.EXPERIENCED, Qualities.STUDIOUS]],
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
        


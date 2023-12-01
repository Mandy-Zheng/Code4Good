import csv
from algorithm import matchingAlgorithm
# Specify the path to your CSV file
mentee_csv = './Data/Mentee.csv'
mentee_forms=[]
headers = ['Your First Name', 'Your Last Name', 'Your Phone Number', 'Your Email', 'Guardian Phone Number', 'Your Gender', 'Your Race', 'Your Dob', 'Your Age', 'Your Program', 'Your Income', 'Your Plan', 'Your Education', 'Your Zipcode', 'County', 'Have Disability', 'Your Disability', 'Primary Language', 'Additional Languages', 'Your Religion', 'Your Qualities', 'Mentor Gender', 'Mentor Race', 'Travel Distance', 'Mentoring Setting', 'Mentoring Time', 'Mentor Disability', 'Mentor Lgtbqia', 'Mentor Religion', 'Mentor Age', 'Interests', 'Hobbies', 'Personality', 'Important Factor 1', 'Important Factor 2', 'System', 'Source', 'Screen', 'Updated', 'Created']
["name", "email","pref_gender","travel","pref_race", "mentoring_relationship"]
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
import csv
from FormFormat import FORM
from algorithm import match
from constants import Gender, Goals, Grow, Hobby, Languages, MentorSession, Qualities, QuestionType, Race, Times
# Specify the path to your CSV file

list_response_questions = ["Your Additional Languages","Preferred Gender","Preferred Race","Preferred Setting","Preferred Time","Preferred Goals", "Preferred Growth Areas", "Preferred Interests", "Preferred Qualities"]

mentee_csv = './Data/Mentee.csv'
mentee_forms = []
# Open the CSV file and create a CSV reader object
with open(mentee_csv, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    count = 0
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

def getTopMatches(topn):
    mentee_mentor_match = {}
    for mentee in mentee_forms:
        candidates = []
        mentee_name = mentee["Your First Name"]['val'] + ' '+ mentee["Your Last Name"]['val']
        for mentor in mentor_forms:
            mentorName = mentor["Your First Name"]['val'] +' '+ mentor["Your Last Name"]['val']
            score = match(mentor, mentee)
            candidates.append((score, mentorName))
        top_matches = sorted(candidates, reverse = True)
        mentee_mentor_match[mentee_name] = top_matches[0:min(topn, len(top_matches))]
    return mentee_mentor_match

def formatOutput(matches):
    count = 0
    for mentee in matches.keys():
        mentors = matches[mentee]
        print('Mentee: '+mentee)
        for mentor in mentors:
            print('\t Mentor: ' + mentor[1] + '\t' +'Compatibility: ' + str(int(mentor[0]))+'%')
        count += 1
        
formatOutput(getTopMatches(3))
        


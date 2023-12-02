import csv
from FormFormat import FORM
from algorithm import match
from constants import list_response_questions
MENTOR_CSV = './Data/Mentor.csv'
MENTEE_CSV = './Data/Mentee.csv'
        
def parse_responses(path_file):
    """
    read responses from path_file and parse into an array of form_question formatted dictionaries
    """
    form_responses = []
    with open(path_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        count = 0
        columns = {}
        for row in reader: # for each user response form
            if(count): 
                response = {}
                for field in columns.keys(): # for question in form, map to make into form_question format
                    question_format = FORM[columns[field]]
                    if columns[field] in set(['#', "Your First Name", "Your Last Name"]):
                        response[columns[field]] = {"val": row[field].strip()}
                    else:
                        response_entry = {"type": question_format[0], "options": question_format[1]} if len(question_format) > 1 else {"type": question_format[0]}
                        response_entry['val'] = [word.strip() for word in row[field].split('-')] if columns[field] in list_response_questions else row[field].strip()
                        response[columns[field]] = response_entry
                form_responses.append(response)
            else: # get headers for each column, for question in each form map column to question label
                for field in range(len(row)):
                    if row[field] in FORM:
                        columns[field] = row[field]         
            count+=1
    return form_responses

def get_top_matches(topn):
    """
    For each mentee, find topn matches out of mentors
    """
    mentor_forms = parse_responses(MENTOR_CSV)
    mentee_forms = parse_responses(MENTEE_CSV)
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
    """
    Format matches between mentees and mentors
    """
    count = 1
    print('Mentee & Mentor Matches')
    for mentee in matches.keys():
        mentors = matches[mentee]
        print('\nMentee'+ ' '+str(count)+': '+mentee)
        for mentor in mentors:
            print('\t Mentor: ' + mentor[1] + '\t' +'Compatibility: ' + str(int(mentor[0]))+'%')
        count += 1
        
formatOutput(get_top_matches(3))
        


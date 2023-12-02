# Enums
# All non-preference questions (not included in calculation) are classified as UNWEIGHTED
from enum import Enum


class QuestionType(Enum):
    UNWEIGHTED = 0
    RADIO = 1
    MULTISELECT = 2
    DROPDOWN = 3
    TEXT = 4
    SLIDER = 5
    PRIORITY1 = 6
    PRIORITY2 = 7
    PRIORITY3 = 8
    RANGE = 9
    DISTANCE = 10
    
class Race(Enum):
    BLACK = "Black"
    WHITE = "White"
    HISPANIC = "Hispanic/Latinx"
    ASIAN = "Asian"
    MIDEASTERN = "Middle Eastern"
    AMERICANINDIAN = "American Indian"

class Gender(Enum):
    MAN = 'Man',
    WOMAN = 'Woman',
    NONBINARY = 'Nonbinary'
    
class MentorSession(Enum):
    PERSON="In Person"
    VIRTUAL="Virtual"
    HYBRID="Hybrid"
    
class Times(Enum):
    WEEKDAYA = "Weekday afternoons", 
    WEEKDAYE = "Weekday evenings", 
    WEEKENDM = "Weekend mornings", 
    WEEKENDA = "Weekend afternoons", 
    WEEKENDE = "Weekend evenings"
    
class Goals(Enum):
    FRIEND= "Make a friend", 
    INDEPENDENCE="Have someone help me feel more independent", 
    CAREER = "Provide me with career and school advice", 
    SKILL = "Learn a new skill", 
    COMMUNITY = "Explore the community", 
    ACTIVITIES = "Do fun activities", 
    HOBBY = "Share a hobby", 
    CHAT = "Have someone to talk to"
    
class Grow(Enum):
    SCHOOL = "Do better in school", 
    LISTENER = "Be a better listener", 
    CONFIDENCE = "Have more confidence", 
    WORK = "Gain work skills",
    PEOPLE = "Gain people skills",
    FUNNY = "Be funnier",
    ORGANIZATION = "Be more organized",
    LEARN = "Learn a skill or hobby", 
    FAMILY = "Get along better with others (including my parents/siblings)",
    ANXIETY = "Feel less anxious about meeting new people or going new places",
    TIME = "Manage my time better",
    COMFORT = "Get out of my comfort zone",
    MONEY = "Learn to make or save money", 
    MYSELF = "Be less self-conscious about myself",
    PERSPECTIVE = "Understand other perspectives better", 
    TRUST = "Trusting my mentor", 
    PUBLIC = "Going to public places", 
    MEETINGS = "Showing up to meetings on time", 
    
class Hobby(Enum):
    ANIMALS = "Animals/Going to Zoo",
    ANIME = "Anime",
    BOARDGAMES = "Playing board games",
    BOWLING = "Bowling",
    COOKING = "Cooking/Baking",
    DANCING = "Dancing",
    FISHING = "Fishing",
    FASHION  = "Fashion/Makeup/Style",
    MOVIES = "Going to the movies",
    FRIENDS = "Hanging with friends",
    LIBRARY = "Reading/Visiting the Library",
    MUSEUMS = "Visiting museums",
    MUSIC = "Listening to music/Attending concerts",
    ART = "Art: Painting, drawing, theater, etc",
    PHOTOS = "Photography",
    EXERCISE = "Exercise: Running, walking, going to park",
    SCIENCE = "Science",
    SHOPPING = "Shopping",
    SINGING = "Singing",
    SPORTS = "Sports",
    SOCIALMEDIA = "Social media",
    TECH = "Technology/Video games",
    VOLUNTEER = "Volunteering",
    TV = "Watching TV",
    WRITING = "Writing",
    EATING = "Going out to eat",
    
class Qualities(Enum):
    FUNNY = "Funny",
    SERIOUS = "Serious and contemplative",
    AMBITIOUS = "Ambitious",
    SCIENTIFIC = "Scientific",
    COURAGEOUS = "Courageous",
    RELAXED = "Relaxed",
    SUPPORTIVE = "Supportive",
    OUTGOING = "Outgoing",
    CONFIDENT = "Confident",
    SOCIAL = "Social",
    SHY = "Introverted/Shy" ,
    EXPERIENCED = "Experience (In career or field of study)",
    STUDIOUS = "Studious"
    
class Pronouns(Enum):
    HE = 'He', 
    SHE = 'She',
    THEY = 'They',
    OTHER = 'Other'

class Languages(Enum):
    ENGLISH = 'English',
    SPANISH = 'Spanish',
    PORTUGUESE = 'Portuguese',
    CANTONESE = 'Cantonese',
    MANDARIN = 'Mandarin',
    FRENCH = 'French',
    HAITIAN = 'Haitian Creole',
    AMERICANSL = 'American Sign Language',
    OTHER = 'Other'
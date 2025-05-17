
import random
import re

intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["hi", "hello", "hey", "good day", "what's up", "how are you"],
            "responses": ["Hello!", "Hi there!", "Greetings!", "Hey! How can I assist you?"]
        },
        {
            "tag": "farewell",
            "patterns": ["bye", "goodbye", "see you", "talk later", "exit", "quit"],
            "responses": ["Goodbye!", "See you later!", "Take care!", "Hope to talk to you soon!"]
        },
        {
            "tag": "creator",
            "patterns": ["who created you", "who is your developer", "who made you", "who invented you"],
            "responses": ["I was created by Veludandi Harini, your college assistant chatbot."]
        },
        {
            "tag": "college_info",
            "patterns": [
                "tell me about the college", "college info", "about the college", "college details",
                "what is this college", "information about college"
            ],
            "responses": [
                "XYZ College of Engineering and Technology was established in 1990 and offers a variety of courses.",
                "Our college focuses on quality education and research with excellent facilities."
            ]
        },
        {
            "tag": "admission",
            "patterns": [
                "how to apply", "admission process", "admission criteria", "application details",
                "admissions", "application process"
            ],
            "responses": [
                "Admissions are open for undergraduate and postgraduate programs. You can apply online through our website.",
                "Please visit the admissions office or our website for detailed admission requirements."
            ]
        },
        {
            "tag": "placement_support",
            "patterns": [
                "placement support", "job assistance", "internships", "career services",
                "placement cell", "placements", "job help"
            ],
            "responses": [
                "Our placement cell provides internship and job placement assistance with reputed companies.",
                "We regularly conduct training and placement drives to support our students."
            ]
        },
        {
            "tag": "canteen",
            "patterns": [
                "canteen timings", "food services", "cafeteria", "meal options", "food timings"
            ],
            "responses": [
                "The canteen is open from 8 AM to 7 PM on weekdays.",
                "We offer a variety of meals including vegetarian and non-vegetarian options."
            ]
        },
        {
            "tag": "library",
            "patterns": [
                "library timings", "library hours", "library information", "where is the library"
            ],
            "responses": [
                "The library is open from 9 AM to 8 PM on weekdays.",
                "You can borrow books with your student ID. We have a large collection of textbooks and research papers."
            ]
        },
        {
            "tag": "courses",
            "patterns": [
                "what courses are offered", "courses available", "list of courses",
                "programs", "degree programs"
            ],
            "responses": [
                "We offer undergraduate and postgraduate courses in Computer Science, Electronics, Mechanical, Civil, and more.",
                "You can check the full list of courses on our official website."
            ]
        },
        {
            "tag": "hostel",
            "patterns": [
                "hostel facilities", "do you have hostels", "accommodation", "hostel details"
            ],
            "responses": [
                "Yes, we have separate hostels for boys and girls with 24/7 security and Wi-Fi.",
                "Hostel rooms are equipped with basic amenities and mess facilities."
            ]
        },
        {
            "tag": "events",
            "patterns": [
                "upcoming events", "college events", "festivals", "seminars", "workshops"
            ],
            "responses": [
                "We regularly host workshops, seminars, cultural festivals, and sports events throughout the year.",
                "Check our events calendar on the website for the latest updates."
            ]
        },
        {
            "tag": "sports",
            "patterns": [
                "sports facilities", "sports activities", "gym", "sports ground"
            ],
            "responses": [
                "We have excellent sports facilities including a gym, basketball and cricket grounds.",
                "Students are encouraged to participate in inter-college sports competitions."
            ]
        },
        {
            "tag": "transport",
            "patterns": [
                "transport facilities", "bus service", "college transport", "shuttle service"
            ],
            "responses": [
                "The college provides bus services to major parts of the city with multiple routes and timings.",
                "You can contact the transport office for route details and fees."
            ]
        },
        {
            "tag": "default",
            "patterns": [],
            "responses": [
                "I'm sorry, I didn't understand that. Could you please rephrase?",
                "Can you try asking in a different way?",
                "I'm still learning. Could you ask something else?"
            ]
        }
    ]
}

def get_bot_response(user_input, intents=intents):
    user_input = user_input.lower().strip()

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            # Regex search to find pattern as a word boundary (flexible matching)
            if re.search(r'\b' + re.escape(pattern.lower()) + r'\b', user_input):
                return random.choice(intent["responses"])
    
    # If no pattern matches, use the default responses
    default_intent = next((i for i in intents["intents"] if i["tag"] == "default"), None)
    if default_intent:
        return random.choice(default_intent["responses"])
    
    return "Sorry, I didn't understand that. Please try asking differently."


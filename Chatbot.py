import re
import random
import datetime
class RuleBasedChatbot:     #using regex to match user input
    def __init__(self):
        self.rules ={
            r"My name is (.*)": [
                "Nice to meet you, {0}!",
                "Hi {0}, how may I help you today?"
            ],
            r"What is your name\?": [
                "I'm your Chatbot 2.2!!",
                "Or you can call me BOT."
            ],
            r"What is Chatbot\?":[
                "Well, Chatbot is a simple ruled based chatbot. It uses regular expressions to match user inputs to predefined responses.",
                "As for an example, if you ask me \"What is Chatbot?\", it replies:",
                "I'm Chatbot 2.2!!",
                "You can call me BOT.",
                "It does not use AI or machine learning; it responds based on patterns and rules that are coded by the developer."
            ],
            r"help":[
                "Oh! How can I assist you?",
                "You can ask me about my name or just say hi!!"
            ],
            r"How are you\?":[
                "I'm doing well, thank you for asking!",
                "I'm a computer program, so I am always at 100%! How are you?"
            ],
            r"What can you do\?":[
                "I can chat with you, answer questions about myself, or provide weather updates for specific cities.",
                "I can help you with basic simple doubts and have a friendly conversation!!"
            ],
            r"What is your purpose\?":[
                "Hmm, my purpose is to assist you and have a cool chat experience."
            ],
            r"What is your version\?":[
                "I'm Chatbot 2.2, ---A SIMPLE RULE-BASED CHATBOT.",
                "Currently, I'm running version 2.2 of Chatbot."
            ],
            r"What's\s+the\s+weather\s+in\s+(.*)\?":[
                "Umm, I'm not connected to live WEATHER SERVICE, but i bet the weather in {0} is lovely!",
                "Sorry, I don't have the rights to check the real weahter, but let's just say it's sunny in {0}."
            ],
            r"What day is it\?":[
                lambda match: f"Today is {datetime.datetime.now().strftime('%A, %d %B %Y')}."
            ],
            r"What time is it\?":[
                lambda match: f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
            ],
            r"(Hi|hello|hey)":[
                "HELLO!!",
                "Hi there!!",
                "Heyy!!"
            ],
            r"sup":[
                "YOOO!!!"
            ],
            r"(bye|quit|exit)":[
                "GOODBYE!!",
                "See you later!!",
                "Exiting chat. HAVE A GREAT DAY!!"
            ]
        }
        self.fallbacks = [
               "Oh! I'm not sure I understand. Can you rephrase?",
               "Sorry, I didn't get that.",
               "Can you ask me something else?" 
            ]
        self.unhandled_log = []
    def g_response(self, user_input):
        for pattern, responses in self.rules.items():
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                response = random.choice(responses)
                if callable(response):
                    return response(match)
                elif match.groups():
                    return response.format(*match.groups())
                else:
                    return response
        self.log_unhandled_query(user_input)
        return random.choice(self.fallbacks)
    def log_unhandled_query(self, user_input):
        self.unhandled_log.append(user_input)
        print(f"(DEBUG: Logged unhandled query: '{user_input}')")
    def start_chat(self):
        print("Chatbot 2.2: Hello! I'm Chatbot. You can type 'bye' to exit.")
        while True:
            user_input = input("You:  ")
            response = self.g_response(user_input)
            print(f"Chatbot 2.2: {response}")
            if re.search(r"bye|quit|exit", user_input, re.IGNORECASE):
                break
if __name__== "__main__":
    bot = RuleBasedChatbot()
    bot.start_chat()

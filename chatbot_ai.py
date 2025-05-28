import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import datetime

print("Ensuring 'wordnet' corpus is downloaded...")
nltk.download('wordnet', quiet=True, raise_on_error=False)
print("Ensuring 'punkt' tokenizer is downloaded...")
nltk.download('punkt', quiet=True, raise_on_error=False)

knowledge_base = {
    "greetings": [
        "hello", "hi", "hey", "greetings", "how are you"
    ],
    "greeting_responses": [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Hey! Good to see you. Ask me anything.",
        "Greetings! How may I assist you?"
    ],
    "goodbyes": [
        "bye", "goodbye", "see you", "farewell", "exit", "quit"
    ],
    "goodbye_responses": [
        "Goodbye! Have a great day!",
        "See you later! Feel free to come back anytime.",
        "Farewell! It was nice chatting with you.",
        "Bye! Take care."
    ],
    "thanks": [
        "thank you", "thanks", "appreciate it"
    ],
    "thanks_responses": [
        "You're welcome!",
        "No problem!",
        "Glad I could help.",
        "Anytime!"
    ],
    "name_query": [
        "your name", "who are you"
    ],
    "name_responses": [
        "I am a simple chatbot created to assist you.",
        "You can call me ChatBot.",
        "I don't have a name, but I'm here to help!"
    ],
    "capabilities_query": [
        "what can you do", "help me", "your purpose"
    ],
    "capabilities_responses": [
        "I can answer basic questions and chat with you. Try asking me about my name or what I can do.",
        "I'm here to provide information and engage in simple conversations.",
        "My purpose is to assist users with their queries."
    ],
    "default_responses": [
        "I'm not sure I understand. Can you rephrase that?",
        "Could you please provide more details?",
        "That's an interesting question, but I don't have an answer for it right now.",
        "I'm still learning. Please try asking something else.",
        "My apologies, I can only handle simple queries at the moment."
    ],
    "weather": {
        "keywords": ["weather", "forecast", "temperature", "climate"],
        "responses": [
            "I cannot provide real-time weather information, as I am just a text-based bot.",
            "To get weather updates, you might want to check a weather app or website."
        ]
    },
    "programming": {
        "keywords": ["programming", "code", "python", "javascript", "developer"],
        "responses": [
            "Programming is a fascinating field! What language are you interested in?",
            "I find programming very logical and creative.",
            "Python is a popular language for AI and data science."
        ]
    },
    "jokes": {
        "keywords": ["joke", "funny", "laugh"],
        "responses": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fake noodle? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised."
        ]
    },
    "date_query": {
        "keywords": ["date", "today's date", "what day is it"],
        "responses": []
    },
    "time_query": {
        "keywords": ["time", "current time", "what time is it"],
        "responses": []
    }
}

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def generate_response(user_input):
    user_input = user_input.lower()

    for greeting in knowledge_base["greetings"]:
        if greeting in user_input:
            return random.choice(knowledge_base["greeting_responses"])

    for goodbye in knowledge_base["goodbyes"]:
        if goodbye in user_input:
            return random.choice(knowledge_base["goodbye_responses"])

    for thank in knowledge_base["thanks"]:
        if thank in user_input:
            return random.choice(knowledge_base["thanks_responses"])

    for name_q in knowledge_base["name_query"]:
        if name_q in user_input:
            return random.choice(knowledge_base["name_responses"])

    for cap_q in knowledge_base["capabilities_query"]:
        if cap_q in user_input:
            return random.choice(knowledge_base["capabilities_responses"])

    for joke_keyword in knowledge_base["jokes"]["keywords"]:
        if joke_keyword in user_input:
            return random.choice(knowledge_base["jokes"]["responses"])

    for date_keyword in knowledge_base["date_query"]["keywords"]:
        if date_keyword in user_input:
            return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}."

    for time_keyword in knowledge_base["time_query"]["keywords"]:
        if time_keyword in user_input:
            return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."

    for topic, data in knowledge_base.items():
        if topic not in ["jokes", "date_query", "time_query"] and isinstance(data, dict) and "keywords" in data:
            for keyword in data["keywords"]:
                if keyword in user_input:
                    return random.choice(data["responses"])

    all_responses_corpus = []
    for key, value in knowledge_base.items():
        if isinstance(value, list) and not (key.endswith("_responses") or key in ["greetings", "goodbyes", "thanks", "name_query", "capabilities_query"]):
            all_responses_corpus.extend(value)
        elif isinstance(value, dict) and "responses" in value and key not in ["jokes", "date_query", "time_query"]:
            all_responses_corpus.extend(value["responses"])

    if not all_responses_corpus:
        return random.choice(knowledge_base["default_responses"])

    corpus = [user_input] + all_responses_corpus

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(corpus)

    vals = cosine_similarity(tfidf[0:1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        return random.choice(knowledge_base["default_responses"])
    else:
        return corpus[idx]

def chatbot():
    print("ChatBot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in knowledge_base["goodbyes"]:
            print("ChatBot:", random.choice(knowledge_base["goodbye_responses"]))
            break
        else:
            response = generate_response(user_input)
            print("ChatBot:", response)

if __name__ == "__main__":
    chatbot()
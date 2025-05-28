# AI-CHATBOT

 A CHATBOT USING NATURAL  LANGUAGE PROCESSING LIBRARIES LIKE  NLTK OR SPACY, CAPABLE OF ANSWERING  USER QUERIES

COMPANY: CODTECH IT SOLUTIONS

NAME: PAILA JAGADEESWARARAO

INTERN ID:CT08DF180

DOMAIN: PYTHON PROGRAMMING

DURATION: 8 WEEKS

MENTOR: NEELA SANTOSH

## IN THIS TASK:

*Key Technologies and Concepts Used:*

Python: The core programming language for developing the chatbot's logic and structure.
Natural Language Processing (NLP):
NLTK (Natural Language Toolkit): A powerful Python library used for:
Tokenization: Breaking down user input sentences into individual words or tokens.
Lemmatization: Reducing words to their base or root form (e.g., "running," "runs" to "run") to improve matching accuracy.
Scikit-learn (sklearn): A machine learning library utilized for:
TF-IDF Vectorization (TfidfVectorizer): Converting text data (user queries and chatbot's knowledge base) into numerical representations (vectors) that capture the importance of words within the text.
Cosine Similarity: Calculating the semantic similarity between the user's query vector and the chatbot's stored response vectors, allowing the bot to identify the most relevant answer for general questions.
Knowledge Base: A simple, dictionary-based structure stores predefined questions, keywords, and corresponding responses, including:
Greetings and farewells.
Common inquiries (e.g., "what is your name," "what can you do").
Specific functionalities like jokes, current date, and time.
Rule-Based and Similarity-Based Response Generation:
Keyword Matching: For direct and common queries (e.g., greetings, asking for a joke, date, or time), the bot uses direct keyword matching for immediate, accurate responses.
Semantic Similarity (TF-IDF & Cosine Similarity): For more general or less direct questions, the bot falls back to analyzing the semantic similarity of the user's input against its broader knowledge base to find the best match.
datetime module: Python's built-in module used to retrieve and format the current date and time dynamically.
random module: Used to select a random response from a list of options (e.g., different ways to say hello, or a random joke).
Functionality:

## The chatbot can:

- Engage in basic conversational greetings and farewells.
- Answer direct questions about itself.
- Tell jokes.
- Provide the current date and time.
- Attempt to answer general questions by finding the most similar pre-defined response in its knowledge base

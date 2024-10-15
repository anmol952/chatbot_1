import nltk
from nltk.chat.util import Chat, reflections

pairs= [
    [
        r"my name is (.*)",
        ["Hello %1, How can i help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!","Hi there!","Hey! How can i assist you?"]

    ],
    [
        r"how are you?",
        ["I'm just a bot, but thanks for asking!", "Doing well, how about you?"]

    ],
    [
        r"what is your name?",
        ["I am a chatboat created using NLTK.",]
    ],
    [
        r"quit",
        ["Bye! Take care.","See you later!"]

    ],
    [
        r"(.*)",
        ["Sorry, I didn't understant that."]

    ]
]


def chatbot():
    print("Hi! I'm a Chatbot. Type 'quit' to exit. ")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
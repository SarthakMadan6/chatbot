import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from tensorflow.keras.models import load_model
import json
import random
import tkinter
from tkinter import *

lemmatizer = WordNetLemmatizer()
model = load_model("chatbot_model.h5")
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details = True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("Found In Bag: %s" %w)
    return (np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words, show_details = False)
    res = model.predict(np. array([p]))[0]
    error_threshold = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > error_threshold]
    results.sort(key = lambda x:x[1], reverse = True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getresponse(ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break

    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getresponse(ints, intents)
    return res



def send(event):
    msg = EntryBox.get("1.0", "end-1c").strip()
    EntryBox.delete("0.0", END)
    if msg != "":
        ChatLog.config(state = NORMAL)
        ChatLog.insert(END, "You: " + msg + "\n\n")
        ChatLog.config(foreground = "#442265", font = ("Verdana", 12, "bold"))
        res = chatbot_response(msg)
        ChatLog.insert(END, "ChatBot: " + res + "\n\n")
        ChatLog.config(state = DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width = FALSE, height = FALSE)
ChatLog = Text(base, bd = 1, bg = "#7FB3D5", height = "8", width = "50", font = "Arial")
ChatLog.config(state = NORMAL)
Welcome = "Hi! How Can I Help You \n "
ChatLog.config(foreground = "#442265", font = ("Verdana", 12, "bold"))
ChatLog.insert(END, "ChatBot: " + Welcome + "\n\n")
ChatLog.config(state = DISABLED)
scrollbar = Scrollbar(base, command = ChatLog.yview )   #cursor = "heart")
ChatLog["yscrollcommand"] = scrollbar.set
SendButton = Button(base, font = ("Verdana", 12, "bold"), text = "Send", width = "12", height = "5", bd = 1,
                    bg = "#ffccff", activebackground = "#3c9d9b", fg = "#000000", command = send)

EntryBox = Text(base, bd = 1, bg = "#C0392B", width = "29", height = "1", font = "Arial")
EntryBox.bind("<Return>", send)
scrollbar.place(x = 376, y = 6, height = 386)
ChatLog.place(x = 6, y = 6, height = 386, width = 370)
EntryBox.place(x = 6, y = 401, height = 50, width = 370)
#SendButton.place(x = 6, y = 401, height = 90)

base.mainloop()








            

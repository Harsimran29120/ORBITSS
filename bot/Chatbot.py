import re
import long_responses as long
from urllib import request, response

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #conta quante parole sono presenti in ogni messaggio predefinito
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    
    #calcola la percentuale delle parole riconosciute in un messaggio dell'user 
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False 
        break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0 #più basso valore possibile di percentuale 


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    #Risposta ----------------------------------------------------------
    response("Hi", ["hi", "hello", "yo"], single_response=True)
    response("I'm fine thanks, and you?", ["how", "are", "you"], required_words=["are"])
    
    response(long.R_POLI, ["why", "the", "iss", "doesn't", "orbit", "around", "the", "poles"], required_words=["why", "doesn't", "orbit", "poles"])
    response(long.R_COSE, ["what's", "the", "space", "iss", "station"], required_words=["what's", "the", "iss"])
    response(long.R_COSE, ["what", "is", "the", "space", "iss", "station"], required_words=["what", "is"])
    response(long.R_ARRIVO, ["how", "do", "astronauts", "arrive", "to", "iss"], required_words=["astronauts", "arrive"])
    response(long.R_ASSEMBLY, ["how", "was", "the", "iss", "built"], required_words=["built"])
    response(long.R_COSTO, ["how", "much", "did", "it", "cost"], required_words=["much", "did", "cost"])
    response(long.R_ESISTENZA, ["why", "does", "the", "iss", "exist"], required_words=["exist"])
    response(long.R_GIRI, ["how", "many", "laps", "does", "the", "iss", "make", "around", "the", "earth"], required_words=["many", "laps", "make", "around", "earth"])
    response(long.R_VEDUTA, ["when", "i", "can", "see", "the", "iss"], required_words=["i", "can", "see"])
    response(long.R_VITA, ["what", "is", "like", "living", "live", "in", "the", "iss"], required_words=["like", "living"])
    

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r"\s+|[,;?'!.-]\s*", user_input.lower())
    response = check_all_messages(split_message)
    return response

#testing the response system 
while True:
    print("Bot: " + get_response(input("You: ")))
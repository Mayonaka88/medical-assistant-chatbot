#we use json to read json files that store our dataset
import json
#we use torch to load the data and extract the data
import torch
# we import our neural network that will process the data from model.py
from nnModel import NeuralNet
from stem import bagOfWords, tokenizeWords
#We use random to et a random response from the data
import random

#we create a new instance of torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#we open our data using json
#change "c:/Users/abdal/Desktop/Ai project/bot/intents.json" to your intents.json directory for the code to work
with open('c:/Users/abdal/Desktop/Ai project/bot/intents.json', 'r') as json_data:
    intents = json.load(json_data)

#we load the data to torch so it can use it
#change "c:/Users/abdal/Desktop/Ai project/bot/data.pth" to your data.pth directory for the code to work
FILE = "c:/Users/abdal/Desktop/Ai project/bot/data.pth"
data = torch.load(FILE)

#these variables are used

#stores all the strings
allWords = data['all_words']
#stores the tags (categories)
tags = data['tags']
#stores the state of the model
modelState = data["model_state"]
#stores the numerical values of the sizes of the possible user inputs and responses
inputSize = data["input_size"]
hiddenSize = data["hidden_size"]
outputSize = data["output_size"]

#we use the NeuralNet() function to process the data using a neural network
model = NeuralNet(inputSize, hiddenSize, outputSize).to(device)
model.load_state_dict(modelState)
model.eval()

def getBotInput(userInput):
    #this function returns the bot's responce depending on the user's input

    #here it processes the user input as a sentence
    sentence = tokenizeWords(userInput)
    Xaxis = bagOfWords(sentence, allWords)
    Xaxis = Xaxis.reshape(1, Xaxis.shape[0])
    Xaxis = torch.from_numpy(Xaxis).to(device)
    output = model(Xaxis)
    #torch.max returns a tuple sp "_," has to be included
    _,predicted = torch.max(output, dim=1)

    #here it makes a predection of the tag of the input and gets the probability of it being the right match
    tag = tags[predicted.item()]
    softmax1 = torch.softmax(output, dim=1)
    probability = softmax1[0][predicted.item()]

    #if the probability of it being the right match is over 75%, it will return one of the correct responses randomly
    #if not, then it will return a message informing the user that it did not understand the input
    if probability.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    else:
        return "I'm sorry but i do not seem to understand you."+"\n"+"Please ask me a question about an illness that you want to learn more about! Until then I will remain on standby"

def getTag(userInput):
    #this function is the same as the getBotInput() function 
    #but instead it returns the tag 


    sentence = tokenizeWords(userInput)
    Xaxis = bagOfWords(sentence, allWords)
    Xaxis = Xaxis.reshape(1, Xaxis.shape[0])
    Xaxis = torch.from_numpy(Xaxis).to(device)
    output = model(Xaxis)
    _,predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    #if the tag is the "goodbye" tag then it will return "Offline" and if not, it will return "Online"
    #this is used in Bot.py to change the "Online/Offline" label
    if tag == "goodbye":
        return "Offline"
    else:
        return "Online"
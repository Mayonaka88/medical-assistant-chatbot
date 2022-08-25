#json is to read the dataset, random is to get a random number, and numpy is used for arrays 
import numpy as np
import random
import json
#torch is to process and train data
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
#nltk_utils is used for stemming while model has the layers of the neural network
from stem import bagOfWords, tokenizeWords, stemWords
from nnModel import NeuralNet


#we load the files using json
#change "c:/Users/abdal/Desktop/Ai project/bot/intents.json" to your intents.json directory for the code to work
with open('c:/Users/abdal/Desktop/Ai project/bot/intents.json', 'r') as f:
    intents = json.load(f)

#these are the arrays we will use to process the data
tags = []
allWords = []
xy = []

#we use a loop to go through each sentence in our intents patterns
for intent in intents['intents']:
    tag = intent['tag']
    #we extract the tag and add it to the list
    tags.append(tag)
    for pattern in intent['patterns']:
        #we tokenize the words in the sentence
        rootWords = tokenizeWords(pattern)
        #we add them to our words list
        allWords.extend(rootWords)
        #we add the corrisponding xy pair to the xy pair list
        xy.append((rootWords, tag))

#we stem each word and we turn them into lowercase
#we ignore some characters
ignoreWords = ['?', '.', '!']
allWords = [stemWords(words) for words in allWords if words not in ignoreWords]
#we sort out the list and remove any dublicates
allWords = sorted(set(allWords))
tags = sorted(set(tags))



#here we create training data
x_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    #X is used for the bag of words for each pattern_sentence
    bag = bagOfWords(pattern_sentence, allWords)
    x_train.append(bag)
    #y is used for the tags
    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

#here are the parameters for the training process
epochs = 1000
learningRate = 0.001
batchSize = 8
inputSize = len(x_train[0])
hiddenSize = 8
outputSize = len(tags)

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    #dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    #we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

#here is where we load the dataset to train
dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batchSize, shuffle=True, num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(inputSize, hiddenSize, outputSize).to(device)

#here is where we calculate loss and define optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)

#here is where we train the model
for epoch in range(epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        #here we preform forward passing
        outputs = model(words)
        loss = criterion(outputs, labels)
        
        #then we do backwrd passing and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')


print(f'final loss: {loss.item():.4f}')

#here is where the data variables are saved
data = {
"model_state": model.state_dict(),
"input_size": inputSize,
"hidden_size": hiddenSize,
"output_size": outputSize,
"all_words": allWords,
"tags": tags
}

#here is where the data is saved on the computer
#change "c:/Users/abdal/Desktop/Ai project/bot/data.pth" to your directory for the code to work
FILE = "c:/Users/abdal/Desktop/Ai project/bot/data.pth"
torch.save(data, FILE)

print(f'training complete. file saved to {FILE}')

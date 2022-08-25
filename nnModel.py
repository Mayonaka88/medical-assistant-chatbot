import torch
#torch.nn provides functions to create neural networks that processes text data
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, inputSize, hiddenSize, numOfClasses):
        super(NeuralNet, self).__init__()
        #We create 3 linear function layers that applies linear transformation to the data
        self.layer1 = nn.Linear(inputSize, hiddenSize) 
        self.layer2 = nn.Linear(hiddenSize, hiddenSize) 
        self.layer3 = nn.Linear(hiddenSize, numOfClasses)
        #this layer applies a linear function on the indiviual elements and not the data as a whole
        self.reluLayer = nn.ReLU()
    
    def forward(self, x):
        #In here, we pass the data through each of the layers. between each layer we pass the data through the ReLU layer
        out = self.layer1(x)
        out = self.reluLayer(out)
        out = self.layer2(out)
        out = self.reluLayer(out)
        out = self.layer3(out)
        #no activation and no softmax at the end
        return out
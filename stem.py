#we use PorterStemmer to find the root form of a word
import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

#this is the object that will do the stemming
stemming = PorterStemmer()

def tokenizeWords(sentence):
    
    #we split the sentences into an array of tokens which can be words or letters or even parts of a sentence
    return nltk.word_tokenize(sentence)


def stemWords(word):
    
    #here we go through the procees of stemming which is to find the root form of the word
    return stemming.stem(word.lower())


def bagOfWords(tokenizedSentence, words):
    
    #Here we return the "bag of words" array which is an array of 1s and 0s
    #1 means that the known word exists in a sentence while 0 means it is not

    # stem each word
    wordsInSentence = [stemWords(element) for element in tokenizedSentence]
    # initialize bag with 0 for each word
    bagOfWords = np.zeros(len(words), dtype=np.float32)
    for idex, words1 in enumerate(words):
        if words1 in wordsInSentence: 
            bagOfWords[idex] = 1

    return bagOfWords
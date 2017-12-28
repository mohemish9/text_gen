PUNCTUATION = [".", "!", "?"]
def dollarify(wordList, k):
    """ dollarify takes adds a given nubmer of "$" sings in the begining of each sentence in a given list of words
        input: wordlist, a list of words
               k, number of dollar signs desired to be added at the begining of each sentence
        output: a list of words with k dollar signs at the begining of each sentence
    """
    output=[]
    sentence=[]
    for x in range(len(wordList)):
        sentence = sentence + [wordList[x]]
        for y in range(len(wordList[x])):
            if wordList[x][y] in PUNCTUATION:
                output = output + ["$"] *k + sentence
                sentence=[]
    return output

def markov_model(wordList, k):
    """marvok_model builds a dictonary with keys of len k, each key coresponds to the words that come after the words in the key
       input: wordlist, a list of words
              k, the len of keys of the dic
       output: a dictionary which has key pointing to the words the come after them
    """
    output={}
    dollarified= dollarify(wordList,2)
    for x in range(len(dollarified)-k):
        if False not in list(map(lambda y: y not in dollarified[x], PUNCTUATION)) and dollarified[x+k] != "$" and dollarified[x+k] != " " and " " not in tuple(dollarified[x:x+k]):
            if tuple(dollarified[x:x+k]) in output:
                output[tuple(dollarified[x:x+k])].append(dollarified[x+k])
            else:
                output[tuple(dollarified[x:x+k])]= list([dollarified[x+k]])
    return output

import random
def gen_from_model(mmodel, numwords):
    """ gen_from_model genrates a number of given words from a given markov model
        input: mmodel, the dictionary (markov model) used to generate words
               numwords, the number of desired words
        output: N/A (prints a genrated text of length numwords and follows mmodel)
    """
    mmOrder=list(map(len,mmodel))[0]
    key= tuple("$" * mmOrder)
    for x in range(numwords):
        word= random.choice(mmodel[key])
        print(word, end=' ')
        if False not in list(map(lambda y: y not in word, PUNCTUATION)):
            key= key[1:len(key)]+ (word,)
        else:
            key= tuple("$" * mmOrder)

def markov(fileName, k, length):
    """ markov uses all the privious functions to genrate a text from another given file
        input: fileName, the file from which the markov model will be genrated
               k, the model parameter
               length, number of words printed
        output N/A (prints text)
    """
    inputfile= open(fileName, "r")
    text = str(inputfile.readlines())
    inputfile.close()
    model= markov_model(text.split(), k)
    gen_from_model(model,length)
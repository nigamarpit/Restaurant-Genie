import nltk
import json
#import FinalProfWay

#Noun Phrase Words
npWords = []

#Attributes
nlu_cuisine=''
nlu_rating=''
nlu_price=''
nlu_location=''

bigramFirstWord=''
bigramCityFirstWord=''

wordbigramList=['Eastern',
'Fast',
'Frozen',
'Hookah',
'Hot',
'Ice',
'Korean',
'Latin',
'Noodle',
'Pacific',
'Pan',
'Pub',
'South'
]

citybigramList=[
    'Los',
    'Santa',
    'San',
    'Beverly',
    'Culvery'
]

#Provide Info Dictionary
#provideInfo={}

attributesModelPath='attributes_model.txt'
attributesModel=open(attributesModelPath, 'r')

with attributesModel as model:
    attributesModelDict = json.load(model)

def parseNounPhrases(posTags,grammar):
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(posTags)
    return result

def traverse(t):
    try:
        t.label()
    except AttributeError:
       if(1 == -1):
           print("")
    else:
        if(t.label()=='NP'):
            for child in t:
                npWords.append(child[0])
        for child in t:
            traverse(child)

def checkCuisine(word):
    global nlu_cuisine
    global bigramFirstWord
    if(bigramFirstWord=='' and word in wordbigramList):
        bigramFirstWord=word
        return
    if(bigramFirstWord!=''):
        newword=bigramFirstWord+' '+word
        if(newword in attributesModelDict["cuisine"]):
            nlu_cuisine=newword
            return
    if(word.title() in attributesModelDict["cuisine"]):
        nlu_cuisine=word
        return

def checkPrice(word):
    global nlu_price
    if(word.lower() in attributesModelDict["price"]["cheap"]):
        nlu_price="cheap"
    elif(word.lower() in attributesModelDict["price"]["expensive"]):
        nlu_price="expensive"
    elif(word.lower() in attributesModelDict["price"]["midlevel"]):
        nlu_price="moderate"
    #else:
    #    price="dnc"

def checkRating(word):
    global nlu_rating
    if(word in attributesModelDict["rating"]):
        if('Any' in word):
            nlu_rating=-1
        else:
            nlu_rating=int(word)

def checkLocation(word):
    global nlu_location
    global bigramCityFirstWord
    if(bigramCityFirstWord=='' and word in citybigramList):
        bigramCityFirstWord=word
        return
    if(bigramCityFirstWord!=''):
        newword=bigramCityFirstWord+' '+word
        if(newword in attributesModelDict["location"]["City"]):
            nlu_location=newword
            return
    if(word in attributesModelDict["location"]["City"]):
        nlu_location=word
        return


def getCuisine():
    return nlu_cuisine

def getPrice():
    return nlu_price

def getRating():
    return nlu_rating

def getLocation():
    return nlu_location

def parseInput(inp):
    #input(inp)
    global nlu_cuisine
    global nlu_price
    global nlu_location
    global nlu_rating
    global bigramFirstWord
    provideInfo={}
    userInput = nltk.word_tokenize(inp)
    npWords.clear()

    posTags=nltk.pos_tag(userInput)

    #print(posTags)

    grammar = r"""NP: {<CD><NN>}
                      {<DT>?<JJ>*<NN>}
                      {<DT>?<JJ>*<NNP>}
                      {<NNP>+}
                      {<CD>+}
                      {<NNP>}
                      {<NN>}
                      {<DT>}
                      {<NN>+}
                      {<DT>+}
                      {<JJ>}
                      {<JJ>+}
                       """
    posTree=parseNounPhrases(posTags,grammar)

    traverse(posTree)

    for word in npWords:
        checkCuisine(word)
        checkPrice(word)
        checkRating(word)
        checkLocation(word)

    if(nlu_cuisine!=''):
        provideInfo['cuisine']=nlu_cuisine
    elif(nlu_price!=''):
        provideInfo['price']=nlu_price
    elif(nlu_rating!=''):
        provideInfo['rating']=nlu_rating
    elif(nlu_location!=''):
        provideInfo['location']=nlu_location

    if(len(provideInfo)==0):
        provideInfo['status']='noresult'
    nlu_cuisine=''
    nlu_price=''
    nlu_rating=''
    nlu_location=''
    return provideInfo

'''if __name__ == "__main__":



#    if(cuisine!=''):
#        provideInfo['cuisine']=cuisine
#        print(cuisine)
#    elif(price!=''):
        provideInfo['price']=price
    elif(nlu_rating!=''):
        provideInfo['nlu_rating']=nlu_rating
    elif(location!=''):
        provideInfo['location']=location

    #DialogManager(provideInfo)'''



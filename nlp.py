import nltk 
#nltk.download('punkt') 
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('stopwords') 
#this will download all data 
#nltk.download() 

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, names
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer 

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier



text = 'Peter is happy and this is a happy day. However, the class was such a boring one.' 
phrases = sent_tokenize(text)
words = word_tokenize(text)

print("**************************************")
print(phrases)
print("**************************************")
print(words)
print("**************************************")
# tag words, verbs, noun, etc 
tagged = nltk.pos_tag(words)
print(tagged)
print("**************************************")
entities = nltk.chunk.ne_chunk(tagged)
#print(entities)
#print("**************************************")

stopWords = set(stopwords.words('english'))
wordsFiltered = []
 
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
 
print(wordsFiltered)
print("**************************************")

'''
ps = PorterStemmer()
 
for word in words:
    print(ps.stem(word))
print("**************************************")
''' 

def word_feats(words):
    return dict([(word, True) for word in words])
 
positive_vocab = [ 'happy', 'nice', ':)' ]
negative_vocab = [ 'bad', 'boring', ':(' ]
neutral_vocab = [ 'day','however','class','was','is'] 
 
positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
 
train_set = negative_features + positive_features + neutral_features
 
classifier = NaiveBayesClassifier.train(train_set) 
 
# Predict
neg = 0
pos = 0
text = text.lower()
words = text.split(' ') 
for word in words:
    classResult = classifier.classify(word_feats(word)) 
    if classResult == 'neg':
        neg = neg + 1
    if classResult == 'pos':
        pos = pos + 1
 
print('Positive: ' + str(float(pos)/len(words)))
print('Negative: ' + str(float(neg)/len(words)))
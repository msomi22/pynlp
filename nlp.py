import nltk 
#nltk.download('punkt') 
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')


from nltk import word_tokenize


text = 'peter is happy, this is a happy day, it was such a boring class' 
tokens = word_tokenize(text) 
print(tokens)
tagged = nltk.pos_tag(tokens)
print("**************************************")
print(tagged)
entities = nltk.chunk.ne_chunk(tagged)
print("**************************************")
print(entities)








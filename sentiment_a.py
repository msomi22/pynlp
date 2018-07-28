'''

'''

from nltk.sentiment.vader import SentimentIntensityAnalyzer 

sentences = ['Peter is happy and this is a happy day.','However, the class was such a boring one.'] 
sentences = ['The trip was such a boring one, i dont think i would attend another.','That food was not bad.']  

sid = SentimentIntensityAnalyzer()
for sentence in sentences:
	print(sentence)
	ss = sid.polarity_scores(sentence)
	for k in sorted(ss):
		print('{0}: {1}, '.format(k, ss[k]) )   






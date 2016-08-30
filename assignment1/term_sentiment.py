import sys
import re
import json

scores = {}
newscores = {}
instances = {}

def scores(file1):
	for line in file:
		term, score = line.split("\t")
		score[term] = int(score) #to add term and it's score in a form of python dictionary

def scoretweets(file2):
	tweet_count = 1
	for line in file2:
		tweet_score = 0
		res = json.loads(line) #load each line of json seperately in form of dictionary
		string = res.get('text','zz').encode("ascii","ignore") #get the value of key "text" and encode in ascii
		new_words = []
		words = string.strip().split() #take out words from string
		for word in words:
			word = word.encode('utf-8')
			word_score = int(scores.get(word,10000)) #check if word is present in corpus
			if word_score == 10000:
				new_words.append(word) #if word is not in the corpus then add it in new_words list
			else:
				tweet_score += word_score
		for word in new_words:
			newscores[word] = newscores.get(word,0) + tweet_score # for new words the term sentiment equals to sentiment scoreof full tweet
		tweet_count += 1

def display_words():
	for key, value in sorted(newscores.iteritems(), key=lambda (k,v): (v,k)):
			print "%s %s" % (key, value)

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores(sent_file)
    scoretweets(tweet_file)
    display_words()
if __name__ == '__main__':
    main()

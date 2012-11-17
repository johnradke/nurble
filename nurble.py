# nurble.py by http://twitter.com/johnradke
import nltk

ok = ['NN', 'NNP', 'NNS']
punc = [',', '.', '!', '?']

def nurbword(taggedWord):
  if taggedWord[1] in ok + punc: return taggedWord[0]
  return 'nurble'

def untok(words):
  return "".join(words[0:1] + [w if w in punc else " " + w for w in words[1:]])

#############################

f = open('sotu.txt')
sotu = f.read()
f.close()

sentences = nltk.tokenize.sent_tokenize(sotu)

taggedSentences = [nltk.pos_tag(nltk.word_tokenize(s)) for s in sentences]

nurbled = open('nurbled.txt', 'w')
nurbled.write(" ".join(untok([nurbword(w) for w in s]) for s in taggedSentences))
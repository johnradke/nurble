# nurble.py by http://twitter.com/johnradke
import nltk
import sys
import string

ok = ['NN', 'NNP', 'NNS']
punc = [',', '.', '!', '?']

def nurbword(taggedWord):
  if taggedWord[1] in ok + punc: return taggedWord[0].upper()
  if taggedWord[0][0] in string.uppercase: return 'Nurble'
  return 'nurble'

def untok(words):
  return "".join(words[0:1] + [w if w in punc else " " + w for w in words[1:]])

#############################

f = open(sys.argv[1])
originalText = f.read()
f.close()

sentences = nltk.tokenize.sent_tokenize(originalText)

taggedSentences = [nltk.pos_tag(nltk.word_tokenize(s)) for s in sentences]

print " ".join(untok([nurbword(w) for w in s]) for s in taggedSentences)
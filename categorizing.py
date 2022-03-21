from matplotlib.image import NonUniformImage
from getspeech import wordlist
from collections import Counter
verb = open(file="31K verbs.txt").read()
verblist=verb.split()
noun = open(file="91K nouns.txt").read()
nounlist=noun.split()
adj = open(file="28K adjectives.txt").read()
adjlist=adj.split()
adv = open(file="6k adverbs.txt").read()
advlist=adv.split()

trumpverblist=[]
for words in wordlist: 
    if words in verblist and words not in nounlist:
        trumpverblist.append(words)
trumpverbdic=Counter(trumpverblist)


trumpnounlist=[]
for words in wordlist: 
    if words in nounlist:
        trumpnounlist.append(words)
trumpnoundic=Counter(trumpnounlist)


trumpadjlist=[]
for words in wordlist: 
    if words in adjlist:
        trumpadjlist.append(words)
trumpadjdic=Counter(trumpadjlist)


trumpadvlist=[]
for words in wordlist: 
    if words in advlist:
        trumpadvlist.append(words)
trumpadvdic=Counter(trumpadvlist)

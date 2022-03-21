import random
from getspeech import linelist
from categorizing import trumpverblist, trumpadjlist,trumpadvlist,trumpnounlist
gesture=["[while lifting his tiny hands]","[while lifting his pinky]","[while rasing his eye brow]","[staring at the audience]","[frowing]","[while having a smirking smile]","China, China, China","Wall, Wall, Wall"]
punctuation=[".","!!","?","...","!","!!!!!"]
def anothergenerator(lines): #how many lines of speech you wanna generator
    for i in range(0,lines):
        ind=random.randint(0, len(linelist))
        ges=random.choice(gesture)
        punt=random.choice(punctuation)
        newline=linelist[ind-1]
        for words in newline.split():
            newwords=random.choice(trumpverblist)
            if words in trumpverblist:##change the verb portion of the speech
                newline=linelist[ind-1].replace(words, newwords)
                for nouns in newline.split(): ##change the noun of the speech
                    newnouns=random.choice(trumpnounlist)
                    if nouns in trumpnounlist:
                        newline=newline.replace(nouns, newnouns)

        print(newline+punt,ges+".")
        print()

    

anothergenerator(10)
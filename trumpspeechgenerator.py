import random
from categorizing import trumpadjlist, trumpadvlist, trumpverblist, trumpnounlist
def trumpspeechgenerator(lines): ##lines: how many lines of speech intended to generator
    ##I used list than Counter because the frequency of words is built in the list
    for i in range(0,lines):
        verb=random.choice(trumpverblist)
        subject=random.choice(trumpnounlist)
        object=random.choice(trumpnounlist)
        adv=random.choice(trumpadvlist)
        subjectadj=random.choice(trumpadjlist)
        objectadj=random.choice(trumpadjlist)
        t=random.randint(1,7)
        if t==1: ##with subject adj and adv
            print(subjectadj,subject, verb, adv, object)
        if t==2: ##with subject adj no adv
            print(subjectadj,subject, verb, object)
        if t==3: ###with object adj and adv
            print(subject, verb,adv, objectadj, object)
        if t==4: ###with object adj no adv
            print(subject, verb, objectadj, object)
        if t==5: ##no adj with adv
            print(subject, verb, adv, object)
        if t==6: ##no adj nor adv
            print(subject, verb, object)
        if t==7: ##with subjectajd, objectadj and adv
            print(subjectadj,subject, verb, adv, objectadj, object)

    
trumpspeechgenerator(5)

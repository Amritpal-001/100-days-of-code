#problem 41

import random
n = [1,2,3,4,5,6,7,8,9]


def randnumgeneratorXdigitNum(x):
    b = ''
    a = n[:x]
    for i in range(0,len(a)):
        random_num = random.choice(a)
        a.remove(random_num)
        b += str(random_num)
    print(b)
    

#randnumgeneratorXdigitNum(4)

x = 4

def factorial(x):
    a = 1
    for i in range(1, x+1):
        a *= i
    #print(a)
    return(a)

factorial(4)


def randnumgeneratorXdigitNum(x):
    Allpossibilites = []
    #while (len(Allpossibilites)) <= factorial(x):
    while (len(Allpossibilites)) <= (factorial(x) - 1):
        b = ''
        a = n[:x]
        for i in range(0,len(a)):
            random_num = random.choice(a)
            a.remove(random_num)
            b += str(random_num)
        #print(b)
        if b not in Allpossibilites:
            Allpossibilites.append(b)
    print(Allpossibilites)
    return(Allpossibilites)
        
randnumgeneratorXdigitNum(8)


'''
b = []
for i in range(1,8):
    a = randnumgeneratorXdigitNum(i+1)
    b += a

print(len(b))
    
'''

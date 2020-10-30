UpperCap = 100

def PrimeListSieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and  initialize all entries it as true. A value
    # in prime[i] will finally be false if i is  Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    a = []
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            a.append(p)
            c += 1
    return (c, a)

NoofPrime = PrimeListSieveOfEratosthenes(10 ** 6)[0]
#print("Total prime numbers in range:", NoofPrime)
PrimeList = PrimeListSieveOfEratosthenes(10 ** 6)[1]
#print(len(PrimeList))
#print(PrimeList)

def PrimeTest(num):
    if num in PrimeList:
        #print("true")
        return(True)
    else:
        return(False)

PrimeTest(98378)

def ReplacementVariableListPerNumber(Num):
    # Make num with al possible replacement variables
    # replacementVariable will be string with a,b options in it that cab be replaced
    replacementVariableList = []
    if Num >= 100000:
        Num = str(Num)
        for i in range(1, len(Num)+1 ):
            for j in range(1, len(Num)+1 ):
                if i != j:
                    Num1 = Num[:(i-1)] + 'a' + Num[i:]
                    #print(Num1)
                    Num2 = Num1[:j-1] + 'b' + Num1[j:]
                    #print(Num2)
                    #if Num2[0] != 0:
                    if Num2 not in replacementVariableList:
                            replacementVariableList.append(Num2)
        #print(replacementVariableList)
        #print(len(replacementVariableList))
    return(replacementVariableList)


def ReplaceAandBwithNumber(replacementVariable , a , b):
    firstNum = str(a)
    SecondNum = str(b)
    replaced = replacementVariable.replace('a' , firstNum)
    replaced = replaced.replace('b', SecondNum)
    #print(replaced)
    return(replaced)

def ReplaceAwithNumber(replacementVariable , a):
    firstNum = str(a)
    replaced = replacementVariable.replace('a' , firstNum)
    #print(replaced)
    return(replaced)
#print(ReplaceAandBwithNumber('a234b' , 9 , 5))


'''for x in replacementVariableList:
    print(ReplaceAandBwithNumber(x, 9, 5))'''

def AllReplacementCombination(replacementVariable):
    # generate all possible numbers with these Replcament varaibles
        ithEntireList = []
        for FirstNum in range(0,9):
                SecondNum = FirstNum
                #for SecondNum in range(0,9):
                newNum = ReplaceAandBwithNumber(replacementVariable , FirstNum , SecondNum)
                newNum = int(newNum)
                #print(replacementVariable , newNum , SecondNum , FirstNum)
                #ithEntireList.append(newNum)
                if newNum not in ithEntireList:
                    if newNum in PrimeList:
                        #print(newNum)
                        ithEntireList.append(newNum)
        return ithEntireList

replacementVariableList = ReplacementVariableListPerNumber(156003)
print(replacementVariableList)
print(AllReplacementCombination(replacementVariableList[19]) , replacementVariableList[19])

'''
#print(len(a))
#print(a)
MainList = []

for x in PrimeList:
    #print(x , x, x)
    if x >= 120000:
        ReplacementVariableListPerNumbers = ReplacementVariableListPerNumber(x)
        #print(ReplacementVariableListPerNumbers   , 'amrit')
        for a in ReplacementVariableListPerNumbers:
            #print(a  , 'amrit')
            AllReplacementCombinationPerVariable = AllReplacementCombination(a)
            #print(AllReplacementCombinationList)
            if len(AllReplacementCombinationPerVariable) >=6:
                MainList.append(AllReplacementCombinationPerVariable)
                print(AllReplacementCombinationPerVariable , x)
        if (x - 120000)% 1000 ==0:
            print(x)
print(MainList)
print(len(MainList))'''

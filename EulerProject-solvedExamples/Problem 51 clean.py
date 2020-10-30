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

PrimeList1 = PrimeListSieveOfEratosthenes(2 * 10 ** 5)[1]

Startvalue = 50000

PrimeList = []
for a in PrimeList1:
    #print(a)
    if a >= Startvalue:
        PrimeList.append(a)

#print(PrimeList)


testlist = [50021, 51121, 52221, 53321, 54421, 55521, 56621, 57721, 58821 , 56003]

for i in testlist:
    if i in PrimeList:
        print(i)

def ReplacementVariableListPerNumber(Num , Startvalue = Startvalue):
    replacementVariableList = []
    if Num >= Startvalue:
        if Num in PrimeList:
            Num = str(Num)
            for i in range(1, len(Num)+1 ):
                for j in range(1, len(Num)+1 ):
                    if i != j:
                        Num1 = Num[:(i-1)] + 'a' + Num[i:]
                        Num2 = Num1[:j-1] + 'a' + Num1[j:]
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

def AllReplacementCombination(replacementVariable):      # generate all possible numbers with these Replcament varaibles
        ithEntireList = []
        ithPrimeLIst = []
        for FirstNum in range(0,9):
                    newNum = ReplaceAwithNumber(replacementVariable , FirstNum)
                    newNum = int(newNum)

                    #if newNum in PrimeList:
                    if newNum not in ithEntireList:
                            ithEntireList.append(newNum)
        for i in ithEntireList:
            if i in PrimeList:
                ithPrimeLIst.append(i)
        return ithPrimeLIst

replacementVariableList = ReplacementVariableListPerNumber(196831)
print(replacementVariableList)

for i in range(0 , len(replacementVariableList)):
    print(AllReplacementCombination(replacementVariableList[i]) , replacementVariableList[i])
    if len(AllReplacementCombination(replacementVariableList[i])) >= 1:
        print(min(AllReplacementCombination(replacementVariableList[i])))



#print(len(a))
#print(a)
MainList = []
for x in PrimeList:
    #print(x , x, x)
    if x >= Startvalue:
        ReplacementVariableListPerNumbers = ReplacementVariableListPerNumber(x)
        #print(ReplacementVariableListPerNumbers   , 'amrit')
        for a in ReplacementVariableListPerNumbers:
            #print(a  , 'amrit')
            AllReplacementCombinationPerVariable = AllReplacementCombination(a)
            #print(AllReplacementCombinationList)
            try:
                if len(AllReplacementCombinationPerVariable) >=7:
                        if min(AllReplacementCombinationPerVariable) >= x :
                            MainList.append(AllReplacementCombinationPerVariable)
                            print(AllReplacementCombinationPerVariable , x , a)
                            #exit()
            except:
                pass
        if (x - 120000)% 1000 ==0:
            print(x)
#print(MainList)
print(len(MainList))

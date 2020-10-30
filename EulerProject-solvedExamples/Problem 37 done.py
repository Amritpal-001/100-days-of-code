#problem 37
# Python Program to find prime numbers in a range 
import time 
def SieveOfEratosthenes(n): 
    # Create a boolean array "prime[0..n]" and  initialize all entries it as true. A value  
    # in prime[i] will finally be false if i is  Not a prime, else true. 
    prime = [True for i in range(n+1)] 
      
    p = 2
    while(p * p <= n): 
           
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
    return (c , a)
  
t0 = time.time() 
NoofPrime = SieveOfEratosthenes(10**5)[0]
print("Total prime numbers in range:", NoofPrime) 
PrimeList = SieveOfEratosthenes(10**5)[1]

t1 = time.time() 
print("Time required:", t1 - t0)


'''
def truncatedlEFTTORIGT(x):
    mylist = []
    for a in range(len(str(x))):
        mylist.append(x%(10**(a+1)))
    print(mylist)
    b= 0
    for i in mylist:
        if i in PrimeList:
            b += 1
    if len(mylist) == b:
        return(True)

print(truncatedlEFTTORIGT(3797))

def truncatedRIGTTOleFT(x):
    mylist = []
    for a in range(len(str(x))):
        d = (10**(a))
        c = (x - (x%(10**(a)) )) 
        a = c / d 
        mylist.append(int(a))
        print( c , d  , x)   
    print(mylist)
    b= 0
    for i in mylist:
        if i in PrimeList:
            b += 1
    if len(mylist) == b:
        return(True)

print(truncatedRIGTTOleFT(3797))

'''

def truncatedBothWay(x):
    mylist = []
    for a in range(len(str(x))):
        mylist.append(x%(10**(a+1)))
    for a in range(len(str(x))):
        d = (10**(a))
        c = (x - (x%(10**(a)) )) 
        a = c / d
        if int(a) not in mylist:
            mylist.append(int(a))
    #print(mylist)
    b= 0
    for i in mylist:
        if i in PrimeList:
            b += 1
    if len(mylist) == b:
        return(True)

#print(truncatedBothWay(3797))
c = []
#while len(c) <=11:
for i in range( 1 , len(PrimeList)):
        if i%1000 == 0:
            print(i)
        if truncatedBothWay(PrimeList[i]) == True:
            if PrimeList[i] not in c:
                if PrimeList[i] >= 10:
                    c.append(PrimeList[i])
                    print("Prime    --- " , PrimeList[i])


c.append(739397)
print(len(c))

t1 = time.time() 
print("Time required:", t1 - t0) 
z = 0
for i in c:
    z += i

print(z)

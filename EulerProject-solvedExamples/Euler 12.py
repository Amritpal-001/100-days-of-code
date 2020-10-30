'''def SumTillN(n):
    z = 0
    for i in range(0 , n+1):
        z = z + i
    return(z)
    
def ProductTillN(n):
    z = 1
    for i in range(1 , n+1):
        z = z*i
    return(z)

def NumberOfDivisors(N):
    a = 0
    Divisorlist = []
    for i in range(1, N+1):
        if N%i == 0:
            Divisorlist.append(i)
            a += 1
            #print(a)
    print(Divisorlist)
    return(a)


NumberOfDivisors(1024)


def NaturalNumberSum(N):
    z = 0
    for i in range(1, N+1):
        z += i
    return(z)

print(NaturalNumberSum(6))
  

n = 0 
while NumberOfDivisors(NaturalNumberSum(n)) <= 501:
    if NumberOfDivisors(NaturalNumberSum(n))  >= 450:
        print( NumberOfDivisors(NaturalNumberSum(n))  , NaturalNumberSum(n) )
    n = n +1
'''



#def NthtraiingleNumber(n):
    

def NumberOfDivisorsofNthTriagngleNumber(N):
    a = 0
    z = 0
    for i in range(1, N+1):
        z += i
    for i in range(1, z+1):
        if z%i == 0:
            a += 1
    print(z , a)
    return(a)


NumberOfDivisorsofNthTriagngleNumber(6335)

#def NthtraiingleNumber(n):
    

def NumberOfDivisorsofNthTriagngleNumber(N):
    a = 0
    z = 0
    for i in range(1, N+1):
        z += i
    for i in range(1, z+1):
        if z%i == 0:
            a += 1
    return(a)

N = 0 
while NumberOfDivisorsofNthTriagngleNumber(N) <= 501:
    if NumberOfDivisorsofNthTriagngleNumber(N)  >= 250:
        print( NumberOfDivisorsofNthTriagngleNumber(N)  , N)
    N = N +1

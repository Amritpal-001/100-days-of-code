#Euler 21
def SumofProperdivisors(n):
    z = 0
    for i in range(1,n):
        if n%i == 0:
            #print(i)
            z = z + i
    return(z)
a = 0         
for i in range(1, 10000):
  
    if SumofProperdivisors(SumofProperdivisors(i)) == i :
        if i != SumofProperdivisors(i):
            b = i + SumofProperdivisors(i)
            a = a + b
            print(a , i , SumofProperdivisors(i) )

answer= a/2
print(answer)

#Euler 16

a = str(2**1024)
print(len(a))
 
def nthletter(x , n):
    a = ((x%(10**n)) - x%(10**(n-1)))/10**(n-1)
    #print(int(a))
    return(int(a))


#nthletter(153 , 3)

def factorial(n):
        z = 1
        for i in range(1 , n+1):
                z = z * i
        return(z)

b = factorial(100)
a = int(b)

z = 0
for i in range (len(str(a))):
    z = z + nthletter(a , (i+1))
    #print(a , len(str(a)) , i , z)

print(z)

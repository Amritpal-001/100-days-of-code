#Euler 16

a = str(2**1024)
print(len(a))
 
def nthletter(x , n):
    a = ((x%(10**n)) - x%(10**(n-1)))/10**(n-1)
    #print(int(a))
    return(int(a))


#nthletter(153 , 3)
a = 2**1000
z = 0
for i in range (len(str(a))):
    z = z + nthletter(a , (i+1))
    #print(a , len(str(a)) , i , z)

print(z)

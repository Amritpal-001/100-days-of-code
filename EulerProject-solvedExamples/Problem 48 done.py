a = 0
N = 1000  #sum till....
n = 10  #number of last digits required

for i in range(1,  N+1):
    a = a + i**i
    #print(a)

b = a %(10**(n))
print(b)

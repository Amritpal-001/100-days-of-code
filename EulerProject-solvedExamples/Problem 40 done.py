#PRolem 40

x = ''

for n in range(1 , 1000000):
    x += str(n)
    #print(x)

print(len(x))
print(x[10])

a = 1
for i in range(0,7):
    n = 10**i - 1

    a *= int(x[n])
    print(n , x[n] , a )

print(a)

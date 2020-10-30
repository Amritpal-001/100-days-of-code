asd = 10
print(asd)

def Chainlength(x):
    b = 0
    while x != 1:
        if x%2 == 1:
            x = int(3*x + 1)
            b = b + 1
        if x%2 == 0:
            x = int(x/2)
            b = b + 1
    #print("chain length" , b)
    return(b)

i = 0

while i < 10:
    z = Chainlength(i)
    print(z)
    b = 1
    a = 1
    if z > b:
        b = z
        a = i
    i = i + 1
    print(i , a ,b )

print(b , a)
        

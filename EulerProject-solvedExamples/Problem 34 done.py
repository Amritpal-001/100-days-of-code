#Euler 34

def factorial(x):
    a = 1
    for i in range(1,x+1):
        a = a * i
    #print(a)
    return(a)

factorial(5)
print(factorial(9))


a = str(123)
print(a[1])

def factorialsum(x):
    c = 0
    for a in range(0, len(str(x))):
        b = factorial(int(str(x)[a]))
        c = c + b
    #print(c)
    return(c)

factorialsum(145)


def AllcuriousnumbersXtoY(x , y):
    ListofCuriousNumbers = []
    for i in range(x , y):
        if factorialsum(i) == i:
            print(i)
            if i not in ListofCuriousNumbers:
                ListofCuriousNumbers.append(i)
    print(ListofCuriousNumbers)
    return(ListofCuriousNumbers)



#assumption made here us that 999999 will be more or less smaller than 6(!9)
## Not really clear why i used 10**6 and not 10**7
a = AllcuriousnumbersXtoY(1, 10**6)

c = 0
for b in range(a[2:], len(a)):
    c = c + b

print(c)
    

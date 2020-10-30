def mydivisor(a):
    divisor = []
    i = 1
    while i < a :
        if a % i == 0 :
            divisor.append(i)
        i += 1
    return(divisor)

a = mydivisor(28)
print(a)        


def sumdivisor(a):
   b = mydivisor(a)
   d = 0
   for i in range(len(b)):
       d += b[i]
   return(d)

c = sumdivisor(32)
print(c)

def abundantnumberlist(n):
    mylist = []
    for i in range(n):
        a = sumdivisor(i)
        b = mydivisor(i)
        if a > n :
            mylist.append(i)
    return(mylist)

c = abundantnumberlist(200)
print(c)

def sumofallthatCantBeWrittenAsSumOfTwoAbundantNUmbersbelowNNNN(n):
    a = abundantnumberlist(n)
    b = sumdivisor(n)
    c = mydivisor(n)
    answer = 0
    d = []
    f = []

    for u in range (len(a)):
        for y in range (len(a)):
            e = a[u] + a[y]
            d.append(e)
    print(d)
    
    for i in range (n):
        if i in d:
            pass
        else:
            f.append(i)
            answer += i
            #print(i, u  , y , answer )
    print(answer)

c = abundantnumberlist(28123)
#sumofallthatCantBeWrittenAsSumOfTwoAbundantNUmbersbelowNNNN(28123)



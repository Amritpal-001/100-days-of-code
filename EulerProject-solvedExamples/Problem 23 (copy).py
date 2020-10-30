#Euler 23

def SumOfDivisors(n):
    z = 0
    for i in range(1, n):
        if n%i == 0:
            z = z + i
    #print(z)
    return(z)    
        
print(SumOfDivisors(28))
    
def abundantnumber(n):
    if SumOfDivisors(n) > n:
        #print(n ,"is a abundant number")
        return(True)
abundantnumber(12)


def AbundantNumbersBelowN(n):
    a =[]
    for i in range(1 , n):
        if abundantnumber(i) == True:
            a.append(i)
    return(a)

N = 28123
b = AbundantNumbersBelowN(N) 
print(len(b))

answer = 0
'''
def SumOfTwoAbuundantNumbersOrNot(n):
    for i in range(0, len(b)):
        for a in range(0, len(b)):
            if b[i] + b[a] <= n:
                if b[i] + b[a] == n:
                    #print("TRUE" , n )
                    return(True)


print(SumOfTwoAbuundantNumbersOrNot(24))

for i in range(1 , N):
    if SumOfTwoAbuundantNumbersOrNot(i) == True:
                       pass
    else:
        answer = answer + i
        print(answer)
    if i % 1000 == 0:
        print("Covered" , i)

print(answer )                       
'''

z = 0
ans = []
for i in range(1, len(b)):
    for a in range(1, len(b)):
        z = b[i] + b[a]
        if z <= N:
            if z not in ans:
                ans.append(z)
                #print(ans)
print("last round")
d = ans + b
c = 0
for i in range(1 , N):
    if i not in d:
        c = c + i
print(c)

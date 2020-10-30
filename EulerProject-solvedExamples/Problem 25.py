a = [1,1]
n = 2

while (a[-1] <= 10**999) :
    
    b = a[-1] + a[-2]
    a.append(b)
    n += 1
print(a[-1])
print(len(a))
print(n)

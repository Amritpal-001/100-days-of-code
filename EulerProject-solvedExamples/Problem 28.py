

p = 1001
answer = 1

for n in range (p,1,-2):
    b = n**2
    c = n**2 - (n -1) 
    d = n**2 - 2*(n -1) 
    e = n**2 - 3*(n - 1)
    answer += b + c + d + e
    #print(n ,answer)

print(answer)

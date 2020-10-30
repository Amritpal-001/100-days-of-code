def reverse(n):
    d= 0
    rev=0
    while n > 0 :
         d = n %10
         n = int(n/10)
         rev = (rev *10) + d    
    return rev  

r1 = 800
r2 = 999
answer = 0
#x = input ("Enter number")
#print(reverse(int(x)))
for x in range (r1 , r2):
    for y in range (r1,r2):
        a = int (x * y)
        b = reverse(a)
       # print (a , b )
        if a == b:
         print ("Answer is ", x , y , a , b)
         if answer < a:
           answer = a
           x1 = x
           y1 = y
print ("biggest palindrome " , answer , x1 ,y1)
        
         

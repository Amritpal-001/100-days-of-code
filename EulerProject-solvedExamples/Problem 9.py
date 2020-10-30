import time

starttime = time.time()
n = 1000
for a in range (1 , n):
    for b in range (1 , int(n - a*a)):
        for c in range (1, (n- (a*a) -(b*b)):
           if ((a*a) + (b*b) == (c*c)):
               if a + b + c == 1000:
                 print(a , b, c , (a*a) , (b*b) , (c*c) , a*b*c )
                 print (time.time() - starttime())
                 exit

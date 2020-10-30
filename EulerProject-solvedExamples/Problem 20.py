import time

start = time.time()
given = 100
product = 1
for n in range ( 1 , (given +1 ) ):
    product = product * n
 #   print (product)
m = 10
answer = 0
r1 = 0
r2 = (product % m ) 
while(product % m) != product:
 r1 = ((product % (10*m)) - (product % m))/m
 answer = answer + r1 
 m = m * 10
 #print (answer , r1 , r2 , m )
finalanswer = answer + (product % 10)
print (finalanswer)
end = time.time()
print ( end- start)

import time
n= 200000
answer = 0

start = time.time()
for num in range (2, n):
  if (num % 2) != 0:
    if (num % 3) != 0:
     #if (num % 5) != 0:
        for i in range(2, num):
            if (num % i) == 0:          
              break
        else:
            answer = answer + num
         #  print (answer , num)

end = time.time()
           
print("sum of primes below" , n , "is " , answer , "time =" , (end - start))


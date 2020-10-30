n= 600851475143
mylist = []
answer = 0

#while (len(mylist) - 1) < n :
 # num = num + 1
for num in range (1, n):  
  for i in range(2, num):
         if (num % i) == 0:
              
              break
  else:
           if (n % num) == 0:
            print ("prime factor of ", n , "is" , num)
            
            if answer < num:
             answer = num
print("largest prime factor of" , n , "is ", answer)


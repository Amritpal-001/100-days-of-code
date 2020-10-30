n=10001
mylist = []
num = 0
while (len(mylist) - 1) < n :
  num = num + 1
  for i in range(2, num):
         if (num % i) == 0:
              
              break
  else:
           mylist.append(num)
           print(num , len(mylist))
           
print(mylist[-1] , (len(mylist)-1))


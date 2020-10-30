import re

search_in_string = [""]
number = "123"

#number = input("type an email")
#number = "singh@gmail.com"
#pattern = "[a-zA-Z0-9]+@[a-zA-A]+\.(com|edu|net)"

'''
if (re.search(pattern , number)):
               print(re.search(pattern , number)[0] , "valid email")
else:
               print(re.search(pattern , number)[0] , "invlaid email")
#works fine
               
number = "ap4.singh@gmail.com"
if (re.search(pattern , number)):
               print(re.search(pattern , number)[0] , "valid email")
else:
               print(re.search(pattern , number)[0] , "invlaid email")
#unable to pick up complex email ids
'''


#Soutions - convert it to "not dot" version before processing in R
print(re.search(pattern , number))
number = "123"
pattern = re.compile(r"\d")     #result - <_sre.SRE_Match object; span=(0, 1), match='1'>
pattern = "\d\d\d"              #result - <_sre.SRE_Match object; span=(0, 3), match='123'>

import wget
import re
from datetime import datetime

#url = 'https://thisartworkdoesnotexist.com/'
#url = 'https://www.thispersondoesnotexist.com/'
url = 'https://thischemicaldoesnotexist.com/'

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

pattern = "[a-zA-A]+\.(com)"
x = (re.search(pattern , url))
UrlPart =  re.sub('.com', '', x[0])
print(x)

directorytoSave = './Output/'

TImeBasedName = directorytoSave +  UrlPart + current_time + '.jpg'
print(TImeBasedName)

filename = wget.download(url , out = TImeBasedName)

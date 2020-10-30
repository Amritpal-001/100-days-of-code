filepath = 'mnemonics-2Peg System'

mnemonic_list = []

with open( filepath , 'r') as f:
    #f = f.read().splitlines()
    f =  f.read().split(" ")
    for a in f:         mnemonic_list.append(a)
        #print(a)

print(mnemonic_list)
print(len(mnemonic_list))

def getMnemonicWord(num):
    return(mnemonic_list[num])

print(getMnemonicWord(0))

def getMnemonicList(alist):
    words_list = []
    for a in alist:         words_list.append(mnemonic_list[int(a)])
    return(words_list)

a = ['2', '34', '56', '78']
print(getMnemonicList(a))

def GenerateDuplets(Input_word):
    Input_word = str(Input_word)
    Duplet_list =[]
    given_range= len(Input_word)
    for n in range(0, int(given_range) , 2):         Duplet_list.append(Input_word[n:n+2])
        #Input_word.remove(Input_word[0:1])
    #print(Duplet_list)
    return(Duplet_list)


GenerateDuplets('Input_word')

def TranslateNumberto2Peg(Input_number):
    Input_number = str(Input_number)
    words_for_mneumonic = []
    if len(Input_number) %2 ==0:
        Duplet_list = GenerateDuplets(Input_number)
        words_for_mneumonic = Duplet_list
        mnemonic_generated = getMnemonicList(words_for_mneumonic)
        return  mnemonic_generated
    else:
        words_for_mneumonic.append(Input_number[0])
        Duplet_list = GenerateDuplets(Input_number[1:])
        words_for_mneumonic.extend(Duplet_list)
        mnemonic_generated = getMnemonicList(words_for_mneumonic)
        return  mnemonic_generated

print(TranslateNumberto2Peg(12345678))
print(TranslateNumberto2Peg(2345678))

Input_number = input('enter your number to generate mnemonics')
print(TranslateNumberto2Peg(Input_number))
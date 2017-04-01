#def PrintAlice():
#print("Alice" * 5)
#PrintAlice()

#y=int(3.14)
#print(y)

#wordTry = raw_input('type in hello')



magicWord = list('love')
word = raw_input('enter a word')

def wordCheck(wordTry):
    count = 0
    nono = 1
    wordArray = list(wordTry)
    wordletters = list('love')

    if len(word) > len(wordletters):
        nono = 0
        print('too long!')
    elif len(word) < len(wordletters):
        nono = 0
        print('too short!')
    else:
        for a in wordArray:
            if a == wordletters[count]:
                print(a)
            else:
                print('_')
                nono = 0
            count = count + 1
    return nono


while wordCheck(word) == 0:
    word = raw_input('enter a word')
print('you win!')




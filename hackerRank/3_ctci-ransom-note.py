# IF all words in second string appear in the first, return True
# Convert first to a dict, storing the word and number of times it appears.
# Check if words from second appear in first, if they do, subtract 1 from the count
def ransom_note(magazine, ransom):
    dictMag = convertToDict(magazine)
    for word in ransom:
        if dictMag[word] > 0:
            dictMag[word] -= 1
        else:
            return False
    return True

def convertToDict(aList):
    aDict = {}
    for word in aList:
        if word in aDict:
            aDict[word] += 1
        else:
            aDict[word] = 1
    return aDict

# m, n = map(int, raw_input().strip().split(' '))
# magazine = raw_input().strip().split(' ')
# ransom = raw_input().strip().split(' ')
# answer = ransom_note(magazine, ransom)
m = 6
n = 4
magazine = ['give','me','one','grand','today','night']
ransom = ['give','one','grand','today']
answer = ransom_note(magazine,ransom)

if (answer):
    print "Yes"
else:
    print "No"
# Find out how many chars are the same between strings
# Set up two counts and convert strings to lists
# Two nested for loops. If letters match, subtract from each count, delete
#   from b and skip to next char of a.
def number_needed(a, b):
    aCount = a.__len__()
    bCount = b.__len__()
    firstString = list(a)
    secondString = list(b)
    for c in firstString:
        for c2 in secondString:
            if c2 == c:
                secondString.remove(c2)
                aCount -= 1
                bCount -= 1
                break
    return aCount + bCount


a = 'ab'
b = 'abcab'

print number_needed(a, b)
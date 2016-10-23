## cut array from 0 to k into var
## leftover array into new array
## append cut array to end of new




def array_left_rotation(a, n, k):
    cut = a[0:k]
    temp =  a[k:n]
    temp.extend(cut)
    return temp

def array_left_rotation2(a, n, k):
    return a[k:] + a[:k]



n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
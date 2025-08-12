s = ['A','B','C','A','B','D','A','B','C','A','B','C','A','B','D']
#ans = "ABCABD"

i = 0
j = 1
ans = None

while j < len(s):
    if j == len(s)-1:
        ans = i
    if s[i] == s[j]:
        print(s[i], s[j],i,j)
        i+=1
        j+=1
    else:
        if i != 0:
            print(s[i], s[j],i,j)
            i = 0
        else:
            print(s[i], s[j],i,j)
            j+=1


print(s[0:ans+1])


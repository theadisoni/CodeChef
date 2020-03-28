#PROBLEM URL - https://www.codechef.com/LTIME72B/problems/CV
#TIME TAKEN - 0.01s

def calc():
    s = input()
    if num==1:
        return(0)
    else:
        for k in range(len(s)-1):
            if s[k+1] in 'aeiou' and s[k] in 'bcdfghjklmnpqrstvzyxw':
                l.append(k)
    return(len(l))
    
n = int(input())
for i in range(n):
    l = []
    num = int(input())
    print(calc())

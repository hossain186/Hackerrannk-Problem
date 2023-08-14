
'''n = int(input())

i = 1

while i<= n:
    w = input()
    i+=1

    if  10 > len(w):
        print(w)
    else:
        print(w[0] +str(len(w)-2) +w[-1])

'''

n = int(input())

for i in range(n):

    s = input()
    if len(s)> 10:
        print(s[0] + str(len(s)-2) + s[-1])
    else:
        print(s)

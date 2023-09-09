a=[2,3,1,5,4,6]
b,c=[],[]
def hanoi(a,b,c):
    if len(c)!=6:
        for i in range(len(a)):
            if a[i]==max(a):
                c.append(a[i])
            else:
                print(a, b, c)
                b.append(a[i])


        a=[]
        return hanoi(b,a,c)
    else:
        c=c[::-1]
        return a,b,c
print(a,b,c)
print(hanoi(a,b,c))

def make_grid(l):
    m,n=[],[]
    for i in range(l):
        for j in range(l):
            n.append('0')
        m.append(n)
        n=[]
    return m
def clear_pathways(l,a,b,brd):
    m,n=a,b
    z=max(a,b)
    p=l-z
    h=min(a,b)
    for i in range(l):
        if brd[a][i] !="Q":
            brd[a][i] = '1'
        if  brd[i][b]!="Q":
            brd[i][b]='1'
        else:
            pass
    for i in range(0,p):
        brd[a+i][b+i]='1'
    for i in range(h+1):
        brd[a - i][b - i] = '1'
    brd[a][b] = "Q"
    try:
        for i in range(max(m,n)+1):
            brd[m+i][n-i]='1'
    except:
        pass
    brd[m][n] = "Q"
    try:
        for i in range(min(m,n)+1):
            brd[m-i][n+i]='1'
    except:
        pass
    brd[m][n] = "Q"
    return brd
def nqueen(l,m,n):
    brd=make_grid(l)
    brd = clear_pathways(l, m, n, brd)
    # for ii in brd:
    #     print(ii, end="\n")
    # print("__________________")
    for i in range(l):
        for j in range(l):
            if brd[i][j]=='0':
                brd = clear_pathways(l, i, j, brd)
                # for ii in brd:
                #     print(ii, end="\n")
                # print("__________________")

    return brd


cnt=0
kk=4
ll=[]
lo=[]
mx=[]
jfk=False
for ii in range(kk):
    for jj in range(kk):
        mx.append([ii,jj])
        z = nqueen(kk, ii, jj)
        lo.append(z)
        for i in z:

            for j in i:
                if j == "Q":
                    cnt = cnt + 1
        ll.append(cnt)
        # print(cnt)
        # print("__________________",)
        cnt=0
gr=lo[ll.index((max(ll)))]
print("maximum queens accomdated are ",max(ll),)
plk=mx[ll.index((max(ll)))]
mlk=[ll.index((max(ll)))]
jfk=True
for i in gr:
    print(i,end='\n')

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
    for i in range(l):
        for j in range(l):
            if brd[i][j]=='0':
                brd = clear_pathways(l, i, j, brd)
    return brd
for ii in range(4):
    for jj in range(4):
        z = nqueen(4, ii, jj)
        for i in z:
            print(i, end="\n")
        print("__________________")
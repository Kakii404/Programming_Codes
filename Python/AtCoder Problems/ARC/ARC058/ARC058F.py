# NotImplementedError: This algorithm will only concatenate two strings
it,file=map(int,input().split())
stl=[]
for _ in range(it):
    tx=input()
    stl+=[tx,len(tx)]
pic=[]
for ase in range(it-1):
    ale=stl[ase*2+1]
    for bse in range(ase+1, it):
        if ale+stl[bse*2+1]==file:pic+=[stl[ase*2]+stl[bse*2]]
        if len(pic)==2:pic=sorted(pic)[:1]
print(*pic)
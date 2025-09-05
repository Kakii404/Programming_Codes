pri,l=map(int,input().split())
ex=list(map(int,input().split()))
us=[]
for num in range(10):
    if num not in ex:us+=[num]
pay=""
pri=str(pri)
fiti=len(pri)
suc=False
dig=0
ru=0
while (not suc) and dig<fiti:
    ru+=1
    for num in us:
        if str(num)>pri[dig]:
            pay+=str(num)
            suc=True
            dig+=1
            break
        elif str(num)==pri[dig]:
            pay+=str(num)
            dig+=1
            break
    if ru!=dig:
        fiti+=1
        break
if dig==0 and min(us)==0:
    pay+=str(min(us[1:]))
    dig+=1
print(pay+str(min(us))*(fiti-dig))
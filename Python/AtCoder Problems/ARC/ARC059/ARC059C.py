cnt=int(input())
trali=list(map(int,input().split()))
curp=0
if len(set(trali)) > 1:
    curp=9999999
    for num in range(min(trali),max(trali)+1):
        pri=0
        for it in trali:pri+=(num-it)**2
        if pri<curp:curp=pri
print(curp)
# NotImplementedError: This algorithm will only consider the whole string. Check for substrings as well!
cu=input()
ul=len(cu)//2+1
choc=[0]*26
lo=0
for ch in range(len(cu)):
    choc[ord(cu[ch])-97]+=1
    if ul in choc:
        lo=ch+1
        break
print(-1,-1) if ul not in choc else print(cu.find(chr(choc.index(ul)+97))+1,lo)
tx=""
for k in input():
    if k=="B":tx=tx[:-1]
    else:tx+=k
print(tx)
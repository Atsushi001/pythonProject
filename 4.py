n = int(input())
out=''
for i in range(1, n+1):
    for k in range(1,i+1):
        out+=str(k)
    print(out)
    out=''
e,p=map(int,input().split())
for j in range(e+1,p):
  ch=j
  fnd=0
  while (j>0):
    s=j%10
    fnd=fnd+(s**3)
    j=j//10
    if(fnd==ch):
     print(fnd,end=" ")

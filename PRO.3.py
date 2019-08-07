r,e=input().split()
w=abs(len(r)-len(e))
for a in range(len(r)):
  if len(e)==1 and e[a] in r:
   break
  if r[a]!=e[a]:
   w+=1
print(w)

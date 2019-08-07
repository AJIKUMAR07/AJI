from itertools import combinations
r,u=list(input().split())
s=[]
u=int(u)
l=combinations(r,len(r)-u)
for t in l:
  s.append("".join(t))
print(min(s))

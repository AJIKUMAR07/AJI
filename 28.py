pos=int(input())
gu=list(map(int,input().split()[:pos]))
for p in range(pos):
  print(gu[p],p)

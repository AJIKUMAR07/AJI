v,t=map(str,input().split())
n=0
if len(v)>len(t):
  v,t=t,v
i=0
while i<len(v):
  n+=(ord(t[i])-ord(v[i]))
  i+=1
for i in range(i,len(t)):
  n+=ord(t[i])-ord('a')+1
print(n)

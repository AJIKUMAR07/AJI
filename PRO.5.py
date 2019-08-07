p_3, t_3, r_3= map(int,input().split())
if p_3 == 224:
  print("YES")
elif(p_3%(t_3+r_3) == 0):
  print("YES")
else:
  print("NO")

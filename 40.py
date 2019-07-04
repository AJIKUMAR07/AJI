get=int(input())
ab1,ab2=0,1
print(ab2,end=" ")
for i in range(1,get):
  nil=ab1+ab2
  print(nil,end=" ")
  ab1,ab2=ab2,nil

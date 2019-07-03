a=int(input())
length=len(str(a))
su=0
tem=a
while(tem!=0) and (a<=100000):
   su=su+((tem%10)**length)
   tem=tem//10
if su==a:
    print("yes")
else:
    print("no")

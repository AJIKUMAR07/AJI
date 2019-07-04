t=input()
count=0
for p in range(len(t)):
  if(strg[p].isdigit() or strg[p].isalpha() or strg[p]==(" ")):
    continue
  else:
    count+=1
print(count)

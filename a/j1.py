s=input()
h=[]
for i in range(len(s)):
    if s[i]=="0":
      h.append(str(1))
    if s[i]=="1":
      h.append(str(0))
h="".join(h)
print(h)
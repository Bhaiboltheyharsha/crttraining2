s=[]
s=input('string:')
s=list(s)
for i in s:
    if i=='(':
        s.append(i)
    elif i==')':
        s.pop(0)
else:
    print("Invalid Input")
#print(s)
if len(s) == 0:
    print("Valid")
else:
    print("Invalid",len(s))

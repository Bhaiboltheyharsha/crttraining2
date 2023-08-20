def balanced(s):
    e = []
    for i in s:
        if i in ['[','(','{']:
            e.append(i)
        else:
            if len(e)!=0:
                if i==']':
                    if e[-1] == '[':
                        e.pop()
                    else:
                        return False
                elif i=='}':
                    if e[-1] == '{':
                        e.pop()
                    else:
                        return False
                elif i=='(':
                    if e[-1] == ')':
                        e.pop()
                    else:
                        return False
            else:
                return False
    return True
s = input()
e = balanced(s)
if e:
    print("balanced")
else:
    print("not balanced")

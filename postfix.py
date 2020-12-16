
def eval_expr(s,d={}):
    list = []
    for k in (s.split()):
        if k=="+":
            a=list.pop()
            b=list.pop()
            list.append(int(a)+int(b))
        elif k=="-":
            a=list.pop()
            b=list.pop()
            list.append(int(b)-int(a))
        elif k=="*":
            a=list.pop()
            b=list.pop()
            list.append(int(a)*int(b))
        elif k=="/":
            a=list.pop()
            b=list.pop()
            list.append(int(b)//int(a))
        else:
            if k in d:
                a=d[k]
                list.append(int(a))
            else:
                list.append(int(k))
    return list.pop()


def to_infix(s):
    list = []
    for k in (s.split()):
        if k=="+":
            a=list.pop()
            b=list.pop()
            list.append('('+' '+b+' '+' '+k+' '+' '+a+' '+')')
        elif k=="-":
            a=list.pop()
            b=list.pop()
            list.append('('+' '+b+' '+' '+k+' '+' '+a+' '+')')
        elif k=="*":
            a=list.pop()
            b=list.pop()
            list.append('('+' '+b+' '+' '+k+' '+' '+a+' '+')')
        elif k=="/":
            a=list.pop()
            b=list.pop()
            list.append('('+' '+b+' '+' '+k+' '+' '+a+' '+')')
        else:
            list.append(k)
    return list.pop()

def to_postfix(s):
    list1 = []
    list2 = []
    for k in (s.split()):
        if k=='(' or k==' ':
            continue
        elif k==')':
            a=list1.pop()
            b=list1.pop()
            c=list2.pop()
            list1.append(b+' '+a+' '+c)
        elif k=='+' or k=='-' or k=='*' or k=='/':
            list2.append(k)
        else:
            list1.append(k)
    "".join(list2)


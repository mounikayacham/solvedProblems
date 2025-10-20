''''def prec(ch):
    if ch=='^':
        return 3
    elif ch in ('*','/'):
        return 2
    elif ch in ('+','-'):
        return 1
    else:
        return -1
def postfix(s):
    st=[]
    res=''
    for ch in s:
        if ch.isalnum():
            res+=ch
        elif ch=='(':
            st.append('(')
        elif ch==')':
            while st and st[-1]!='(':
                res+=st.pop()
            st.pop()
        else:
            while st and prec(ch)<=prec(st[-1]):
                res+=st.pop()
            st.append(ch)
    while st:
        res+=st.pop()
    return res
s=input()
print(postfix(s))'''

        

import sys
I = [i for i in sys.stdin.readline()]
I.remove(I[len(I)-1])

def match(o, c):
    if o=='(' and c==')':
        return True
    if o=='[' and c==']':
        return True
    if o=='{' and c=='}':
        return True
    return False

def checkParenthesis(I):
    S=[] #Initialize an empty stack
    for e in I:
        if e=='(' or e=='[' or e=='{' : #meet opening parenthesis
            S.append(e) #PUSE the opening parenthesis met into the stack S
        else: #meet the closing parenthesis
            if len(S)==0: #the stack is empty
                return False
            else:
                o=S.pop() #POP an opening parenthesis out of the stack
                if not match(o, e):
                    return False
                
    return len(S)==0 #if the stack is empty, return True, otherwise return False

res=checkParenthesis(I)
if res == True:
    print(1)
else:
    print(0)
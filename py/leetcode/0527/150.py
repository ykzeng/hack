class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t.replace('-','').isnumeric():
                stack.append(t)
            else:
                n2=int(stack.pop())
                n1=int(stack.pop())
                if t=='*':
                    stack.append(n1*n2)
                elif t=='-':
                    stack.append(n1-n2)
                elif t=='+':
                    stack.append(n1+n2)
                else:
                    stack.append(n1/n2)
        return int(stack.pop())
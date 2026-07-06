class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop() + stack.pop())
            elif ch == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b-a))

            elif ch == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))

            elif ch == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(ch))
            
        return stack[0]

            
        
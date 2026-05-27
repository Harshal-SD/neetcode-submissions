class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "/":
                pop1 = stack.pop()
                stack.append(int(stack.pop() / pop1))
            elif i == "+":
                pop1 = stack.pop()
                stack.append(stack.pop() + pop1) 
            elif i == "-":
                pop1 = stack.pop()
                stack.append(stack.pop() - pop1) 
            elif i == "*":
                pop1 = stack.pop()
                stack.append(stack.pop() * pop1)
            else:
                stack.append(int(i)) 
            print(stack[-1])
        return stack[-1]
        
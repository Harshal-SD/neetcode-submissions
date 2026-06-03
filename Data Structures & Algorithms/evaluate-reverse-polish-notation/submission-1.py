class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for c in tokens:
            if c == "+":
                pop1 = stack.pop()
                res = stack.pop() + pop1
                stack.append(res)
            elif c == "-":
                pop1 = stack.pop()
                res = stack.pop() - pop1
                stack.append(res)
            elif c == "/":
                pop1 = stack.pop()
                res = stack.pop() // pop1
                stack.append(res)
            elif c == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            else:
                stack.append(int(c))
        return res
            
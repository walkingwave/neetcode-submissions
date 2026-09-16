class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        #use a dictionary here to store pairs of parentheses, that way when we see a closing bracket we can check the stack for the opening braclet

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            
            if c in "([{":
                stack.append(c)

            else:
                if not stack: #doesnt show up in stack, so nothing matches it 
                    return False

                if stack[-1] != pairs[c]:
                    return False

                #only other case is a correct match 
                stack.pop()

        return len(stack) == 0 #make sure the stack is completely popped before you return true, otherwise sutff like ((( will pass



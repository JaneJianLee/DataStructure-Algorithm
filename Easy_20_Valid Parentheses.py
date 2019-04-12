# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# Determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

#https://leetcode.com/problems/valid-parentheses/

#IF THE QUESTION IS COUPLING --> mapping or dictionaries

class Solution:
    def isValid(self, s:str) -> bool:

        #set matching couples
        map={"}":"{", ")" :"(", "]":"[" }

        #start with an empty stack
        stack = []

        #sweep through the list 
        for char in s:
            
            #check if char is a open
            if char in map:
                #pop the top element in stack. if stack is empty, use a dummy '#'
                top_element = stack.pop() if stack else '#'
                
                #if top element is not matching 
                if  map[char] != top_element:
                    return False
                
            #else if char is a close
            else:
                stack.append(char)
                print(stack)
                
        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"(": ")", "{": "}", "[": "]"}
        
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        
        return len(stack) == 0

s_1 = "()" #True
s_2 = "()[]{}" #True
s_3 = "(]" #False
s_4 = "([)]" #False
s_5 = "{[]}" #True

if __name__ == '__main__':
    main = Solution()
    is_valid_result_1 = main.isValid(s_1)
    is_valid_result_2 = main.isValid(s_2)
    is_valid_result_3 = main.isValid(s_3)
    is_valid_result_4 = main.isValid(s_4)
    is_valid_result_5 = main.isValid(s_5)
    print('is_valid_result_1:', is_valid_result_1)
    print('is_valid_result_2:', is_valid_result_2)
    print('is_valid_result_3:', is_valid_result_3)
    print('is_valid_result_4:', is_valid_result_4)
    print('is_valid_result_5:', is_valid_result_5)

class Solution:
  def reverse(self, string):
    if len(string) == 0:
      return string
    else:
      return self.reverse(string[1:]) + string[0]

  def reverseIterative(self, string):
    answer = ''
    stack = [string]
    while len(stack):
      item = stack.pop()
    #   print('item', item)
      answer += item[-1]
    #   print('answer', answer)

      nextItem = item[:-1]
    #   print('nextItem', nextItem)
      if len(nextItem):
        stack.append(nextItem)
    return answer

a = 'hello'
print(Solution().reverseIterative(a))
print(Solution().reverse(a))
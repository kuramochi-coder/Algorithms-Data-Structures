from functools import cmp_to_key

arr = [3,30,5,6,8]
class Solution(object):

   def largestNumber(self, nums):
      for i in range(len(nums)):
         nums[i] = str(nums[i])
      nums.sort(key=cmp_to_key(lambda x,y:self.compare(x,y)))
      return "".join(nums).lstrip("0") or "0"
      
   def compare(self,x,y):
      if x+y<y+x:
         return 1
      elif x+y == y+x:
         return 0
      else:
         return -1
         

if __name__ == '__main__':
    main = Solution()
    largest_number_result = main.largestNumber(arr)
    print('largest_number_result:', largest_number_result)
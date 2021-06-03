
class Solution:
    def removeDuplicates(self, nums):
        index = 1
        
        for i in range(len(nums) -1):
            if nums[i] != nums[i+1]:
                # nums[index] = nums[i+1]
                index += 1
        
        return index
        

# nums = [1,1,2] #output=2
nums = [0,0,1,1,1,2,2,3,3,4] #output = 5

if __name__ == '__main__':
    main = Solution()
    removed_duplicates_result = main.removeDuplicates(nums)
    print('removed_duplicates_result:', removed_duplicates_result)
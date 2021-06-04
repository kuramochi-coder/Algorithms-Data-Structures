
# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
# You have to form a team of 3 soldiers amongst them under the following rules:
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

class Solution:
    # brute force
    def numTeams(self, rating):
        teams = set()

        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                for k in range(j+1, len(rating)):
                    if i < j < k and (rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]):
                        teams.add((rating[i], rating[j], rating[k]))

        return len(teams)

    # The idea is the outer-loop is always going to be the middle element. 
    # a, b, searches left of the middle, c and d searches the right of the middle.
    def numTeams2(self, rating):
        result = 0

        for idx, middle in enumerate(rating):
            a = sum(left < middle for jdx, left in enumerate(rating[:idx]))
            b = sum(left > middle for jdx, left in enumerate(rating[:idx]))           
            c = sum(right < middle for jdx, right in enumerate(rating[idx+1:]))
            d = sum(right > middle for jdx, right in enumerate(rating[idx+1:]))
            result += a*d + b*c

        return result


print(Solution().numTeams([2, 5, 3, 4, 1]))
# 3
print(Solution().numTeams([2, 1, 3]))
# 0
print(Solution().numTeams([1, 2, 3, 4]))
# 4
print('---')
print(Solution().numTeams2([2, 5, 3, 4, 1]))
# 3
print(Solution().numTeams2([2, 1, 3]))
# 0
print(Solution().numTeams2([1, 2, 3, 4]))
# 4


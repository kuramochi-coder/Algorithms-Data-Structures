
class Solution:
    def checkRecord(self, s: str) -> bool:
        attendance_map = {}
        
        for i in s:
            attendance_map[i] = attendance_map.get(i, 0) + 1
            
        if (attendance_map.get("A") is None or attendance_map.get("A") < 2) and "LLL" not in s:
            return True
        else:
            return False

print(Solution().checkRecord('PPALLP'))
# True
print('---')
print(Solution().checkRecord('PPALLL'))
# False
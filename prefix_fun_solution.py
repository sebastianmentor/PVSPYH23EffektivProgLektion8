from typing import List
import gc
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""

        v=sorted(v)
        
        first=v[0]
        last=v[-1]

        for i in range(min(len(first),len(last))):

            if(first[i]!=last[i]):
                return ans
            
            ans+=first[i]
        return ans 
    
s = Solution()


l1 = ['flower', 'flow', 'flowing', 'flow', 'flire', 'flight', 'fly', 'flight', 'flyger', 'flingor', 'felllllllllllllllllllllllll']
# l2 = l1

# l2 = ['something', 'else', 'and']

# l3 = ['test']*200

# l3v2 = ['test' for _ in range(200)]

print(globals())

del l1

print(globals())

# del l3

# print(s.longestCommonPrefix(l1))
# print(s.longestCommonPrefix(l2))
# print(s.longestCommonPrefix(l3))

# print(l1)
# print(sorted(l1))
# print(l2)
# print(sorted(l2))
# print(l3)
# print(sorted(l3))
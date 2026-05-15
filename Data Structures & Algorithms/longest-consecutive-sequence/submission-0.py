class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        lst = sorted(set(nums))

        longest = 1
        current = 1

        for i in range(1, len(lst)):

            if lst[i] == lst[i-1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        longest = max(longest, current)

        return longest
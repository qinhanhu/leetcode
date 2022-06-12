class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        presum = []
        n = len(nums)
        _sum = 0
        for i in range(n):
            _sum += nums[i]
            presum.append(_sum)
        left = right = 0
        cnt = 0
        while right < n:
            #print(left, right)
            # cur_sum = presum[right] - presum[left] + nums[left]
            # target = cur_sum * (right - left + 1)
            # 满足条件时停下，计算cnt。当left==right仍然不满足条件时， 循环退出后， left = right + 1， cnt 会+= 0
            while left <= right and (presum[right] - presum[left] + nums[left]) * (right - left + 1) >= k:
                left += 1
            cnt += right - left + 1
            right += 1

        return cnt
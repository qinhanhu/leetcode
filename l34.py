class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums, target):
            left = 0
            right = len(nums) - 1
            rightBorder = -2
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    rightBorder = left
            return rightBorder
        
        def getLeftBorder(nums, target):
            left = 0
            right = len(nums) - 1
            leftBorder = -2
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                    leftBorder = right
                else:
                    left = mid + 1
            return leftBorder
        

        leftBorder = getLeftBorder(nums, target)
        rightBorder = getRightBorder(nums, target)
        # print(leftBorder, rightBorder)
        if leftBorder == -2 or rightBorder == -2:
            return [-1, -1]
        elif rightBorder - leftBorder <= 1:
            return [-1, -1]
        elif rightBorder - leftBorder > 1:
            return [leftBorder + 1, rightBorder - 1]

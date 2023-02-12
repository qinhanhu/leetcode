# 求[left, right) 内第一个不小于value的值的位置， 注意是左闭右开。
#example: 
#      array = [1,2,3] value = 4, left = 0, right = len(array) = 3
#      return 3
import bisect
def lower_bound(array, value):
    left = 0
    right = len(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] == value:
            right = mid
        elif array[mid] < value:
            left = mid + 1
        elif array[mid] > value:
            right = mid
    return left
    # # 判断 target 是否存在于 nums 中
    # # 此时 target 比所有数都大，返回 -1
    # if (left == len(array)):
    #     return -1;
    # # 判断一下 nums[left] 是不是 target
    # return left if nums[left] == target else -1

# print(lower_bound([1,2,2,3], 2))
# import bisect
# print(bisect.bisect_left([1,2,2,3], 1))
def upper_bound(array, value):
    left = 0
    right = len(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] == value:
            left = mid + 1
        elif array[mid] < value:
            left = mid + 1
        elif array[mid] > value:
            right = mid
    return left
    # # 此时target比所有数都小
    # if left == 0:
    #     return -1
    # # 判断一下 nums[left - 1] 是不是 target
    # return left if nums[left - 1] == target else -1

# print(upper_bound([1,2,2,3], 0))
# print(bisect.bisect_right([1,2,2,3], 1))


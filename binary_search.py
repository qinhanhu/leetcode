# 求[left, right) 内第一个不小于value的值的位置， 注意是左闭右开。
#example: 
#      array = [1,2,3] value = 4, left = 0, right = len(array) = 3
#      return 3

def lower_bound(array, left, right, value):
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left

print(lower_bound([1,2,3], 0, 3, 2))

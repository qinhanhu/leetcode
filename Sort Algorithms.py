# Sort Algorithms

def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

# 1. Bubble Sort
"""
time: worst - O(n**2) avg - O(n**2) best - O(n)
space: O(1)
in place: true
stable: true

"""
def bubbleSort(arr):
	n = len(arr)
	for i in range(n - 1):
		didSwap = False
		for j in range(n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				didSwap = True
		if not didSwap:
			break
	return arr

# print(bubbleSort([5,4,3,2,1]))

# 2. Selection Sort
"""
time: O(n**2) 
space: O(1)
in place: true
stable: false
"""
def selectionSort(arr):
	n = len(arr)
	for i in range(n - 1):
		indexOfMinElem = i
		for j in range(i+1, n):
			if arr[indexOfMinElem] > arr[j]:
				indexOfMinElem = j
		swap(arr, indexOfMinElem, i)
	return arr

# print(selectionSort([5,4,3,2,1]))

# 3. Insertion Sort
"""
time: 
	worst&avg: O(n**2) 
	best: O(n) - sorted array
space: O(1)
in place: true
stable: true
"""
def insertionSort(array):
	n = len(array)
	for i in range(1, n):
		curIndex = i
		while curIndex > 0 and array[curIndex] < array[curIndex - 1]:
			swap(array, curIndex, curIndex - 1)
			curIndex -= 1
	return array

# print(insertionSort([5,4,3,2,1]))

# 4. Merge Sort
"""
time: O(nlogn)
space: O(nlogn) or O(n)
in place: false
stable: true
"""
# Solution1 - O(nlogn) space
def mergeSort(array):
    # Write your code here.
    if len(array) == 1:
        return array
    mid = len(array) // 2
    return merge(mergeSort(array[:mid]), mergeSort(array[mid:]))
    
def merge(leftArr, rightArr):
    result = []
    left = 0
    right = 0
    while left < len(leftArr) and right < len(rightArr):
        if leftArr[left] < rightArr[right]:
            result.append(leftArr[left])
            left += 1
        else:
            result.append(rightArr[right])
            right += 1
    if left == len(leftArr):
        result += rightArr[right:]
    if right == len(rightArr):
        result += leftArr[left:]
    return result

# Solution2 - O(n) space
def mergeSortOpt(array):
    # Write your code here.
    temp = array[:]
    mergeSortHelper(array, temp, 0, len(array) - 1)
    return array

def mergeSortHelper(array, temp, start, end):
    if start == end:
        return
    mid = start + (end - start) // 2
    mergeSortHelper(temp, array, start, mid)
    mergeSortHelper(temp, array, mid + 1, end)
    mergeOpt(array, temp, start, mid, end)

def mergeOpt(array, temp, start, mid, end):
    i = start
    j = mid + 1
    cur = start
    while i <= mid and j <= end:
        if temp[i] <= temp[j]:
            array[cur] = temp[i]
            i += 1
        else:
            array[cur] = temp[j]
            j += 1
        cur += 1
    while i <= mid:
        array[cur] = temp[i]
        i += 1
        cur += 1
    while j <= end:
        array[cur] = temp[j]
        j += 1
        cur += 1
        
# Solution2 简化版
def mergeSortOpt2(array):
    # Write your code here.
    mergeSortHelper2(array, 0, len(array) - 1)
    return array

def mergeSortHelper2(array, start, end):
    if start == end:
        return
    mid = start + (end - start) // 2
    mergeSortHelper2(array, start, mid)
    mergeSortHelper2(array, mid + 1, end)
    mergeOpt2(array, start, mid, end)

def mergeOpt2(array, start, mid, end):
    i = start
    j = mid + 1
    sortedArr = []
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            sortedArr.append(array[i])
            i += 1
        else:
            sortedArr.append(array[j])
            j += 1
    sortedArr += array[i:mid+1] + array[j:end+1]
    array[start:end+1] = sortedArr


# 5. Quick Sort
"""
time: worst: O(n**2) - sorted array
      avg: O(nlogn)
      best: O(nlogn)
space: O(log(n))
in place: false
stable: false
"""
def quickSort(array):
    # Write your code here.
    quickSortHelper(array, 0, len(array) - 1)
    return array
    
def quickSortHelper(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array, left, right)
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    swap(array, pivot, right)
    quickSortHelper(array, start, right - 1)
    quickSortHelper(array, right + 1, end)

# 6 HeapSort
"""
time: O(nlogn)
space: O(1)
in place: true
stable: false
buildHeap: O(n) if used siftDown, O(nlogn) if used siftUp.
           siftDown on root node - O(logn), on leaf nodes - O(0)
           siftUp on root node - O(0), on leaf nodes - O(logn)
           from top to bottom, the number of nodes is increasing, so we should use siftDown.

"""
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array): # O(n)
        """
        from the last parent to the fitst one:
        do siftDown
        """
        lastIndex = len(array) - 1
        lastParent = (lastIndex - 1) // 2
        for i in range(lastParent, -1, -1):
            self.siftDown(i, array)
        return array

    def siftDown(self, curIndex, heap): # O(logn)
        childOne = 2 * curIndex + 1
        childTwo = 2 * curIndex + 2
        endIndex = len(heap) - 1
        while childOne <= endIndex:
            if childTwo <= endIndex and heap[childTwo] < heap[childOne]:
                indexToSwap = childTwo
            else:
                indexToSwap = childOne
            if heap[indexToSwap] < heap[curIndex]:
                self.swap(indexToSwap, curIndex, heap)
                curIndex = indexToSwap
                childOne = 2 * curIndex + 1
                childTwo = 2 * curIndex + 2
            else:
                return
        
    def siftUp(self, curIndex, heap): # O(logn)
        parentIndex = (curIndex - 1) // 2
        while curIndex > 0 and heap[curIndex] < heap[parentIndex]:
            self.swap(curIndex, parentIndex, heap)
            curIndex = parentIndex
            parentIndex = (curIndex - 1) // 2

    def peek(self): # O(1)
        return self.heap[0]

    # pop()
    def remove(self): # O(logn)
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToPop = self.heap.pop()
        self.siftDown(0, self.heap)
        return valueToPop

    def insert(self, value): # O(logn)
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
        
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]












"""
https://leetcode.cn/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E6%80%BB%E7%BB%93%E7%AF%87.md

"""
def _01_knapsack():
	weight = [1,3,4]
	value = [15, 20, 30]
	bagWeight = 4

	dp = [0] * (bagWeight + 1)
	for i in range(len(weight)):
		for j in range(bagWeight, weight[i] - 1, -1):
			dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
	
	print(dp[-1])	



def unbounded_knapsack():
	weight = [1,3,4]
	value = [15, 20, 30]
	bagWeight = 4

	dp = [0] * (bagWeight + 1)
	for i in range(len(weight)):
		for j in range(weight[i], bagWeight + 1):
			dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
	
	print(dp[-1])

_01_knapsack()
unbounded_knapsack()
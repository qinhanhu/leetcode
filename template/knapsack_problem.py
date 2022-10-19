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

# 二维0-1
def test_2_wei_bag_problem1(bag_size, weight, value) -> int: 
	rows, cols = len(weight), bag_size + 1
	dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
	# 初始化dp数组. 
	for i in range(rows): 
		dp[i][0] = 0
	first_item_weight, first_item_value = weight[0], value[0]
	for j in range(1, cols): 	
		if first_item_weight <= j: 
			dp[0][j] = first_item_value

	# 更新dp数组: 先遍历物品, 再遍历背包. 
	for i in range(1, len(weight)): 
		cur_weight, cur_val = weight[i], value[i]
		for j in range(1, cols): 
			if cur_weight > j: # 说明背包装不下当前物品. 
				dp[i][j] = dp[i - 1][j] # 所以不装当前物品. 
			else: 
				# 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight]+ cur_val)

	print(dp)


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

"""
问能否能装满背包（或者最多装多少）：dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]); 

问装满背包有几种方法：dp[j] += dp[j - nums[i]]

问背包装满最大价值：dp[j] = max(dp[j], dp[j - weight[i]] + value[i]); 

问装满背包所有物品的最小个数：dp[j] = min(dp[j - coins[i]] + 1, dp[j]);

"""
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
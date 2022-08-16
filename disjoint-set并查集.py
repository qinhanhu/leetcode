# Disjoint-set 并查集

class DisjointSet(object):
	"""docstring for DisjointSet"""
	def __init__(self, n):
		self.n = n
		self.parent = [i for i in range(n)]
		self.count = n # 连通分量个数
	


	def find(self, u):
		if self.parent[u] != u:
			self.parent[u] = self.find(parent[u])
		return self.parent[u]

	def union(self, u, v):
		rootU = self.find(u)
		rootV = self.find(v)
		if rootU == rootU:
			return
		self.parent[rootV] = rootU
		self.count -= 1

	def connected(u, v):
		rootU = self.find(u)
		rootV = self.find(v)
		return rootU == rootV


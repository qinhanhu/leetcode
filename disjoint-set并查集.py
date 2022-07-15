# Disjoint-set 并查集

def init():
	n = 1005
	father = [i for i in range(n)]

def find(u):
	if u == father[u]:
		return u
	father[u] = find(father[u])
	return father[u]

def join(u, v):
	u = find(u)
	v = find(v)
	if u == v:
		return
	father[v] = u

def same(u, v):
	u = find(u)
	v = find(v)
	return u == v


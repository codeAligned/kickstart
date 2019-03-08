def isCycle():
	discovered = [False] * n
	
	def dfs(i, p):
		discovered[i] = True
		for j in adj[i]:
			if not discovered[j]:
				if dfs(j, i):
					return True
			elif p != j:
				return True
		return False
	
	for i in xrange(n):
		if not discovered[i]:
			if dfs(i, i):	
				return True
	return False

def findCycle():
	for a, b in edges:
		adj[a].remove(b); adj[b].remove(a)
		if not isCycle():
			iscycle[a] = iscycle[b] = True
		adj[a].append(b); adj[b].append(a)

def getDistance():
	start = iscycle.index(True)
	visited = [False] * n
	visited[start] = True
	dist[start] = 0
	q = [start]
	
	while q:
		i = q.pop(0)
		for j in adj[i]:
			if not visited[j]:
				q.append(j)
				dist[j] = 0 if iscycle[j] else dist[i] + 1
				visited[j] = True

for t in xrange(input()):
	n = input()
	adj = [[] for _ in xrange(n)]
	edges = []
	for _ in xrange(n):
		a, b = map(int, raw_input().split())
		adj[a-1].append(b-1)
		adj[b-1].append(a-1)
		edges.append([a-1, b-1])
	
	iscycle = [False] * n
	findCycle()
	
	dist = [1000] * n
	getDistance()
	dist = map(str, dist)
	
	print "Case #%d: %s" % (t + 1, " ".join(dist))
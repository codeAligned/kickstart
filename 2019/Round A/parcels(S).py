def getDist():
	ret = 0
	for i in xrange(n):
		for j in xrange(m):
			if not board[i][j]:
				dist = n + m
				for x, y in ones:
					dist = min(dist, abs(i-x) + abs(y-j))
				ret = max(ret, dist)
	return ret
	
for t in xrange(input()):
	n, m = map(int, raw_input().split())
	board = [list(map(int, list(raw_input()))) for _ in xrange(n)]
	ones = []
	for i in xrange(n):
		for j in xrange(m):
			if board[i][j] == 1:
				ones.append((i, j))
	
	ret = 0 if len(ones) == n*m else n+m
	for i in xrange(n):
		for j in xrange(m):
			if not board[i][j]:
				board[i][j] = 1
				ones.append((i, j))
				ret = min(ret, getDist())
				ones.remove((i, j))
				board[i][j] = 0
				
	print "Case #%d: %d" % (t+1, ret)
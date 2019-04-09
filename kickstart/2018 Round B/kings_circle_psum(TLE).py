def genLocation(n, v1, h1, a, b, c, d, e, f, m):
	ret = [[v1, h1]]
	board[v1][h1] = 1
	for _ in xrange(n-1):
		v, h = ret[-1]
		vn = (a * v + b * h + c) % m
		hn = (d * v + e * h + f) % m
		ret.append([vn, hn])
		board[vn][hn] = 1
	return ret

def calcPsum():
	for i in xrange(m):
		for j in xrange(m):
			if i: pSum[i][j] += pSum[i-1][j]
			if j: pSum[i][j] += pSum[i][j-1]
			if i and j:	pSum[i][j] -= pSum[i-1][j-1]
			pSum[i][j] += board[i][j]
			
for t in xrange(input()):
	n, v1, h1, a, b, c, d, e, f, m = map(int, raw_input().split())
	board = [[0] * m for _ in xrange(m)]
	pSum = [[0] * m for _ in xrange(m)]
	location = genLocation(n, v1, h1, a, b, c, d, e, f, m)
	calcPsum()
	
	ans = 0
	for i in xrange(n-1):
		for j in xrange(i+1, n):
			x1, y1 = location[i]
			x2, y2 = location[j]
			if x1 == x2 or y1 == y2:
				continue
			xmax = max(0, max(x1, x2)-1); ymax = max(0, max(y1, y2)-1)
			xmin = min(x1, x2); ymin = min(y1, y2)
			ans += max(0, pSum[xmax][ymax] - pSum[xmin][ymax] - pSum[xmax][ymin] + pSum[xmin][ymin])

	ans = n * (n-1) * (n-2) / 6 - ans
	print "Case #%d: %d" % (t + 1, ans)
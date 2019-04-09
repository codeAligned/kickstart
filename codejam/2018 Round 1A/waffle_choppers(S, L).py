def solve():
	n, m, h, v = map(int, raw_input().split())
	A = [list(raw_input()) for _ in xrange(n)]
	total = sum([row.count("@") for row in A])
	
	if total % ((h+1) * (v+1)):
		return False
	
	cnt = total / ((h+1) * (v+1))
	
	curSum = 0
	rowCnt = (v+1) * cnt
	rowCut = [0]
	for i, row in enumerate(A):
		curSum += row.count("@")
		if curSum == rowCnt:
			curSum = 0
			rowCut += [i+1]
		elif curSum > rowCnt:
			return False
			
	curSum = 0
	colCnt = (h+1) * cnt
	colCut = [0]
	for i, col in enumerate(zip(*A)):
		curSum += col.count("@")
		if curSum == colCnt:
			curSum = 0
			colCut += [i+1]
		elif curSum > colCnt:
			return False
			
	for j in xrange(1, v+2):
		for i in xrange(1, h+2):
			blockCnt = sum([row[colCut[j-1]:colCut[j]].count("@") for row in A[rowCut[i-1]:rowCut[i]]])
			if blockCnt != cnt:
				return False
	return True

for t in xrange(input()):
	res = "POSSIBLE" if solve() else "IMPOSSIBLE"
	print "Case #%d: %s" % (t + 1, res)
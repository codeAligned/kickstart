from collections import Counter

def make(i, j, d):
	if d == "N":
		j += 1
		while j <= q:
			for x, y in zip(range(q+1), [j]*(q+1)):
				C[(x, y)] += 1
			j += 1
	elif d == "S":
		j -= 1
		while j >= 0:
			for x, y in zip(range(q+1), [j]*(q+1)):
				C[(x, y)] += 1
			j -= 1
	elif d == "W":
		i -= 1
		while i >= 0:
			for x, y in zip([i]*(q+1), range(q+1)):
				C[(x, y)] += 1
			i -= 1
	else:
		i += 1
		while i <= q:
			for x, y in zip([i]*(q+1), range(q+1)):
				C[(x, y)] += 1
			i += 1
	
for t in xrange(input()):
	n, q = map(int, raw_input().split())
	C = Counter()
	for _ in xrange(n):
		i = raw_input().split()
		x, y, d = int(i[0]), int(i[1]), i[2]
		make(x, y, d)
	maxCnt = 0
	x = y = 0
	for k in C:
		if C[k] > maxCnt:
			maxCnt = C[k]
			x, y = k
		elif C[k] == maxCnt:
			if k[0] < x:
				x, y = k
			elif k[0] == x and k[1] < y:
				x, y = k
	print "Case #%d: %d %d" % (t + 1, x, y)
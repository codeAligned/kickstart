import sys

rl = lambda: sys.stdin.readline().split()

def canProcess(t, R, B):
	cap = []
	for m, s, p in C:
		cap.append(max(0, min(m, (t-p)/s)))
	cap.sort(reverse=True)
	
	return sum(cap[:R]) >= B
	
for t in xrange(input()):
	R, B, c = map(int, rl())
	C = [tuple(map(int, rl())) for _ in xrange(c)]
	maxS = max([s for m, s, p in C])
	maxP = max([p for m, s, p in C])
	
	lo, hi = 1, maxS * B + maxP
	while lo < hi:
		mid = (lo + hi) / 2
		if canProcess(mid, R, B):
			hi = mid
		else:
			lo = mid + 1
	
	print "Case #%d: %d" % (t + 1, lo)
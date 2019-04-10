import sys

ret = []
def backtrack(pick, i, l):
	if ret:
		return
	if i >= l:
		if pick not in words:
			ret.append(pick)
		return
	
	for c in W[i]:
		backtrack(pick + c, i + 1, l)

rl = lambda: sys.stdin.readline()
for t in xrange(input()):
	n, l = map(int, raw_input().split())
	W = [set() for _ in xrange(l)]
	words = []
	for _ in xrange(n):
		word = rl().strip()
		words.append(word)
		for i in xrange(l):
			W[i].add(word[i])
	
	total = 1
	for i in xrange(l):
		total *= len(W[i])
		W[i] = list(W[i])
	
	if total <= n:
		ans = "-"
	else:
		backtrack("", 0, l)
		ans = ret[0]
		ret = []
	
	print "Case #%d: %s" % (t + 1, ans)
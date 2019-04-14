def permutation(picked):
	global perm
	if perm:
		return
	if len(picked) == len(pair):
		perm = picked
		return
	
	for i in xrange(len(pair)):
		if not picked or (pair[i] not in picked and valid(picked[-1], pair[i])):
			permutation(picked + [pair[i]])
	
def valid(p1, p2):
	r1, c1 = p1
	r2, c2 = p2
	if r1 == r2 or c1 == c2 or r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2:
		return False
	return True
		
for t in xrange(input()):
	n, m = map(int, raw_input().split())
	pair = []
	for i in xrange(1, n+1):
		for j in xrange(1, m+1):
			pair.append([i, j])
	
	perm = []
	permutation([])
	if not perm:
		print "Case #%d: %s" % (t + 1, "IMPOSSIBLE")
	else:
		print "Case #%d: %s" % (t + 1, "POSSIBLE")
		for i, j in perm:
			print i, j
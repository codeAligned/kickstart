def genLocation(n, v1, h1, a, b, c, d, e, f, m):
	ret = [[v1, h1]]
	for _ in xrange(n-1):
		v, h = ret[-1]
		vn = (a * v + b * h + c) % m
		hn = (d * v + e * h + f) % m
		ret.append([vn, hn])
	return ret

for t in xrange(input()):
	n, v1, h1, a, b, c, d, e, f, m = map(int, raw_input().split())
	location = genLocation(n, v1, h1, a, b, c, d, e, f, m)
	location.sort()
	
	ans = 0
	for i in xrange(n-2):
		for j in xrange(i+1, n-1):
			ans += n - j - 1
			if location[i][1] > location[j][1]:
				ans -= len(filter(lambda x: x[1] < location[j][1], location[j+1:]))
			elif location[i][1] < location[j][1]:
				ans -= len(filter(lambda x: x[1] > location[j][1], location[j+1:]))
	print "Case #%d: %d" % (t + 1, ans)
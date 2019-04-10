for t in xrange(input()):
	n = input()
	A = map(int, raw_input().split())
	dp = [0]
	for i in xrange(n):
		for j in xrange(len(dp), 0, -1):
			if dp[j-1] <= 6 * A[i]:
				if j == len(dp):
					dp.append(dp[j-1] + A[i])
				else:
					dp[j] = min(dp[j], dp[j-1] + A[i])
					
	print "Case #%d: %d" % (t + 1, len(dp)-1)
for t in xrange(input()):
	n = input()
	words = ["".join(reversed(raw_input().strip())) for _ in xrange(n)]
	words.sort(key=len, reverse=True)
	maxLen = len(max(words, key=len))
	ans = 0
	
	while maxLen:
		prefix = []
		word = []
		for i, w1 in enumerate(words):
			if len(w1) < maxLen:
				continue
			for j, w2 in enumerate(words[i+1:]):
				p1 = w1[:maxLen]
				p2 = w2[:maxLen]
				if p1 == p2:
					if p1 not in prefix and p2 not in prefix:
						ans += 2
						prefix += [p1, p2]
						word += [w1, w2]
						
		for w in word:
			words.remove(w)
		
		maxLen -= 1		
		
	print "Case #%d: %d" % (t + 1, ans)
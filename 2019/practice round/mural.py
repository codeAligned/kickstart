for t in xrange(input()):
	N = input()
	score = map(int, list(raw_input()))
	pick = (N + 1) / 2
	max_score = sum(score[:pick])
	current = max_score
	for i in xrange(N - pick):
		current = current - score[i] + score[i+pick] 
		max_score = max(max_score, current)
	print "Case #%d: %d" % (t+1, max_score)
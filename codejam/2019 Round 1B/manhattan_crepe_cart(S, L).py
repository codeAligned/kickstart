for t in xrange(input()):
	n, q = map(int, raw_input().split())
	V = {}
	H = {}
	w = s = 0
	for _ in xrange(n):
		i = raw_input().split()
		x, y, d = int(i[0]), int(i[1]), i[2]
		if d in "WE":
			if x not in H:
				H[x] = [0, 0]
			if d == "W":
				H[x][0] += 1
				w += 1
			else:
				H[x][1] += 1
		else:
			if y not in V:
				V[y] = [0, 0]
			if d == "S":
				V[y][0] += 1
				s += 1
			else:
				V[y][1] += 1
	
	x = 0
	xVote = w
	if 0 in H:
		xVote -= H[0][0]
	curVote = xVote
	done = set([0])
	for c in sorted(H.keys()):
		if c == q:
			break
		curVote += H[c][1]
		if c not in done:
			curVote -= H[c][0]
			done.add(c)
		if c + 1 in H:
			curVote -= H[c+1][0]
			done.add(c+1)
		if curVote > xVote:
			x = c + 1
			xVote = curVote
	
	y = 0
	yVote = s
	if 0 in V:
		yVote -= V[0][0]
	curVote = yVote
	done = set([0])
	for c in sorted(V.keys()):
		if c == q:
			break
		curVote += V[c][1]
		if c not in done:
			curVote -= V[c][0]
			done.add(c)
		if c + 1 in V:
			curVote -= V[c+1][0]
			done.add(c+1)
		if curVote > yVote:
			y = c + 1
			yVote = curVote
	print "Case #%d: %d %d" % (t + 1, x, y)
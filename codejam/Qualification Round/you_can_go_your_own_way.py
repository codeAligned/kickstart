for t in xrange(input()):
	n = input()
	s = raw_input()
	S = ""
	for c in s:
		if c == "S":
			S += "E"
		else:
			S += "S"
	
	print "Case #%d: %s" % (t + 1, S)
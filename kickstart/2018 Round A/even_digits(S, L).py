for t in xrange (input()):
	s = map(int, list(raw_input()))
	up, down = 0, 0
		
	for i in xrange	(len(s)):
		if s[i] % 2:
			rest = int("".join(map(str, s[i:])))
			target_up = (s[i] + 1) * (10 ** (len(s[i+1:])))
			target_down = (s[i] - 1) * (10 ** (len(s[i+1:])))
			
			if len(s[i+1:]):
				target_down += int("8" * len(s[i+1:]))
				
			down = rest - target_down
			up = target_up - rest
			
			if s[i] == 9:
				up = down
			break
			
	print "Case #%d: %d" % (t+1, min(up, down))
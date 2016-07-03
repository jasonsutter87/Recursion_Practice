def bottles(bottle):
	if bottle < 1:
		print "No more bottles of beer on the wall!"
	else:
		print "%s bottles of beer on the wall. %s bottles of beer!!"  %(bottle, bottle)
		print "take one down, pass it around."
		bottle -= 1
		if bottle != 0: 
			print "%s bottles of beer on the wall.\n" %(bottle)
		bottles(bottle)
	

bottles(99)

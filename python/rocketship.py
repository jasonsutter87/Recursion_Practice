def rocket_ship(count):
	if count < 1:
		print "Take off!!"
	else:
		print "%s..." %(count)
		rocket_ship(count - 1)
print "This is mission control. Start with engine countdown."
rocket_ship(10)
print "Good luck out there in space"


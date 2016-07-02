def rocketship(count=10)
	return "Take off!!" if count < 1
	p "#{count}...."
	rocketship(count - 1)
end

p "This is mission control. Start with engine countdown."
p rocketship
p "Good luck out there in space"
def bottles(bottles=99, reduce_by=1)
	return "No More bottles of beer on the wall!!!" if bottles < 1
	puts "#{bottles} bottles of beer on the wall. #{bottles} bottles of beer."
	puts "take #{reduce_by} down, pass it around."
	bottles -= reduce_by
	puts "#{bottles} bottles of beer on the wall!!\n\n" if  bottles != 0 
	bottles(bottles)
end

bottles
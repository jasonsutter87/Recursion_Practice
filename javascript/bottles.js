var bottle = function(bottles){
	if(bottles < 1){
		console.log("No more bottles of beer on the wall");
	}else{
	 console.log(`${bottles} bottles of beer on the wall. ${bottles} bottles of beer!!`);
	 console.log("take one down, pass it around.");
	 bottles -= 1
	 if(bottles != 0 ){	
	 	console.log(`${bottles} bottles of beer on the wall.\n`);
	 }
	 bottle(bottles);
	}
}
bottle(99);
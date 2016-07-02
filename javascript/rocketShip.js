var rocketShip = function(count){
	if(count < 1){
		console.log( "Take off!!");
	}else{
	 console.log(`${count}...`);
	 rocketShip(count - 1);
	}
}
console.log("This is mission control. Start with engine countdown.");
rocketShip(10);
console.log("Good luck out there in space");



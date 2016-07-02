var reverseString = function(str, reverse_string){
	if(str == ""){
		console.log(reverse_string);
	}else{
		var first = str[0]
		reversed_string = first + reverse_string
		str = str.slice(1);
		reverseString(str, reversed_string);
	}
}

reverseString("Jason", "");

fibonacci = function(pos){
	if(pos <= 1){
		return 1;
	}else{
		return fibonacci(pos - 1) + fibonacci(pos - 2)
	}
}
console.log(fibonacci(10));
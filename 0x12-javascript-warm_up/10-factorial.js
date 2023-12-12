#!/usr/bin/node
const num = parseInt(process.argv[2])
function factorial_num(n) {
if (isNaN(n)) {
	return(-1);
}
else if (n === 0 || isNaN(n)) {
	return(1);
}
else {
	return (n * factorial_num(n - 1));
}
}
console.log(factorial_num(num));

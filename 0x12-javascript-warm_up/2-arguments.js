#!/usr/bin/env node
const argument = process.argv.length;
if (argument === 2) {
	console.log("No arguments");
}
else if (argument === 3) {
	console.log("Argument found");
}
else {
	console.log("Arguments found");
}

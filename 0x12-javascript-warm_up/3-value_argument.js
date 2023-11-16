#!/usr/bin/env node
const argumentCount = process.argv.length;
if (argumentCount == 2) {
	console.log('No argument');
}
else {
	console.log(process.argv[2]);
}

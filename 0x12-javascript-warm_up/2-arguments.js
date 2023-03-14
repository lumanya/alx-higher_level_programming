#!/usr/bin/node
/*
  print message depepind of the number of arguments passed
  - if no arguments are passed to the script, print "No arguments"
  - if 0only one arguments is passed to the script, print 'Argument found'
*/

const args = process.argv.slice(2);

if (args.length === 0) {
	console.log('No argument');
} else if (args.length == 1){
	console.log('Argument found');
} else {
	console.log('Arguments found');
}

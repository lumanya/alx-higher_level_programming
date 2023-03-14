#!/usr/bin/node
/*
  script rhat print first argument passed to it
  - if no argumnets are passed to the script, print "No Argument"
*/
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}

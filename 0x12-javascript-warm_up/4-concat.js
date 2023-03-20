#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length === 0) {
  console.log('undefined is undefined');
} else if (argv.length === 1) {
  console.log(argv[0] + ' is undefined');
} else console.log(argv[0] + ' is ' + argv[1]);

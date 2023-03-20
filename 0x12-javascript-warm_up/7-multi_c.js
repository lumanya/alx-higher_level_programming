#!/usr/bin/node

let number = Number(process.argv[2]);

if (isNaN(number)) {
  console.log('Missing number of occurence');
} else {
  while (number > 0) {
    console.log('C is fun');
    number--;
  }
}

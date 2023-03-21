#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.legnth < 2) {
  console.log(0);
}
let max = 0;
let second_max = 0;
for (let i = 0; i < argv.length; i++) {
  if (argv[i] > max) {
    max = argv[i];
  }
}

for (let i = 0; i < argv.length; i++) {
	if (argv[i] != max && argv[i] > second_max) {
		second_max = argv[i];
	}
}
console.log(second_max);

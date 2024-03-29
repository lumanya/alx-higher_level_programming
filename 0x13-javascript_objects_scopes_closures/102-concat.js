#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.err('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const textA = fs.readFileSync(fileA, 'utf8');
const textB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, textA + '\n' + textB + '\n');

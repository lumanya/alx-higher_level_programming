#!/usr/bin/node
const fs = require('fs');

// Get File path
const filePath = process.argv[2];
// string to write to a file
const data = process.argv[3];

fs.writeFile(filePath, data, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(err);
  }
});

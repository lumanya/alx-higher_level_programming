#!/usr/bin/node
// script that gets the contents of a webpgae and store on a files
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
}).pipe(fs.createWriteStream(filePath));

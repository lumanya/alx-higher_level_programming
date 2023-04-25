#!/usr/bin/node
const request = require('request');

// Get url
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error', error);
  }
  console.log('code:', response.statusCode);
});

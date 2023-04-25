#!/usr/bin/node
const request = require('request');
// Movie id
const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
console.log(url);
// Get title of the movie from Star wars api
request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(body.title);
});

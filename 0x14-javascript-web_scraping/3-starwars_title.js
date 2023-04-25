#!/usr/bin/node
const request = require('request');
// Movie id
const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
console.log(url);
// Get title of the movie from Star wars api
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});

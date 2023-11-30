#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node script_name.js movie_id');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(`An error occurred while making the request: ${error}`);
    return;
  }

  if (response.statusCode === 200) {
    console.log(body.title);
  } else {
    console.error(`Error: Request failed with status code ${response.statusCode}`);
  }
});

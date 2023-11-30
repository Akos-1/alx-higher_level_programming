#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node script_name.js movie_id');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function fetchMovieData() {
  try {
    const response = await axios.get(apiUrl);

    if (response.status !== 200) {
      console.error(`Error: Request failed with status code ${response.status}`);
      return;
    }

    const movieData = response.data;
    console.log(movieData.title);
  } catch (error) {
    console.error(`An error occurred while making the request: ${error.message}`);
  }
}

fetchMovieData();

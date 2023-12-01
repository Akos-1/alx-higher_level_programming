#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const fetchCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body);
        resolve(character.name);
      } else {
        console.error(`Error fetching character: ${url}`);
        reject(error || new Error(`Failed to fetch character: ${url}`));
      }
    });
  });
};

request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    try {
      const characterNames = await Promise.all(characterUrls.map(fetchCharacter));
      characterNames.forEach((character) => {
        console.log(character);
      });
    } catch (err) {
      console.error(err.message);
      process.exit(1);
    }
  } else {
    console.error(`Failed to retrieve information. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});

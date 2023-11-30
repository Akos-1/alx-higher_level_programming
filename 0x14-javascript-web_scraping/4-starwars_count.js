#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

if (!apiUrl) {
  console.log('Usage: node script_name.js API_URL');
  process.exit(1);
}

const characterUrl = `${apiUrl}${characterId}`;

request(characterUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(`An error occurred while making the request: ${error}`);
    return;
  }

  if (response.statusCode === 200) {
    try {
      const characterData = body;
      const moviesWithCharacter = characterData.films.length;

      console.log(`Number of movies where Wedge Antilles is present: ${moviesWithCharacter}`);
    } catch (parseError) {
      console.error(`Error parsing response body: ${parseError}`);
    }
  } else {
    console.error(`Error: Request failed with status code ${response.statusCode}`);
  }
});

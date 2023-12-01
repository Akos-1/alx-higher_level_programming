#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

if (!apiUrl) {
  console.log('Usage: node script_name.js API_URL');
  process.exit(1);
}

const characterUrl = `${apiUrl}${characterId}`;

request.get(characterUrl, handleApiResponse);

function handleApiResponse(error, response, body) {
  if (error) {
    return handleError(`An error occurred while making the request: ${error}`);
  }

  if (response.statusCode !== 200) {
    return handleError(`Error: Request failed with status code ${response.statusCode}`);
  }

  try {
    const moviesWithCharacter = parseCharacterData(body);

    console.log(`Number of movies where Wedge Antilles is present: ${moviesWithCharacter}`);
  } catch (parseError) {
    handleError(`Error parsing response body: ${parseError}`);
  }
}

function handleError(message) {
  console.error(message);
}

function parseCharacterData(body) {
  const characterData = JSON.parse(body);
  return characterData.films.length;
}

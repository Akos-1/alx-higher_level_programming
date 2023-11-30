#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.log('Usage: node script_name.js URL');
  process.exit(1);
}

try {
  request.get(url, (error, response) => {
    if (error) {
      console.error(`An error occurred while making the request: ${error}`);
      return;
    }
    console.log(`code: ${response.statusCode}`);
  });
} catch (error) {
  console.error(`An error occurred: ${error}`);
}

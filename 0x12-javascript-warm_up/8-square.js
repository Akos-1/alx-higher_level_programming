#!/usr/bin/node
const size = process.argv[2];

const squareSize = parseInt(size);

if (!isNaN(squareSize)) {
  for (let i = 0; i < squareSize; i++) {
    let line = '';
    for (let j = 0; j < squareSize; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}

#!/usr/bin/node
const x = process.argv[2];

const numberOfOccurrences = parseInt(x);

if (!isNaN(numberOfOccurrences)) {
  for (let i = 0; i < numberOfOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

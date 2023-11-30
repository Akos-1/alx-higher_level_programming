#!/usr/bin/node

const fs = require('fs');

const readAndPrintFile = (filePath) => {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log('File content:', content); // Log the file content
    if (content.includes('Error')) {
      console.log('Error found in file content.');
    } else {
      console.log('No error found in file content.');
    }
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
};

if (process.argv.length !== 3) {
  console.log('Usage: ./read_file.js <file_path>');
} else {
  const filePath = process.argv[2];
  console.log('Reading file:', filePath);
  readAndPrintFile(filePath);
}

#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
  console.log('Usage: node script_name.js file_path "content_to_write"');
  process.exit(1);
}

try {
  fs.writeFileSync(filePath, contentToWrite, 'utf-8');
  console.log(`Content successfully written to ${filePath}`);
} catch (error) {
  console.error(`An error occurred while writing to the file: ${error}`);
}

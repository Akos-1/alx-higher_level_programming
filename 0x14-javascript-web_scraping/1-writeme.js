#!/usr/bin/node

const fs = require('fs');

function writeToFile(filePath, content) {
  try {
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`Content successfully written to ${filePath}`);
  } catch (error) {
    console.error(`Error occurred: ${error.message}`);
  }
}

if (require.main === module) {
  const args = process.argv.slice(2);

  if (args.length !== 2) {
    console.error('Usage: node script.js <file_path> <content>');
    process.exit(1);
  }

  const filePath = args[0];
  const content = args[1];

  writeToFile(filePath, content);
}

module.exports = writeToFile;

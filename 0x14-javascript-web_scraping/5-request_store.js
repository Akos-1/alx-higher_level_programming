#!/usr/bin/node

const http = require('http');
const fs = require('fs');

const getAndStoreWebpage = (url, filePath) => {
    // Parse the URL to extract hostname and path
    const { hostname, path } = new URL(url);

    // Configure the HTTP request options
    const options = {
        hostname,
        path,
        method: 'GET',
    };

    // Send the HTTP request
    const req = http.request(options, (res) => {
        let content = '';

        // Concatenate chunks of data received
        res.on('data', (chunk) => {
            content += chunk;
        });

        // Write the content to the specified file once the response is complete
        res.on('end', () => {
            if (res.statusCode === 200) {
                fs.writeFileSync(filePath, content, 'utf-8');
                console.log(`Webpage content successfully stored in ${filePath}`);
            } else {
                console.log(`Failed to retrieve webpage. Status code: ${res.statusCode}`);
            }
        });
    });

    // Handle errors during the request
    req.on('error', (error) => {
        console.error(`An error occurred: ${error.message}`);
    });

    // End the request
    req.end();
};

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 4) {
    console.log('Usage: node script_name.js <URL> <file_path>');
} else {
    const url = process.argv[2];
    const filePath = process.argv[3];
    getAndStoreWebpage(url, filePath);
}

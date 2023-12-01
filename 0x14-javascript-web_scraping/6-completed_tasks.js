#!/usr/bin/node

const http = require('http');

function getRequest (apiUrl, callback) {
  http.get(apiUrl, (response) => {
    let data = '';

    response.on('data', (chunk) => {
      data += chunk;
    });

    response.on('end', () => {
      callback(null, { statusCode: response.statusCode, data });
    });
  }).on('error', (error) => {
    callback(error, null);
  });
}

function getCompletedTasks (apiUrl) {
  if (process.argv.length !== 3) {
    console.error('Usage: ./6-completed_tasks.js <API-URL>');
    process.exit(1);
  }

  getRequest(apiUrl, (error, response) => {
    if (error) {
      console.error(error.message);
      process.exit(1);
    }

    if (response.statusCode === 200) {
      const todos = JSON.parse(response.data);
      const completedTasksByUser = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          const userId = todo.userId.toString();
          completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
        }
      });

      console.log(completedTasksByUser);
    } else {
      console.error(`Failed to retrieve information. Status code: ${response.statusCode}`);
      process.exit(1);
    }
  });
}

const apiUrl = process.argv[2];
getCompletedTasks(apiUrl);

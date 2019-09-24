#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  const task = {};
  if (error) {
    return console.log(error);
  } else {
    for (let i = 0; i < JSON.parse(body).length; i++) {
      if (JSON.parse(body)[i].completed) {
        const count = JSON.parse(body)[i].userId;
        task[count] = (task[count] || 0) + 1;
      }
    }
  }
  console.log(task);
});

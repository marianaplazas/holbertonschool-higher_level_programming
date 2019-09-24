#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    let count = 0;
    for (const item of JSON.parse(body).results) {
      for (const character of item.characters) {
        if (character.includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

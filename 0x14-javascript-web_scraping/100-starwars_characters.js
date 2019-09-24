#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const charList = JSON.parse(body).characters;
    charList.forEach(function (element) {
      request.get(element, function (error, response, body) {
        if (error) {
          return console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});

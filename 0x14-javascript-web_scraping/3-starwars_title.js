#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request.get(url, function (err, res, data) {
  if (err);
  console.log(JSON.parse(data).title);
});

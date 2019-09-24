#!/usr/bin/node
let request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2];
request.get(url, function(err, res, data){
  console.log(JSON.parse(data)['title']);
});

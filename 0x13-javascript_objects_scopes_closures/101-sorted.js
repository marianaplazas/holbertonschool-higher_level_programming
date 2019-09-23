#!/usr/bin/node
const dict = require('./101-data').dict;
const dic = {};
for (const key in dict) {
  if (dic[dict[key]] === undefined) {
    dic[dict[key]] = [];
  }
  dic[dict[key]].push(key);
}
console.log(dic);

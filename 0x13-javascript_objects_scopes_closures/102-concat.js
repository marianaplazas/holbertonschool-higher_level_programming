#!/usr/bin/node
const FileOne = process.argv[2];
const FileTwo = process.argv[3];
const FileThree = process.argv[4];
const fs = require('fs');
const textA = fs.readFileSync(FileOne, 'utf8');
const textB = fs.readFileSync(FileTwo, 'utf8');
fs.writeFileSync(FileThree, textA + textB);

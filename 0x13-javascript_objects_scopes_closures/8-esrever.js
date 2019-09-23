#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (let i = 0; i <= list.length - 1; i++) {
    reverse.unshift(list[i]);
  }
  return (reverse);
};

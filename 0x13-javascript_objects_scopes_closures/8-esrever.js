#!/usr/bin/node

exports.esrever = function (list) {
  const myList = [];
  let index = 0;

  for (let i = list.length - 1; i >= 0; i--) {
    myList[index] = list[i];
    index += 1;
  }
  return myList;
};

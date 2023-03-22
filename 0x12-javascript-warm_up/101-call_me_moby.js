#!/usr/bin/node
/*
execute x times a function
*/

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < 3; i++) {
    theFunction();
  }
};

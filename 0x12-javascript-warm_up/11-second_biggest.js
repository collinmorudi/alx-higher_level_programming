#!/usr/bin/node

const numsList = process.argv.slice(2);

function secondBiggest (array) {
  if (array.length < 2) {
    return 0;
  } else {
    array.sort((x, y) => x - y);
    array.pop();
    return array.pop();
  }
}
console.log(secondBiggest(numsList));

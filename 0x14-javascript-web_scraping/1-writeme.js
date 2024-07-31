#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(filename, fileContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});

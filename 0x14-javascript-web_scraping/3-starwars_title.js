#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${filmId}`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.error(`Error Code: ${response.statusCode}`);
  }
});

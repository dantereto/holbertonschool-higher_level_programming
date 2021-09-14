#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
request(url, (err, res, body) => {
  if (err) {
      return console.log(err);
  }
    console.log(JSON.parse(body).title);
});

#!/usr/bin/node

const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) {
      return console.log(err);
  }
  const path = JSON.parse(body).results;
  let cont = 0;
  for (let i = 0; i < path.length; i++) {
    for (let j = 0; j < path[i].characters.length; j++) {
      if (path[i].characters[j].endsWith('18/')) {
        cont++;
      }
    }
  }
  console.log(cont);
});

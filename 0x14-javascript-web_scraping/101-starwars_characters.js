#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
function printC (chara, idx) {
  request(chara[idx], (err, res, body) => {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).name);
    if (idx + 1 < chara.length) {
      printC(chara, idx + 1);
    }
  });
}
request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const chara = JSON.parse(body).characters;
  printC(chara, 0);
});

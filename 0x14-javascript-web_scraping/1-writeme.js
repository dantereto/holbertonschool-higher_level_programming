#!/usr/bin/node

const fs = require('fs')
const content = 'Python is cool';

fs.writeFile(process.argv[2], process.argv[3], 'utf8', err => {
  if (err) {
    return console.log(err);
  }
});

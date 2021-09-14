#!/usr/bin/node

var myArgs = process.argv.slice(2);
const fs = require('fs')
fs.readFile(myArgs[2], 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  console.log(data)
})

#!/usr/bin/node
const val = parseInt(process.argv[2], 10);
if (isNaN(val)) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + val);
}
#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}

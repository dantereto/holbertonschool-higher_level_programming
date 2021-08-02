#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (x) {
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
if (num > 0) {
  console.log(factorial(num));
}

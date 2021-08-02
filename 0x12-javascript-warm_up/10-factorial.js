#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (x) {
  if (isNaN(x)) {
    console.log(1);
  }
  if (x === 1) {
    return 1;
  }
  return x * factorial(x - 1);
}
if (isNaN(num)) {
  console.log(1);
}
if (num > 0) {
  console.log(factorial(num));
}

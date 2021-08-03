#!/usr/bin/node
module.exports = class Rectangle {
  constructor (h, w) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.height));
    }
  }
  
  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }
  
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
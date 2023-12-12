#!/usr/bin/node

const getSquare = require('./5-square');

class Square extends getSquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(`${`${c}`.repeat(this.width)}`);
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(`${'X'.repeat(this.width)}`);
     }
   }
 }
}

module.exports = Square;

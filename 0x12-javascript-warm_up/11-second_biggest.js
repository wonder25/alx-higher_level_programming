#!/usr/bin/node

let largest = 0;
let sndLargest = 0;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv.forEach(element => {
    if (parseInt(element) > largest) {
      largest = parseInt(element);
    }
  });

  process.argv.forEach(element => {
    if (parseInt(element) > sndLargest && parseInt(element) < largest) {
      sndLargest = parseInt(element);
    }
  });
  console.log(sndLargest);
}


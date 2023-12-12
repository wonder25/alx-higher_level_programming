#!/usr/bin/node

exports.esrever = function (list) {
  const reverList = [];

  list.forEach(element => {
    reverList.unshift(element);
  });
  return reverList;
};

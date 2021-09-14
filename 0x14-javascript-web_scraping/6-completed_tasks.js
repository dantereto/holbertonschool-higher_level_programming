#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const todos = JSON.parse(body);
  const completed = {};
  todos.forEach((todo) => {
    if (todo.completed && completed[todo.userId] === undefined) {
      completed[todo.userId] = 1;
    } else if (todo.completed) {
      completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});

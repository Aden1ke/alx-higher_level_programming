#!/usr/bin/node

const request = require('request');
const urlToMakeReq = process.argv[2];

request(urlToMakeReq, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});

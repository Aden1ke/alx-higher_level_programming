#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonData = JSON.parse(body).results;
    let count = 0;

    for (let i = 0; i < jsonData.length; i++) {
      const characters = jsonData[i].characters;

      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          count++;
        }
      }
    }

    console.log(count);
  }
});

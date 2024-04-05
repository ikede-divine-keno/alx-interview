#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body);
    processcharacters(results.characters, 0);
  }
});

function processcharacters (characters, n) {
  request(characters[n], function (error, res, body1) {
    if (error) {
      console.log(error);
    }
    const data1 = JSON.parse(body1);
    console.log(data1.name);

    if (n + 1 < characters.length) {
      processcharacters(characters, n + 1);
    }
  });
}

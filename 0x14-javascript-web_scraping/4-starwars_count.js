#!/usr/bin/node

/**
 * Star Wars Movie Count with Character
 * ------------------------------------
 *
 * Description: This script retrieves the number of movies where the character
 *              "Wedge Antilles" is present based on the Star Wars API.
 *
 * Author: John Doe
 *
 * Date: February 20, 2024
 *
 * Usage: node starwars-count-with-character.js [api_url]
 *
 * Exceptions:
 * - Error: Raised when an unexpected error occurs during the API request or response parsing.
 * - TypeError: Raised when the API URL is not provided as a command line argument.
 *
 * Star Wars API Endpoint: https://swapi-api.alx-tools.com/api/films/
 * Character ID: 18
 *
 * Example Usage:
 *   - node starwars-count-with-character.js https://swapi-api.alx-tools.com/api/films
 *
 * Dependencies:
  - request module: Used to make HTTP requests to the Star Wars API.
 **/
const request = require('request')
const starWarsUri = process.argv[2]
let times = 0

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j]
      const characterId = character.split('/')[5]

      if (characterId === '18') {
        times += 1
      }
    }
  }

  console.log(times)
})

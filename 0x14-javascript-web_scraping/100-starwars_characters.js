#!/usr/bin/node

/**
 * Star Wars Movie Characters
 * --------------------------
 *
 * Description: This script retrieves the characters of a Star Wars movie based on the movie ID
 *              and prints their names, one character per line.
 *
 * Author: sebsibe solomon
 *
 * Date: February 20, 2024
 *
 * Usage: node starwars_characters.js [movie_id]
 *
 * Exceptions:
 * - Error: Raised when an unexpected error occurs during the request or data processing.
 * - TypeError: Raised when the movie ID is not provided as a command line argument.
 *
 * Dependencies:
 * - request module: Used to send HTTP requests and retrieve the data.
 *
 * API Used:
 * - Star Wars API (https://swapi.dev/)
 */

const request = require('request');

// Retrieve the movie ID from the command line argument
const movieId = process.argv[2];

// Construct the API URL based on the movie ID
const movieUrl = `https://swapi.dev/api/films/${movieId}`;

// Send a GET request to the Star Wars API to fetch the movie details
request(movieUrl, function (error, response, body) {
  if (error) {
    console.error(`Error occurred while fetching movie details: ${error}`);
  } else if (response.statusCode === 200) {
    // Parse the response body as JSON
    const movie = JSON.parse(body);
    const characters = movie.characters;

    // Iterate over the character URLs and send separate GET requests for each character
    characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error(`Error occurred while fetching character details: ${error}`);
        } else if (response.statusCode === 200) {
          // Parse the response body as JSON
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
        }
      });
    });
  } else {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
  }
});

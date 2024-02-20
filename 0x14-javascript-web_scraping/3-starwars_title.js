#!/usr/bin/node
/**
 * Star Wars Movie Title Fetcher
 * -----------------------------
 *
 * Description: This script retrieves and prints the title of a Star Wars movie
 *              based on the episode number provided by the user.
 *
 * Author: sebsibe solomon
 *
 * Date: February 20, 2024
 *
 * Usage: node starwars-title-fetcher.js [movie_id]
 *
 * Exceptions:
 * - Error: Raised when an unexpected error occurs during the API request or response parsing.
 * - TypeError: Raised when the movie ID is not provided as a command line argument.
 *
 * API Endpoint: https://swapi-api.alx-tools.com/api/films/:id
 *
 * Example Usages:
 *   - node starwars-title-fetcher.js 1
 *   - node starwars-title-fetcher.js 5
 *
 * Dependencies:
 * - request module: Used to make HTTP requests to the Star Wars API.
 */
const request = require('request');
const movieId = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiURL, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
  }
});

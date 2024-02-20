#!/usr/bin/node
/**
 * Star Wars Movie Characters
 * --------------------------
 *
 * Description: This script retrieves and prints the characters of a Star Wars movie
 *              based on the movie ID, displaying one character name per line. The
 *              characters are printed in the same order as the list "characters" in
 *              the `/films/` response from the Star Wars API.
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
const request = require('request')
const movieId = process.argv[2]
const apiUrl = `https://swapi.dev/api/films/${movieId}`
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error)
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body)
    const characters = movie.characters
    const characterRequests = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            reject(error)
          } else if (response.statusCode === 200) {
            const character = JSON.parse(body)
            resolve(character.name)
          } else {
            reject(new Error(`Error: ${response.statusCode} - ${response.statusMessage}`))
          }
        })
      })
    })
    Promise.all(characterRequests)
      .then((characterNames) => {
        characterNames.forEach((characterName) => {
          console.log(characterName)
        })
      })
      .catch((error) => {
        console.error(error)
      })
  } else {
    console.error(new Error(`Error: ${response.statusCode} - ${response.statusMessage}`))
  }
})

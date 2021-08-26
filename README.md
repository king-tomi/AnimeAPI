# Anime Source API. Get information about your favorite anime, manga, characters, reviews and ratings!

### This API allows you collect the information you need about an anime, manga, characters of the anime/manga, reviews
### and ratings.

### It's a database-less API, the source is https://anime-planet/com

### The Api is hosted on https://animesource.herokuapp.com/

## ENDPOINTS exposed

### There are two endpoints but it reacts according to the user's request

### api/section/name/target where section is either anime or manga and name is the name of the anime/manga while taget is the information the uer needs

### Examples 
### https://animesource.herokuapp.com/api/anime/naruto/characters will return all the characters of Naruto anime

### api/section/name where section is either anime or manga and name is the name of the anime/manga. This returns basic information about the anime including the number of chapters, the studio, year of running and average ratings

### Examples 
### https://animesource.herokuapp.com/api/anime/naruto/characters will return all the characters of Naruto anime
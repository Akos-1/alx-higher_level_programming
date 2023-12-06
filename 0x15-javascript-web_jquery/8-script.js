// Use jQuery to wait for the document to be ready
$(document).ready(function () {
  // Use jQuery to fetch data from the provided URL
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Use jQuery to select the ul with id list_movies
    var listMovies = $('#list_movies');

    // Loop through each movie in the fetched data
    $.each(data.results, function (index, movie) {
      // Create a new li element with the movie title and append it to the ul
      listMovies.append('<li>' + movie.title + '</li>');
    });
  });
});

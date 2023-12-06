// Use jQuery to wait for the document to be ready
$(document).ready(function () {
  // Use jQuery to fetch data from the provided URL
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extract the character name from the fetched data
    var characterName = data.name;

    // Use jQuery to select the div with id character and update its text with the fetched character name
    $('#character').text(characterName);
  });
});

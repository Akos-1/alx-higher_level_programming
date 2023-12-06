// Use jQuery to fetch data from the provided URL
$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  // Use jQuery to select the div with id hello and update its text with the fetched translation
  $('#hello').text(data.hello);
});

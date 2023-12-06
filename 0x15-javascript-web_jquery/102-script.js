// Use jQuery to wait for the document to be ready
$(document).ready(function () {
  // Use jQuery to select the input with id btn_translate and add a click event handler
  $('#btn_translate').click(function () {
    // Use jQuery to get the value entered in the input with id language_code
    var languageCode = $('#language_code').val();

    // Use jQuery to fetch data from the provided API service with the entered language code
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode, function (data) {
      // Use jQuery to select the div with id hello and update its text with the fetched translation
      $('#hello').text(data.hello);
    });
  });
});

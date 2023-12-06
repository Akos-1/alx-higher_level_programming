// Use jQuery to wait for the document to be ready
$(document).ready(function () {
  // Use jQuery to select the input with id btn_translate and add a click event handler
  $('#btn_translate').click(fetchTranslation);

  // Use jQuery to select the input with id language_code and add a keypress event handler
  $('#language_code').keypress(function (e) {
    // Check if the pressed key is ENTER (key code 13)
    if (e.which === 13) {
      fetchTranslation();
    }
  });

  // Function to fetch translation based on the entered language code
  function fetchTranslation() {
    // Use jQuery to get the value entered in the input with id language_code
    var languageCode = $('#language_code').val();

    // Use jQuery to fetch data from the provided API service with the entered language code
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode, function (data) {
      // Use jQuery to select the div with id hello and update its text with the fetched translation
      $('#hello').text(data.hello);
    });
  }
});

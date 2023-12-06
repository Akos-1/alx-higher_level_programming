// Use jQuery to wait for the document to be ready
$(document).ready(function () {
  // Use jQuery to select the div with id red_header and add a click event handler
  $('#red_header').click(function () {
    // Inside the click event handler, use jQuery to select the header element and add the class 'red'
    $('header').addClass('red');
  });
});

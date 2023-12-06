// Use jQuery to wait for the document to be ready
$(document).ready(function () {
  // Use jQuery to select the div with id toggle_header and add a click event handler
  $('#toggle_header').click(function () {
    // Inside the click event handler, use jQuery to select the header element
    var header = $('header');

    // Toggle the class 'red' and 'green' in the header element
    header.toggleClass('red green');
  });
});

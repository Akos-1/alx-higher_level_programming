// Use jQuery to wait for the document to be ready
$(document).ready(function () {
  // Use jQuery to select the div with id update_header and add a click event handler
  $('#update_header').click(function () {
    // Use jQuery to select the header element and update its text to "New Header!!!"
    $('header h1').text('New Header!!!');
  });
});

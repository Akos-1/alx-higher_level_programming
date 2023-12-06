// Use jQuery to wait for the document to be ready
$(document).ready(function () {
  // Use jQuery to select the div with id add_item and add a click event handler
  $('#add_item').click(function () {
    // Create a new li element with the text "Item"
    var newItem = $('<li>Item</li>');

    // Use jQuery to select the ul with class my_list and append the new li element to it
    $('ul.my_list').append(newItem);
  });
});


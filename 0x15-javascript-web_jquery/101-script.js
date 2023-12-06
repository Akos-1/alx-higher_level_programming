// Use jQuery to wait for the document to be ready
$(document).ready(function () {
  // Use jQuery to select the div with id add_item and add a click event handler
  $('#add_item').click(function () {
    // Create a new li element with the text "Item"
    var newItem = $('<li>Item</li>');

    // Use jQuery to select the ul with class my_list and append the new li element to it
    $('ul.my_list').append(newItem);
  });

  // Use jQuery to select the div with id remove_item and add a click event handler
  $('#remove_item').click(function () {
    // Use jQuery to select the last li element in the ul with class my_list and remove it
    $('ul.my_list li:last-child').remove();
  });

  // Use jQuery to select the div with id clear_list and add a click event handler
  $('#clear_list').click(function () {
    // Use jQuery to select all li elements in the ul with class my_list and remove them
    $('ul.my_list li').remove();
  });
});

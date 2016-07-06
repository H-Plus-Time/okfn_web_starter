// client-side js
// run by the browser each time your view template is loaded

// protip: you can rename this to use .coffee if you prefer

// by default, you've got jQuery,
// add other scripts at the bottom of index.html

$(function() {
  
  // Switching up to the Fetch Web API
  $.get('/users', function(data) {
    data.users.forEach(function(user) {
      $('<li>' + user.name + '</li>').appendTo('ul#users');

    });
  });

});

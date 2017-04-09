$(document).ready(function () {
  var socket = io.connect('http//' + document.domain + ':' + location.port);
  var lemons = new Array("/static/lemon.png", "/static/split-lemon.png");
  var count = 0;
  var stop = false;

  // Stop and start from 
  $('#submission-box button').click(function(){
    socket.emit('initialize', $('#input-box div').html());
    $('#result-box div').html("");
    stop = false;
  });
  $('#remission-box button').click(function(){
    stop = true;
  });

  // Splitting socket events.
  socket.on('splitter-ready', function(data) {
    socket.emit('split')
  });

  socket.on('split-sequence', function(data) {
    // Unless told to stop, continue splitting.
    if (!stop) {
      $('#result-box div').html(data);
      $('#lemon img').attr("src",lemons[count % 2]);
      count++;
      socket.emit('split')
    }
  });

  socket.on('splitter-ready', function(data) {
    socket.emit('split')
  });

  socket.on('split-ended', function(data) {
    $('#result-box div').html(data);
    $('#lemon img').attr("src","/static/split-lemon.png");
    count = 0;
  });

  $('#input-box div').click(function() {
    if ($('#input-box div').html() == "ENTER TEXT") {
      $('#input-box div').html("")
    }
  });
  $('#input-box div').blur(function() {
    if ($('#input-box div').html() == "") {
      $('#input-box div').html("ENTER TEXT")
    }
  });

  // Count the number of characters in the input.
  $('#input-box div').keyup(function() {
    var characters = $('#input-box div').html().length
    console.log(characters + "/100")
    $('#submission-box div').html(characters + "/100")
  });
})

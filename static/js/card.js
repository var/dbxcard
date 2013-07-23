// Vimal Atreya Ramaka
// Copyright (C) 2013 Vimal Atreya Ramaka
// license GPLv2
// version 0.2

function setDivSize() {
  var wWidth = $(window).width();
  var wHeight = $(window).height();

  var ch = $("#content").outerHeight();

  var ptop = ((wHeight / 2) - (ch / 4));

  $('#content').css('padding-top', ptop + 'px');

  $('#content').css('visibility', 'visible');
  $('#content').addClass('animated fadeIn');

}

$(document).ready(function() {
  setDivSize();
});

$(window).resize(function() {
  setDivSize();
});

$(window).load(function() {    

  var theWindow        = $(window),
      $bg              = $("#bg"),
      aspectRatio      = $bg.width() / $bg.height();
                    
  function resizeBg() {
    
    if ( (theWindow.width() / theWindow.height()) < aspectRatio ) {
        $bg
          .removeClass()
          .addClass('bgheight');
    } else {
        $bg
          .removeClass()
          .addClass('bgwidth');
    }

    $('#bg').css('visibility', 'visible');
    $('#bg').addClass('animated fadeIn');
          
  }
                          
  theWindow.resize(resizeBg).trigger("resize");

});
/*
$(function() {
  function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }
  $('.nav-content').hide();
  $('.content').css('margin-left', $('.nav-bar').innerWidth());
  document.getElementsByClassName('content')[0].style.width = 'calc(100vw - ' + $('nav-bar').innerWidth() + 'px)';
  $('#menu-icon').on('click', function() {
    if ($(this).attr('uk-icon') == "icon: menu; ratio:1.5") {
      $(this).hide().attr('uk-icon', 'icon: close; ratio:1.5').fadeIn(200);
      $('.nav-content').fadeIn(200);
      $('.nav-bar').addClass('nav-content-enlarged');
    } else {
      $(this).hide().attr('uk-icon', 'icon: menu; ratio:1.5').fadeIn(200);
      $('.nav-content').fadeOut(200);
      $('.nav-bar').removeClass('nav-content-enlarged');
    }
    if (document.getElementsByClassName('nav-content-enlarged')[0]) {
      document.getElementsByClassName('content')[0].style.marginLeft = 'calc(30vh + 40px)';
    } else {
      document.getElementsByClassName('content')[0].style.marginLeft = 'calc(6vh + 40px)';
    }
  });
});
*/

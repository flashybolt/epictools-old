$(function() {
  $('.nav-content').hide();
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
  });
});

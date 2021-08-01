function validateStyler(mess, type, name, placeholder) {
  $('input[name=' + name + ']').attr('placeholder', mess).attr('type', 'text').addClass('uk-form-danger');
  $('link[href="/static/css/placeholder.css"]').prop('disabled', false);
  $('input[name=' + name + ']').on('click', function() {
    $(this).removeClass('uk-form-danger').attr('type', type).attr('placeholder', placeholder);
    $('link[href="/static/css/placeholder.css"]').prop('disabled', true);
  });
  $(document).on('unload', function() {
    $('input').attr('placeholder', placeholder).attr('type', type).removeClass('uk-form-danger');
  });
}

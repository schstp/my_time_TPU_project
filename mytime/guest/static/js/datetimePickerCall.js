$('#task-group-container').click( function (e) {
   e.preventDefault();
   $("#task-group-container").datetimepicker({
        format: 'DD/MM/YYYY HH:mm',
       locale: 'ru',
    });
});

    $(document).on('mouseup touchend', function (e) {
      var container = $('.bootstrap-datetimepicker-widget');
      if (!container.is(e.target) && container.has(e.target).length === 0) {
            container.parent().datetimepicker('hide');
      }
});
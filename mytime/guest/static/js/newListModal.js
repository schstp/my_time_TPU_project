$('#exampleModal').on('show.bs.modal', function (event) {
  let newListTitleInput = $('#new-list-title');
  let saveButton = $('#saveNewList');
  let closeButton = $('#closeModal');

  //делаем кнопку "Сохранить" доступной, только если поле не пустое
  newListTitleInput.keyup( function (e) {
    if ($.trim(newListTitleInput.val()) !== '') {
      saveButton.prop('disabled',false);
      if (e.keyCode === 13) { //не работает
        e.preventDefault();
        saveButton.click();
      }
    }
    else saveButton.prop('disabled',true);
  });

  //обработчик клика по кнопке "Сохранить"
  saveButton.click( function (e) {
    saveButton.prop('disabled', true);

    let newListTitle = newListTitleInput.val();
    newListTitleInput.val('');
    closeButton.click();

    if ($.trim(newListTitle) !== '') {
      let csrftoken = getCookie('csrftoken');

      let data = {
        list_title: newListTitle,
        csrfmiddlewaretoken: csrftoken,
      };

      $.ajax({
        type: 'POST',
        url: 'add_list',
        dataType: 'json',
        data: data,
        success: function (data) {
          let icon = document.createElement('img');
          icon.className = 'icon';
          icon.src = '/static/my_time/img/personal-list.png';

          let title = document.createTextNode(data['title']);

          let div = document.createElement('div');
          div.className = 'float-right';
          let spanOverdue = document.createElement('span');
          spanOverdue.className = 'badge badge-pill badge-danger';
          spanOverdue.id = 'overdueBadge' + data['id'];
          let spanAll = document.createElement('span');
          spanAll.className = 'badge badge-pill badge-light';
          spanAll.id = 'allBadge' + data['id'];
          div.appendChild(spanOverdue);
          div.appendChild(spanAll);

          let a = document.createElement('a');
          a.className = 'nav-link';
          a.href = '#';
          a.id = data['id'];
          a.setAttribute('onclick', 'changeList(this)');

          a.appendChild(icon);
          a.appendChild(title);
          a.appendChild(div);

          let li = document.createElement('li');
          li.className = 'nav-item';
          li.appendChild(a);

          lists.appendChild(li);
          a.click();
        }
      })
  }
  })
});
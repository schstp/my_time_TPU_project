

var csrftoken = getCookie('csrftoken');

var newTaskInputElement = $('#newTaskInput');
var newTaskButtonElement = $('#newTaskButton');

newTaskButtonElement.on('click', function (e) {
    e.preventDefault();
    newTaskInput.dispatchEvent(new KeyboardEvent('keydown',{'keyCode': 13}))
});

newTaskInputElement.on('keydown', function(e) {
    if (e.keyCode === 13) {
        e.preventDefault();


        let title = newTaskInputElement.val();
        let activeList = document.getElementById('lists').querySelector('.active').querySelector('a');

        let data = {
            title: title,
            active_list: activeList.id,
            csrfmiddlewaretoken: csrftoken,
        };

        $.ajax({
            type: 'POST',
            url: 'add_task',
            dataType: 'json',
            data: data,
            success: function (data) {
                if ($.trim(newTaskInputElement.val())) {
                    let input = document.createElement('input');
                    input.className = 'custom-control-input';
                    input.type = 'checkbox';
                    input.id = 'customCheck' + data['id'];

                    let label = document.createElement('label');
                    label.className = 'custom-control-label';
                    label.setAttribute('for', input.id);
                    label.innerHTML = data['title'];

                    let div = document.createElement('div');
                    div.className = 'custom-control custom-checkbox';
                    div.appendChild(input);
                    div.appendChild(label);

                    let newTask = document.createElement('li');
                    newTask.className = 'list-group-item item-alignment fadeInDown';
                    newTask.appendChild(div);

                    listRoot.insertBefore(newTask, listRoot.firstChild);

                    newTaskInputElement.val('');
                    newTaskInputElement.blur();
                }
            }
        })
    }
});
let csrftoken = getCookie('csrftoken');

let newTaskInputElement = $('#newTaskInput');
let newTaskButtonElement = $('#newTaskButton');

newTaskButtonElement.on('click', function (e) {
    e.preventDefault();
    newTaskInput.dispatchEvent(new KeyboardEvent('keydown',{'keyCode': 13}))
});

newTaskInputElement.on('keydown', function(e) {
    if (e.keyCode === 13) {
        e.preventDefault();


        let title = newTaskInputElement.val();
        let activeListId = document.getElementById('lists').querySelector('.active').querySelector('a').id;

        let data = {
            title: title,
            active_list_id: activeListId,
            starred: true,
            planned_on: null,
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

                    for (let list in data['smart_lists']) {
                        let overdueBadge = document.getElementById('overdueBadge' + data['smart_lists'][list]['slug']);
                        let allBadge = document.getElementById('allBadge' + data['smart_lists'][list]['slug']);

                        if (data['smart_lists'][list]['count_tasks']) {
                            if (data['smart_lists'][list]['count_overdue_tasks']) {
                                overdueBadge.innerHTML = data['smart_lists'][list]['count_overdue_tasks'];
                            }
                            allBadge.innerHTML = data['smart_lists'][list]['count_tasks'];
                        }
                    }

                    for (let list in data['personal_lists']) {
                        let overdueBadge = document.getElementById('overdueBadge' + data['personal_lists'][list]['id']);
                        let allBadge = document.getElementById('allBadge' + data['personal_lists'][list]['id']);

                        if (data['personal_lists'][list]['count_tasks']) {
                            if (data['personal_lists'][list]['count_overdue_tasks']) {
                                overdueBadge.innerHTML = data['personal_lists'][list]['count_overdue_tasks'];
                            }
                            allBadge.innerHTML = data['personal_lists'][list]['count_tasks'];
                        }
                    }
                }
            }
        })
    }
});
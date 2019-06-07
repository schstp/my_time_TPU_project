let csrftoken = getCookie('csrftoken');
let newTaskButtonElement = $('#newTaskButton');

newTaskButtonElement.on('click', function (e) {
    e.preventDefault();
    newTaskInput.dispatchEvent(new KeyboardEvent('keydown',{'keyCode': 13}))
});

newTaskInputElement.on('keydown', function(e) {
    if (e.keyCode === 13 && $.trim(newTaskInputElement.val()) !== '') {
        e.preventDefault();
        //console.log($('#task-group-container').datetimepicker('date'));
        let title = newTaskInputElement.val();

        let starred = starredChechbox.is(':checked');
        if (starredChechbox.is(':checked')) markTask.click();

        let activeListId = document.getElementById('lists').querySelector('.active').id;

        let data = {
            title: title,
            active_list_id: activeListId,
            starred: starred,
            planned_on: null,
            csrfmiddlewaretoken: csrftoken,
        };

        $.ajax({
            type: 'POST',
            url: 'add_task',
            dataType: 'json',
            data: data,
            success: function (data) {
                let input = document.createElement('input');
                input.className = 'custom-control-input';
                input.type = 'checkbox';
                input.id = 'customCheck' + data['id'];

                let label = document.createElement('label');
                label.className = 'custom-control-label task-title-alignment';
                label.setAttribute('for', input.id);
                label.setAttribute('onclick', 'archiveTask(this)');
                label.innerHTML = data['title'];

                let div1 = document.createElement('div');
                div1.className = 'custom-control custom-checkbox float-left task-inner-alignment';
                div1.appendChild(input);
                div1.appendChild(label);

                let img = document.createElement('img');
                img.className = 'icon-star';
                img.src = '/static/my_time/img/';
                if (data['starred']) img.src += 'starred.png';
                else img.src += 'notstarred.png';

                let checkInput = document.createElement('input');
                checkInput.style.visibility = 'hidden';
                checkInput.type = 'checkbox';
                if (data['starred'])  checkInput.checked = true;
                else  checkInput.checked = false;

                let button = document.createElement('button');
                button.className = 'button-star';
                button.appendChild(img);
                button.appendChild(checkInput);

                let div2 = document.createElement('div');
                div2.className = 'float-right checklabel';
                div2.style.marginRight = '-0.9rem';
                div2.appendChild(button);

                let newTask = document.createElement('li');
                newTask.id = data['id'];
                newTask.className = 'list-group-item item-alignment fadeInDown';
                newTask.appendChild(div1);
                newTask.appendChild(div2);

                listRoot.insertBefore(newTask, listRoot.firstChild);

                newTaskInputElement.val('');

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
        })
    }
});
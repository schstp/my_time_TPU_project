function changeList(self) {
    let activeListId = self.id;
    let previousActiveList = document.getElementById('lists').querySelector('.active');
    let data = {
        'active_list_id': activeListId,
    };

    let taskInsertionForm = document.getElementById('taskInsertionForm');
    let headStatementElement = document.getElementById('headstatement');

    $.ajax({
        type: 'GET',
        url: 'active_list',
        dataType: 'json',
        data: data,
        success:function(data){
            if (!self.isEqualNode(previousActiveList)) {
                self.className += ' active list-group-item-primary';
                previousActiveList.className = "nav-link";
                listRoot.innerHTML = '';
                if (activeListId === 'week') taskInsertionForm.style.display = 'None';
                else taskInsertionForm.style.display = '';
                if (activeListId === 'starred') {
                    markTask.parentNode.style.display = 'None';
                    document.getElementById('task-group-container').removeChild( document.getElementById('starredcheckbox-container'))
                }
                else if (!document.getElementById('starredcheckbox-container')) {
                    let div = document.createElement('div');
                    div.className = 'input-group-append';
                    div.id = 'starredcheckbox-container';
                    div.innerHTML = markTask.outerHTML;
                    document.getElementById('task-group-container').appendChild(div);
                }

                if (activeListId === 'inbox') newTaskInput.placeholder = 'Добавить задачу...';
                if (activeListId === 'today') newTaskInput.placeholder = 'Добавить сегодняшнюю задачу в папку "Входящие"...';
                if (activeListId === 'tomorrow') newTaskInput.placeholder = 'Добавить задачу на завтра в папку "Входящие"...';
                if (activeListId === 'starred') newTaskInput.placeholder = 'Добавить отмеченную звездочкой задачу в папку "Входящие"...';
                if (activeListId === 'all') newTaskInput.placeholder = 'Добавить задачу в папку "Входящие"...';
                if (+activeListId) newTaskInput.placeholder = 'Добавить задачу...';

                headStatementElement.innerHTML = data['list_title'];

                $.each(data['tasks'], function (index) {
                    let input = document.createElement('input');
                    input.className = 'custom-control-input';
                    input.type = 'checkbox';
                    input.id = 'customCheck' + data['tasks'][index]['id'];

                    let label = document.createElement('label');
                    label.className = 'custom-control-label task-title-alignment';
                    label.setAttribute('for', input.id);
                    label.setAttribute('onclick', 'archiveTask(this)');
                    label.innerHTML = data['tasks'][index]['title'];

                    let div1 = document.createElement('div');
                    div1.className = 'custom-control custom-checkbox float-left task-inner-alignment';
                    div1.appendChild(input);
                    div1.appendChild(label);

                    let img = document.createElement('img');
                    img.className = 'icon-star';
                    img.src = '/static/my_time/img/';
                    if (data['tasks'][index]['starred']) img.src += 'starred.png';
                    else img.src += 'notstarred.png';

                    let checkInput = document.createElement('input');
                    checkInput.style.visibility = 'hidden';
                    checkInput.type = 'checkbox';

                    let button = document.createElement('button');
                    button.className = 'button-star';
                    button.appendChild(img);
                    button.appendChild(checkInput);

                    let div2 = document.createElement('div');
                    div2.className = 'float-right checklabel';
                    div2.style.marginRight = '-0.9rem';
                    div2.appendChild(button);

                    let newTask = document.createElement('li');
                    newTask.id = data['tasks'][index]['id'];
                    newTask.className = 'list-group-item item-alignment fadeInDown';
                    newTask.appendChild(div1);
                    newTask.appendChild(div2);

                    listRoot.insertBefore(newTask, listRoot.firstChild);
                })
            }
        }
    })
}
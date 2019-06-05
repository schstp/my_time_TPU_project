function changeList(self) {
    let activeListId = self.id;
    let previousActiveList = document.getElementById('lists').querySelector('.active');
    let data = {
        'active_list_id': activeListId,
    };

    let taskInsertionForm = document.getElementById('taskInsertionForm')
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
                
                if (activeListId === 'inbox' || typeof +activeListId === "number") newTaskInput.placeholder = 'Добавить задачу...';
                if (activeListId === 'today') newTaskInput.placeholder = 'Добавить сегодняшнюю задачу в папку "Входящие"...';
                if (activeListId === 'tomorrow') newTaskInput.placeholder = 'Добавить задачу на завтра в папку "Входящие"...';
                if (activeListId === 'starred') newTaskInput.placeholder = 'Добавить отмеченную звездочкой задачу в папку "Входящие"...';
                if (activeListId === 'all') newTaskInput.placeholder = 'Добавить задачу в папку "Входящие"...';

                $.each(data['tasks'], function (index) {

                    let input = document.createElement('input');
                    input.className = 'custom-control-input';
                    input.type = 'checkbox';
                    input.id = 'customCheck' + data['tasks'][index]['id'];

                    let label = document.createElement('label');
                    label.className = 'custom-control-label';
                    label.setAttribute('for', input.id);
                    label.innerHTML = data['tasks'][index]['title'];

                    let div = document.createElement('div');
                    div.className = 'custom-control custom-checkbox';
                    div.appendChild(input);
                    div.appendChild(label);

                    let newTask = document.createElement('li');
                    newTask.className = 'list-group-item item-alignment fadeInDown';
                    newTask.appendChild(div);

                    listRoot.insertBefore(newTask, listRoot.firstChild)
                })
            }
        }
    })
}
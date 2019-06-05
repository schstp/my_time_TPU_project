function changeList(self) {
    let activeListId = self.id;
    let previousActiveList = document.getElementById('lists').querySelector('.active');
    let data = {
        'active_list_id': activeListId,
    };

    $.ajax({
        type: 'GET',
        url: 'active_list',
        dataType: 'json',
        data: data,
        success:function(data){
            self.parentElement.className += ' active list-group-item-primary';

            previousActiveList.className = "nav-item";
            listRoot.innerHTML='';
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
    })
}
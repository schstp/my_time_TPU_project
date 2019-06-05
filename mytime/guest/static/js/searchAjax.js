let searchBarElement = $('#searchbar');
let taskInsertionForm = document.getElementById('taskInsertionForm');

let flag = true;
let previousQuery = 'not empty';

searchBarElement.keyup( function (e) {
    let query = searchBarElement.val();

    taskInsertionForm.style.display = 'None';
    if (!query) taskInsertionForm.style.display = '';

    if (!query && !previousQuery) flag=false;
    else flag=true;

    previousQuery = query;

    let activeList = document.getElementById('lists').querySelector('.active').querySelector('a');
    let data = {
        q: query,
        active_list: activeList.id,
    };

    $.ajax({
        type: 'GET',
        url: 'search_query',
        dataType: 'json',
        data: data,
        success:function(data){
            if (flag) {
                listRoot.innerHTML='';
                $.each(data, function (index) {
                    let input = document.createElement('input');
                    input.className = 'custom-control-input';
                    input.type = 'checkbox';
                    input.id = 'customCheck' + data[index]['id'];

                    let label = document.createElement('label');
                    label.className = 'custom-control-label';
                    label.setAttribute('for', input.id);
                    label.innerHTML = data[index]['title'];

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

});
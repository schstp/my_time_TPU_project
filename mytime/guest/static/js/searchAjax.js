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

    let activeList = document.getElementById('lists').querySelector('.active');
    let data = {
        q: query,
        active_list_id: activeList.id,
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
                    label.className = 'custom-control-label task-title-alignment';
                    label.setAttribute('for', input.id);
                    label.setAttribute('onclick', 'archiveTask(this)');
                    label.innerHTML = data[index]['title'];

                    let div1 = document.createElement('div');
                    div1.className = 'custom-control custom-checkbox float-left task-inner-alignment';
                    div1.appendChild(input);
                    div1.appendChild(label);

                    let img = document.createElement('img');
                    img.className = 'icon-star';
                    img.src = '/static/my_time/img/';
                    if (data[index]['starred']) img.src += 'starred.png';
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
                    newTask.id = data[index]['id'];
                    newTask.className = 'list-group-item item-alignment fadeInDown';
                    newTask.appendChild(div1);
                    newTask.appendChild(div2);

                    listRoot.insertBefore(newTask, listRoot.firstChild);
                })
            }
        }
    })

});
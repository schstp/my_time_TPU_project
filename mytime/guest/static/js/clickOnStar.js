$('#listRoot').delegate('button', 'click', function(e) {
    e.preventDefault();

    let star = $(this).find('input');
    let starImg = $(this).find('img');

    if (!star.is(':checked')) {
        starImg.prop('src', '/static/my_time/img/starred.png');
        star.prop('checked', true);
    }
    else {
        starImg.prop('src', '/static/my_time/img/notstarred.png');
        star.prop('checked', false);
    }

    let csrftoken = getCookie('csrftoken');
    let task = $(this).closest('li');

    let data = {
            task_id: task.prop('id'),
            starred: star.is(':checked'),
            csrfmiddlewaretoken: csrftoken,
    };

    $.ajax({
        type: 'POST',
        url: 'swap_starred',
        dataType: 'json',
        data: data,
        success: function (data) {
            let activeList = document.getElementById('lists').querySelector('.active');
            let overdueBadge = document.getElementById('overdueBadge' + data['slug']);
            let allBadge = document.getElementById('allBadge' + data['slug']);

            if (data['count_tasks']) {
                    allBadge.innerHTML = data['count_tasks'];
                }
                else if (allBadge) {
                    allBadge.innerHTML = '';
                }

                if (data['count_overdue_tasks']) {
                        overdueBadge.innerHTML = data['count_overdue_tasks'];
                }
                else if (overdueBadge){
                    overdueBadge.innerHTML = '';
                }

            if (activeList.id === 'starred') {
                task[0].className += ' fadeOut';
                function removeTask () {

                    listRoot.removeChild(task[0]);
                }
                setTimeout(removeTask, 180);
            }
        }
    })

});
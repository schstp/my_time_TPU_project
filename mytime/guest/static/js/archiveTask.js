function archiveTask(self) {
    let csrftoken = getCookie('csrftoken');

    let taskToArchiveId = self.parentNode.parentNode.id;
    let data = {
        'task_to_archive_id': taskToArchiveId,
        csrfmiddlewaretoken: csrftoken,
    };


    $.ajax({
        type: 'POST',
        url: 'archive_task',
        dataType: 'json',
        data: data,
        success:function(data){
            let li = listRoot.querySelector('[id="' + taskToArchiveId +'"]');
            li.className += ' fadeOut';
            function removeTask () {
                listRoot.removeChild(li);
            }
            setTimeout(removeTask, 180);

            //badge refreshing
            for (let list in data['smart_lists']) {
                let overdueBadge = document.getElementById('overdueBadge' + data['smart_lists'][list]['slug']);
                let allBadge = document.getElementById('allBadge' + data['smart_lists'][list]['slug']);

                if (data['smart_lists'][list]['count_tasks']) {
                    allBadge.innerHTML = data['smart_lists'][list]['count_tasks'];
                }
                else if (allBadge) {
                    allBadge.innerHTML = '';
                }

                if (data['smart_lists'][list]['count_overdue_tasks']) {
                        overdueBadge.innerHTML = data['smart_lists'][list]['count_overdue_tasks'];
                }
                else if (overdueBadge){
                    overdueBadge.innerHTML = '';
                }
            }

            for (let list in data['personal_lists']) {
                let overdueBadge = document.getElementById('overdueBadge' + data['personal_lists'][list]['id']);
                let allBadge = document.getElementById('allBadge' + data['personal_lists'][list]['id']);

                if (data['personal_lists'][list]['count_tasks']) {
                    allBadge.innerHTML = data['personal_lists'][list]['count_tasks'];
                }
                else if (allBadge) {
                    allBadge.innerHTML = '';
                }

                if (data['personal_lists'][list]['count_overdue_tasks']) {
                        overdueBadge.innerHTML = data['personal_lists'][list]['count_overdue_tasks'];
                }
                else if (overdueBadge) {
                    overdueBadge.innerHTML = '';
                }
            }
        }
    })
}
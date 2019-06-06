function archiveTask(self) {
    let taskToArchiveId = self.parentNode.parentNode.id;
    let data = {
        'task_to_archive_id': taskToArchiveId,
    };


    $.ajax({
        type: 'POST',
        url: 'archive_task',
        dataType: 'json',
        data: data,
        success:function(data){
            $.each(data['tasks'], function (index) {
                let li = document.getElementById(taskToArchiveId);
                li.className += ' fadeOut';
            })
        }
    })
}
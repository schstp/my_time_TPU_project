let newTaskInputElement = $('#newTaskInput');
let starredChechbox = $('#starredcheck');
let markTask = document.getElementById('taskImp');
let img = markTask.firstChild;
markTask.onclick = function (e) {
    e.preventDefault();
    alert(img)
    if (!starredChechbox.is(':checked')) {
        img.src = '/static/my_time/img/starred.png';
        starredChechbox.prop('checked', true);
        newTaskInputElement.focus();
    }
    else {
        img.src = '/static/my_time/img/notstarred.png';
        starredChechbox.prop('checked', false);
        newTaskInputElement.focus();
    }
};
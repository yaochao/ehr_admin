var button = null;
$('#tableEditor').on('show.bs.modal', function (event) {
    button = $(event.relatedTarget); // Button that triggered the modal
    let tab_name = button.data('tab_name');
    let tab_buzz = button.data('tab_buzz');
    let tab_type = button.data('tab_type');
    let tab_status = button.data('tab_status');
    let tab_comment = button.data('tab_comment');
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.var
    modal = $(this);
    modal.find('.modal-title').text('编辑: ' + tab_name);
    modal.find('#tab_name').val(tab_name);
    modal.find('#tab_buzz').val(tab_buzz);
    modal.find('#tab_type').val(tab_type);
    modal.find('#tab_status').val(tab_status);
    modal.find('#tab_comment').val(tab_comment);
});

function updateUITable() {
    let tab_name = $('#tab_name');
    let tab_buzz = $('#tab_buzz');
    let tab_type = $('#tab_type');
    let tab_status = $('#tab_status');
    let tab_comment = $('#tab_comment');
    let tds = button.parent().parent().children();

    $(tds[0]).find('a').text(tab_name.val()).attr('href', 'table/' + tab_name.val());
    $(tds[1]).text(parseInt($(tds[1]).text()) + 1);
    $(tds[2]).text(tab_buzz.val());
    $(tds[3]).text(tab_type.val());
    $(tds[4]).text(tab_status.val());
    $(tds[5]).text(tab_comment.val());
}

function postData() {
    let data = {
        tab_name: $('#tab_name').val(),
        tab_buzz: $('#tab_buzz').val(),
        tab_type: $('#tab_type').val(),
        tab_status: $('#tab_status').val(),
        tab_comment: $('#tab_comment').val(),
    };
    $.ajax({
        type: 'POST',
        url: '/update_table/',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        success: function (result) {
            updateUITable();
            console.log(result);
            alert(result['msg']);
        },
        error: function (error) {
            console.log(error.responseJSON['msg']);
            alert(error.status + ' ' + error.statusText);
        },
    });
}
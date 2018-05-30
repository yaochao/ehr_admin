// function tool
function postData(data, url, callback) {
    $.ajax({
        type: 'POST',
        url: url,
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        success: function (result) {
            callback();
            console.log(result);
            alert(result['msg']);
        },
        error: function (error) {
            console.log(error.responseJSON['msg']);
            alert(error.status + ' ' + error.statusText);
        },
    });
}


// Table
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
    modal.find('.modal-title').text('编辑表: ' + tab_name);
    modal.find('#tab_name').val(tab_name);
    modal.find('#tab_buzz').val(tab_buzz);
    modal.find('#tab_type').val(tab_type);
    modal.find('#tab_status').val(tab_status);
    modal.find('#tab_comment').val(tab_comment);
});

function updateTableUI() {
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

function postTableData() {
    let data = {
        tab_name: $('#tab_name').val(),
        tab_buzz: $('#tab_buzz').val(),
        tab_type: $('#tab_type').val(),
        tab_status: $('#tab_status').val(),
        tab_comment: $('#tab_comment').val(),
    };
    let url = '/update_table/';
    postData(data, url, updateTableUI);
}


// Column
var button2 = null;
$('#columnEditor').on('show.bs.modal', function (event) {
    button2 = $(event.relatedTarget); // Button that triggered the modal
    let col_name = button2.data('col_name');
    let tab_name = button2.data('tab_name');
    let data_type = button2.data('data_type');
    let is_nullable = button2.data('is_nullable');
    let col_status = button2.data('col_status');
    let col_comment = button2.data('col_comment');

    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.var
    modal = $(this);
    modal.find('.modal-title').text('编辑字段: ' + col_name);
    modal.find('#col_name').val(col_name);
    modal.find('#tab_name').val(tab_name);
    modal.find('#data_type').val(data_type);
    modal.find('#is_nullable').val(is_nullable);
    modal.find('#col_status').val(col_status);
    modal.find('#col_comment').val(col_comment);
});

function updateColumnUI() {
    let col_name = $('#col_name');
    let tab_name = $('#tab_name');
    let data_type = $('#data_type');
    let is_nullable = $('#is_nullable');
    let col_status = $('#col_status');
    let col_comment = $('#col_comment');
    let tds = button2.parent().parent().children();

    $(tds[0]).text(col_name.val());
    $(tds[1]).text(tab_name.val());
    $(tds[2]).text(parseInt($(tds[2]).text()) + 1);
    $(tds[3]).text(data_type.val());
    $(tds[4]).text(is_nullable.val());
    $(tds[5]).text(col_status.val());
    $(tds[6]).text(col_comment.val());
}

function postColumnData() {
    let data = {
        col_name: $('#col_name').val(),
        tab_name: $('#tab_name').val(),
        data_type: $('#data_type').val(),
        is_nullable: $('#is_nullable').val(),
        col_status: $('#col_status').val(),
        col_comment: $('#col_comment').val(),
    };
    let url = '/update_column/';
    postData(data, url, updateColumnUI);
}
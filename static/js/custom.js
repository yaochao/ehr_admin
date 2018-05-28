$('#tableEditor').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var tab_name = button.data('tab_name');
    var tab_buzz = button.data('tab_buzz');
    var tab_type = button.data('tab_type');
    var tab_status = button.data('tab_status');
    var tab_comment = button.data('tab_comment');
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.var
    modal = $(this);
    modal.find('.modal-title').text('编辑: '+tab_name);
    modal.find('#tab_name').val(tab_name);
    modal.find('#tab_buzz').val(tab_buzz);
    modal.find('#tab_type').val(tab_type);
    modal.find('#tab_status').val(tab_status);
    modal.find('#tab_comment').val(tab_comment);
});
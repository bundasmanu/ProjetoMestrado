/*ref: https://stackoverflow.com/questions/22636819/confirm-deletion-using-bootstrap-3-modal-box*/
/*ref: https://stackoverflow.com/questions/17333130/how-to-pass-value-to-a-js-file*/

/*
$(confirmElement).on('click', function(e){
    confirmDialog(message, function(){
        //My code to delete
        console.log("deleted!");
    });
});
*/

function confirmDialog(message){
    var fClose = function(){
        modal.modal("hide");
    };
    var modal = $("#confirmModal");
    modal.modal('show');
    $("#confirmMessage").empty().append(message);
    $("#confirmOk").unbind().one('click', applyLogicDeleteDataset()).one('click', fClose);
    $("#confirmCancel").unbind().one("click", fClose);
}

function applyLogicDeleteDataset(){

}
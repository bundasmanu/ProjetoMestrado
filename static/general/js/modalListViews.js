function warningDialog(message){
    var fClose = function(){
        modal.modal("hide");
    };
    var modal = $("#warningModal").modal();
    modal.modal('show');
    $("#warningMessage").empty().append(message);
    $("#warningOk").unbind().one('click', fClose);
}

/*modal logic */
var modal = $("#confirmModal");

function confirmDialogDelete(message){ /*Put specific message on dialog*/

    modal.modal('show');
    $("#confirmMessage").empty().append(message);
}

var fClose = function(){ /*close modal */
    modal.modal("hide");
};

$("#confirmCancel").one().click(function () { /*action of cancel button*/
    modal.modal("hide");
});
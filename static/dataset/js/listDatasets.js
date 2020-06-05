/*ref pass variable to javascript file: https://stackoverflow.com/questions/28516101/django-how-to-pass-template-variable-to-javascript-onclick-routine*/
/*logic of display only datasets that are submitted by logged user*/
/*I need to check for each row, if a dataset was submitted by logged user, if not i need to make is display = none*/
/*Another way to solve this is to use AJAX, but i think the first way is better, in terms of performance (i would have to make new database request and render page, etc)*/

/*get token to permit to make AJAX post requests*/
var csrftoken = Cookies.get('csrftoken'); /*uses jquery library defined in listDatasets.html, and stored in dependencies js folder*/

/*ajax check if token is needed, for example in a POST request it is necessary to add the token*/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*AJAX setup*/
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('.inlineCheckBoxLabelFilter').one().click(function(){

    var ffff = document.getElementsByClassName('inlineCheckBoxLabelFilter');
    var $check_content = document.getElementsByClassName('inlineCheckBoxLabelFilter')[0].getElementsByTagName("input")[0].checked;
    var table = document.getElementById('tabelaDatasets'); /*get table*/

    if ($check_content === true){ /*if checkbox is clicked to check --> event (False (unchecked) --> True (check)) --> i need to hid datasets that aren't not submitted by logged user*/

        for (let row of table.rows){ /*fill all table rows, except first one (thead row)*/
            var k = row.cells[0].innerText;
            if (row.cells[0].innerText === ''){
                row.style.display = 'none';
            }
        }
    }
    else{
        for (let row of table.rows){ /*fill all table rows, except first one (thead row)*/
            if (row.style.display === 'none'){
                row.style.display = '';
            }
        }
    }
});

/*table variable*/
var table = document.getElementById('tabelaDatasets');

/*allow the selection of a single line at a time*/
var rows_check_boxes = document.querySelectorAll('.inlineCheckBoxLabelFilter2');

rows_check_boxes.forEach(function(input){
   input.addEventListener('click', function (event) {
       check_exists_checkboxes_actived(input); /*clean all actived checkboxes*/
       event.stopPropagation();
   });
});

function check_exists_checkboxes_actived(element){ /*clean of activated checkboxes*/

    for (var i = 0; i <rows_check_boxes.length; i++){
        if (rows_check_boxes[i] !== element) {
            rows_check_boxes[i].getElementsByTagName("input")[0].checked = false;
        }
    }
}

/*modals usage for CRUD operations, edit and delete dataset's*/

$('.linkApagaFiltro').click(function() { /*click class of a href delete button*/
    exist_one_checkbox_activated = canUserProcessOperation(); /*check if exists a checkbox activated (can only exist one at a time, events have already been defined to respond to this)*/
    if (exist_one_checkbox_activated === false){
        warningDialog('Tem de seleccionar um dataset primeiro');
    }
    else{
        confirmDialogDelete('Pretende mesmo apagar?');
    }

});

$('.linkAlteraFiltro').click(function() { /*click class of a href edit button*/

    exist_one_checkbox_activated = canUserProcessOperation(); /*check if exists a checkbox activated (can only exist one at a time, events have already been defined to respond to this)*/
    if (exist_one_checkbox_activated === false){ /*if doesn't exists, then i need to create a modal that displays a warning to user*/
        warningDialog('Tem de seleccionar um dataset primeiro');
    }
});

function canUserProcessOperation() { /*this function checks whether the user can edit or change a dataset. That is, it checks if a user has selected a dataset, if he can go ahead, if not, an alert message appears */

    for (let i=0; i< rows_check_boxes.length; i++){ /*fill all rows*/
        var input = rows_check_boxes[i].getElementsByTagName("input")[0]; /*get input of row*/
        if (input !== 'undefined') { /*check if input exists (precaution)*/
            if (input.checked === true) { /*check if checkbox is checked*/
                return true; /*if exists one checkbox activated, then returns --> user can make alterations*/
            }
        }
    }
    return false;
}

/*modal logic */
var modal = $("#confirmModal");

function confirmDialogDelete(message){

    modal.modal('show');
    $("#confirmMessage").empty().append(message);
}

var fClose = function(){
    modal.modal("hide");
};

$("#confirmOk").one().click(function () {
    applyLogicDeleteDataset();
});

$("#confirmCancel").one().click(function () {
    modal.modal("hide");
});

function warningDialog(message){
    var fClose = function(){
        modal.modal("hide");
    };
    var modal = $("#warningModal").modal();
    modal.modal('show');
    $("#warningMessage").empty().append(message);
    $("#warningOk").unbind().one('click', fClose);
}

function applyLogicDeleteDataset(){

    var index_selected_dataset = getSelectedOptionToEdit(); /*id to delete from database*/
    if (index_selected_dataset !== -1) { /*if return numeric index*/
        var link_by_id = getLinkOptionByID(1, index_selected_dataset);

        /*AJAX call*/
        $.ajax({
            type: 'POST',
            url: link_by_id,
            success: function (res) {
                window.location.reload(true);
            },
            error: function (res) {
                alert('Erro');
            }
        });
    }
    else{ /*non numeric index returned (it's only a safety way, but never enter here*/
        var modal = $("#confirmModal");
        modal.modal("hide");
    }
}

function getSelectedOptionToEdit(){ /*this function get's the id of dataset to edit (change or delete)*/

    var index = -1;
    var counter_user_datasets = 0; /*all user dataset's counter (to control index of rows check boxes) --> first tr doesn't matter (thead)*/

    for (var i=1; i<table.rows.length; i++){
        var info = table.rows[i].cells[0].innerText;
        if (table.rows[i].cells[0].innerText !== ""){ /*if exist content*/
            if (rows_check_boxes[counter_user_datasets].getElementsByTagName("input")[0].checked === true){ /*if checkbox is checked*/
                id = table.rows[i].cells[1].innerText;
                return i-1; /*because first row doesn't matter, and i doesn't start in 0 but in 1, i need to subtract 1 element to start in 0*/
            }
        counter_user_datasets = counter_user_datasets + 1;
        }
    }

    return index;
}

function getLinkOptionByID(option, index){ /*this function presents the logic to get link of clicked dataset --> option parameter 0: edit and 1:delete*/

    if (option === 0){ /*edit*/

    }
    else{ /*delete*/
        var td_element_with_url_datasetID_delete = document.getElementsByClassName("deleteLinkDatasetById")[index];
        var link_dataset_delete_id = td_element_with_url_datasetID_delete.getElementsByTagName("a")[0];
        return link_dataset_delete_id.getAttribute("href");
    }

}
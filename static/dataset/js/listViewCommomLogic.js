
/*---------------------------VARIABLES-------------------------------------*/
var navBarPrincipal = document.getElementById("navigationGenericBar").getElementsByTagName("a");
var navBarPrincipalArray = Array.from(navBarPrincipal); /*conversion to Array*/

var userToolsBar = document.getElementById("user-tools").getElementsByTagName("a");
var userToolsBarArray = Array.from(userToolsBar);

var rows_check_boxes = document.querySelectorAll('.inlineCheckBoxLabelFilter2');

/*------------------LOGIC COOKIES REDIRECTION (SET AND DELETE)----------------------------------*/
/*preserve checked box option when user uses pagination*/
$("#differentPage, #boxpreviousSymbol, #boxNextSymbol").click(function () {
    var is_checked_inline_checkbox = document.getElementsByClassName('inlineCheckBoxLabelFilter')[0].getElementsByTagName("input")[0].checked;
    if (is_checked_inline_checkbox === true){
        setCookie("inlineCheckBox", "true"); /*set inline cookie to true*/
    }
    else{
        setCookie("inlineCheckBox", "false"); /* set cookie to false*/
    }

    var index_checkbox_checked = getSelectedOptionToEdit();

    if (index_checkbox_checked !== -1){
        /*get links of selected dataset*/
        var link_edit = getLinkOptionByID(0, index_checkbox_checked);
        var link_delete = getLinkOptionByID(1, index_checkbox_checked);

        /*set links of selected dataset in cookies*/
        setCookie("link_edit", link_edit);
        setCookie("link_delete", link_delete);
    }

});

/*listener logic when happens a refresh*/
document.addEventListener('DOMContentLoaded', function() {
    var is_inline_checkbox_checked = getCookie("inlineCheckBox");
    if (is_inline_checkbox_checked === "true"){
        document.getElementsByClassName('inlineCheckBoxLabelFilter')[0].click(); /*simule click*/
    }

    /*apply check between pages, if exists*/
    /*check if links exists in this page*/
    for (var i=0; i< table.rows.length; i++){
        var td_element_edit = document.getElementsByClassName("changeLinkDatasetById")[i];
        var td_element_delete = document.getElementsByClassName("deleteLinkDatasetById")[i];
        if (td_element_edit !== undefined && td_element_delete !== undefined){
            var td_element_edit_link = td_element_edit.getElementsByTagName("a")[0].getAttribute("href");
            var td_element_delete_link = td_element_delete.getElementsByTagName("a")[0].getAttribute("href");
            var x = getCookie("link_edit");
            var y = getCookie("link_delete");
            if (td_element_edit_link === x && td_element_delete_link === y){
                /*simule click on rows_check_boxes option correspondent to links*/
                var div_checkbox_to_check = table.rows[i+1].cells[0].getElementsByClassName("inlineCheckBoxLabelFilter2")[0];
                div_checkbox_to_check.getElementsByTagName("input")[0].checked = true;
            }
        }
    }

}, false);

/*listeners to delete cookies when user clicks in other page contents*/
navBarPrincipalArray.forEach(function (input) {
    input.addEventListener('click', function (event) {
        resetPageOptionsWhenUsersJumpsOutsideThisPage();
        deleteAllCookies();
    })
});

userToolsBarArray.forEach(function (input) {
    input.addEventListener('click', function (event) {
        resetPageOptionsWhenUsersJumpsOutsideThisPage();
        deleteAllCookies();
    })
});

function resetPageOptionsWhenUsersJumpsOutsideThisPage(){

    /*uncheck filter checkbox if it's already checked*/
    var check_content = document.getElementsByClassName('inlineCheckBoxLabelFilter')[0].getElementsByTagName("input")[0].checked;
    if (check_content === true){
        document.getElementsByClassName('inlineCheckBoxLabelFilter')[0].click(); /*simule click*/
    }

    /*if exists a checkbox selected, then i need to uncheck this checkbox
    *I just need to be careful with checkbox on the same page, on other pages in the load does automatic reset, ie I just need to worry about checking the page where I am*/
    var index_selected_checkbox = getSelectedOptionToEdit();

    if (index_selected_checkbox !== -1){
        var div_checkbox_to_check = table.rows[index_selected_checkbox+1].cells[0].getElementsByClassName("inlineCheckBoxLabelFilter2")[0]; /* +1 because initial tr*/
        div_checkbox_to_check.getElementsByTagName("input")[0].checked = false;
    }

}

/*-------------------------COMMOM FUNCTIONS--------------------------------------------------------------*/
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

    var td_element_with_url_datasetID = undefined;
    if (option === 0){ /*edit*/
        td_element_with_url_datasetID = document.getElementsByClassName("changeLinkDatasetById")[index];
    }
    else{ /*delete*/
        td_element_with_url_datasetID = document.getElementsByClassName("deleteLinkDatasetById")[index];
    }
    var link_dataset_delete_id = td_element_with_url_datasetID.getElementsByTagName("a")[0];
    return link_dataset_delete_id.getAttribute("href");
}

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

/*FOR EACH EVENT CHECKBOXES CLICK'S*/
rows_check_boxes.forEach(function(input){
   input.addEventListener('click', function (event) {
       check_exists_checkboxes_actived(input); /*clean all actived checkboxes*/

       /*check if exist an option checked*/
       var index_checkbox_checked = getSelectedOptionToEdit();

       if (index_checkbox_checked !== -1){ /*if exists i need to create cookies, with links to edit and delete checked option*/
           if (getCookie("link_edit") === "" || getCookie("link_delete") === ""){
               var link_edit = getLinkOptionByID(0, index_checkbox_checked);
               var link_delete = getLinkOptionByID(1, index_checkbox_checked);

               /*set links of selected dataset in cookies*/
               setCookie("link_edit", link_edit);
               setCookie("link_delete", link_delete);
           }
       }

   });
});

function check_exists_checkboxes_actived(element){ /*clean of activated checkboxes*/

    for (var i = 0; i <rows_check_boxes.length; i++){
        if (rows_check_boxes[i] !== element) {
            rows_check_boxes[i].getElementsByTagName("input")[0].checked = false;
        }
    }
}

var rows_delete_table = []; /*html rows elements, that doesn't are created by users, and are "unchecked"*/
var position_delete_rows = []; /*position of rows elements "deleted", in order to put them in table after disable "Submitted by me" option, in his correct position*/

$('.inlineCheckBoxLabelFilter').one().click(function(){ /*extend and coolapse only datasets or models submitted by logged user*/

    var ffff = document.getElementsByClassName('inlineCheckBoxLabelFilter');
    var $check_content = document.getElementsByClassName('inlineCheckBoxLabelFilter')[0].getElementsByTagName("input")[0].checked;

    if ($check_content === true){ /*if checkbox is clicked to check --> event (False (unchecked) --> True (check)) --> i need to hid datasets that aren't not submitted by logged user*/

        var counter = -1; /*because first tr doesn't matter*/
        for (let row of table.rows){ /*fill all table rows, except first one (thead row)*/
            var k = row.cells[0].innerText;
            if (row.cells[0].innerText === ''){ /*doesn't have checkbox, and it's not submitted by logged user*/
                /**row.style.display = 'none';**/
                rows_delete_table.push(row); /*put row element on array*/
                position_delete_rows.push(counter); /*put his position on table on array*/
            }
            counter = counter + 1;
        }
        /*delete datasets/models that are not submitted by looged user*/
        for (var i=0; i<rows_delete_table.length; i++){
            rows_delete_table[i].parentNode.removeChild(rows_delete_table[i]); /*remove child from parent*/
        }
    }
    else{
        var tbody = document.getElementsByTagName("tbody")[0];
        for (var i=0; i<rows_delete_table.length; i++){
            tbody.insertBefore(rows_delete_table[i], tbody.children[position_delete_rows[i]]); /*tbody is parent of table rows, and insert in his correct position*/
        }
        rows_delete_table = []; /*reset array*/
        position_delete_rows = [] /*reset array*/
    }
});
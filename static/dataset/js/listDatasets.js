/*ref pass variable to javascript file: https://stackoverflow.com/questions/28516101/django-how-to-pass-template-variable-to-javascript-onclick-routine*/
/*logic of display only datasets that are submitted by logged user*/
/*I need to check for each row, if a dataset was submitted by logged user, if not i need to make is display = none*/
/*Another way to solve this is to use AJAX, but i think the first way is better, in terms of performance (i would have to make new database request and render page, etc)*/

/*modal logic */
$("#confirmOk").one().click(function () {
    applyLogicDeleteDataset();
});

function applyLogicDeleteDataset(){

    /*check pagination*/
    var exists_pagination_before = document.getElementById("pagination"); /*check if exists pagination before AJAX call*/

    /*get delete url*/
    var selected_delete_link = getCookie("link_delete");

    /*AJAX call*/
    $.ajax({
        type: 'POST',
        url: selected_delete_link,
        success: function (res) {

            if (exists_pagination_before !== null){
                window.location.href = '/dataset/list';
            }
            else{ /*no pagination before delete, and i don't have preocupations here, i only need to reload page*/
                window.location.reload(true);
            }
            deleteAllCookies(); /*delete cookies*/
        }
    });

}

/*listener logic when happens a refresh*/
document.addEventListener('DOMContentLoaded', function() {
    var is_inline_checkbox_checked = getCookie("inlineCheckBox");

    if (localStorage.entrou === "0"){ /*if user doesnt redirect clicking in pagination*/
        resetPageOptionsWhenUsersJumpsOutsideThisPage();
        deleteAllCookies();
    }

    else{ /*if the user has clicked on the pagination*/
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
    }

    /*reset variable that controls the correct flux of redirect's*/
    localStorage.entrou = 0;

}, false);

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
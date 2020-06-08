/*ref pass variable to javascript file: https://stackoverflow.com/questions/28516101/django-how-to-pass-template-variable-to-javascript-onclick-routine*/
/*logic of display only datasets that are submitted by logged user*/
/*I need to check for each row, if a dataset was submitted by logged user, if not i need to make is display = none*/
/*Another way to solve this is to use AJAX, but i think the first way is better, in terms of performance (i would have to make new database request and render page, etc)*/

$('.linkApagaFiltro').click(function() { /*click class of a href delete button*/

    /*get delete cookie*/
    var selected_delete_link = getCookie("link_delete");

    if (selected_delete_link !== '') {
        confirmDialogDelete('Pretende mesmo apagar?');
    }
    else{
        warningDialog('Tem de seleccionar um dataset primeiro');
    }

});

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

/*logic edit dataset*/
$('.linkAlteraFiltro').click(function() { /*click class of a href edit button*/

    /*get cookies*/
    var selected_edit_link = getCookie("link_edit");

    if (selected_edit_link !== ''){

        resetPageOptionsWhenUsersJumpsOutsideThisPage();

        /*reset cookies*/
        deleteAllCookies();

        /*redirect to page*/
        window.location.href = selected_edit_link;
    }
    else{
        warningDialog('Tem de seleccionar um dataset primeiro');
    }

});
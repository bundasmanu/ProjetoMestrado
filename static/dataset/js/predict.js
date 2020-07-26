
/*Onclick submit form button function, show loading and hide content of page*/
function loading_bar() {

    /*get variables*/
    var content_form = document.getElementById("ContainerPrincipal");
    var loading_div = document.getElementById("loadingBox");

    /*show loading div, and hide form*/
    content_form.style.display = 'none';
    loading_div.style.display = '';

}

/*This function represents the logic of refresh predict page, where detects with users predicts an image and show results or if it's a simple entry on predict page or a refresh without making a prediction*/
document.addEventListener('DOMContentLoaded', function() {

    var exist_results = showResults;

    if (exist_results === "true"){ /*user makes a prediction, i need to show results*/

        var resultsModal = $("#showResultsModal").modal().show();/*get Modal of Show Results page*/

        if (Object.keys(pred_class_dicts).length > 4){ /*check number of classes to display in modal,
                                                        if is greater than 4, i need to increase modal position in reference to top (put modal more in middle)*/
            resultsModal.css({top: '40%'});
        }

        $("#resultsMessage").empty().append("Diagnóstico obtido:");

    }

});

/*Modal close button*/
$("#warningClose").one().click(function () { /*action of cancel button*/
    $("#showResultsModal").modal("hide");
});

/*this function allows users to hide the modal by clicking on the windows*/
$(document).click(function (e) {
    if ($(e.target).hasClass('modal-backdrop')) {
        $("#showResultsModal").modal("hide");
    }
});
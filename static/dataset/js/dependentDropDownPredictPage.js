
$("#id_dataset_dropdown").change(function () { /*id_dataset_dropdown is required id of select element*/
    var url = $("#predictOutputModelClass").attr("data-models-url");
    var datasetID = $(this).val(); /*use jquery to get value of selected option*/

    if (datasetID === '') { /*reset models option, if user clicks on Selecciona Dataset, remove models of old dataset (only appears Selecciona Modelo)*/
        var options = {'': 'Selecciona Modelo'};
        var $select_model = $("#id_models_dropdown");
        $select_model.children('option:not(:first)').remove();
    }
    else {
        $.ajax({
            url: url,
            data: {
                'id_model': datasetID
            },
            success: function (data) {
                $("#id_models_dropdown").html(data);
            }
        });
    }
});
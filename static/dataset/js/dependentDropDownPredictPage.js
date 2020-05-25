
$("#id_dataset_dropdown").change(function () {
    var url = $("#predictOutputModelClass").attr("data-models-url");
    var datasetID = $(this).val();

    if (datasetID === '') { /*check empty dataset --> Selecciona Modelo option*/
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
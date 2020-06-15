
/*slick options*/
$(document).ready(function(){
    $('#carousels').slick({
        autoplaySpeed: 2000,
        autoplay: true,
        infinite: true,
        slidesToShow: 1,
        arrows: false,
        dots: true,
        fade: true,
    });
});

/*refresh page event, to get history to display on slideshow*/
document.addEventListener('DOMContentLoaded', function() {

    /*make ajax call, to get most used dataset's by logged user (3), most used datasets (3) and most used models (3), that are displayed on showHistoryDetails page*/
    $.ajax({
        url: '/history/details',
        success: function (data) {

            /*put all content data on a hidden div on SlideShowEntryPage*/
            $("#exp").html(data);

            /*retrieve correspondent data to each slide in use (next steps)*/
            var all_text_exploration_classes = document.getElementsByClassName("textExploration");

            /*most used dataset's by logged user*/
            var most_used_datasets_by_logged_user = document.getElementsByClassName("datasetsMostUsedPerUser"); /*most used dataset's by logged user*/
            $(all_text_exploration_classes).eq(0).html(most_used_datasets_by_logged_user);

            /*most used dataset's by all users*/
            var most_used_datasets_by_all_users = document.getElementsByClassName("datasetsMostUsed");
            $(all_text_exploration_classes).eq(1).html(most_used_datasets_by_all_users);

            /*most used model's by all users*/
            var most_used_models_by_all_users = document.getElementsByClassName("modelsMostUsed");
            $(all_text_exploration_classes).eq(2).html(most_used_models_by_all_users);

        }
    });

});

/*slick options*/
$(document).ready(function(){
    $('#carousels').slick({
        autoplaySpeed: 2000,
        autoplay: true,
        infinite: true,
        slidesToShow: 1,
        arrows: true,
        dots: true,
    });
});

/*refresh page event, to get history to display on slideshow*/
document.addEventListener('DOMContentLoaded', function() {

    /*make ajax call, to get most used dataset's by logged user (3), most used datasets (3) and most used models (3), that are displayed on showHistoryDetails page*/
    $.ajax({
        url: '/history/details',
        success: function (data) {
            $("#exp").html(data);
            var x = document.getElementsByClassName("datasetsMostUsedPerUser");
            $("#textExploration").html(x);
        }
    });

});
function load() {
    var divs = getAboutDivs();
    divs[1].style.display = "none"; /*aboutProject div*/
    divs[2].style.display = "none"; /*aboutMethodology div*/
}
window.onload = load();

/*click to change class of clicked li, from class link to active*/
$('.link').click(function () {
    $('.active').removeClass('active');
    $(this).addClass('active');
});

/*function that defines the div (with information - contentAbout.html) that corresponds to the option selected by the user*/
$('.link .author').click(function () {
    var values = getAboutDivs();
    if (values[0].style.display === 'none'){
        values[0].style.display = 'block';
    }
    setDisplayNoneOtherDivs(defNewList(values, 0));
});

$('.link .scope').click(function () {
    var values = getAboutDivs();
    if (values[1].style.display === 'none'){
        values[1].style.display = 'block';
    }
    setDisplayNoneOtherDivs(defNewList(values, 1));
});

$('.link .methodology').click(function () {
    var values = getAboutDivs();
    if (values[2].style.display === 'none'){
        values[2].style.display = 'block';
    }
    setDisplayNoneOtherDivs(defNewList(values, 2));
});

function getAboutDivs(){
    $x = window.parent.document.getElementById("aboutMe");
    $y = window.parent.document.getElementById("aboutProject");
    $z = window.parent.document.getElementById("aboutMethodology");
    return [$x, $y, $z]
}

function setDisplayNoneOtherDivs(values){
    for(i=0; i<values.length; i++){
        if(values[i].style.display !== 'none'){
            values[i].style.display = 'none';
        }

    }
    return true;
}

function defNewList(values, value){
    var cloneArray = values.slice();
    cloneArray.splice(value,1);
    return cloneArray;
}
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
        disableAllDimensionsLists(); /*disable all lists from all models*/
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

/*functions that expand and collapse list of models dimensions optimization*/
function disableAllDimensionsLists(){ /*load function used to disable display of all lists on methodology click*/
    document.getElementById("alexDimensions").style.display = 'none';
    document.getElementById("vggDimensions").style.display = 'none';
    document.getElementById("resnetDimensions").style.display = 'none';
    document.getElementById("densenetDimensions").style.display = 'none';
}

/*logic of span icon click --> expand and collapse*/
var span_arrow_buttons = document.getElementsByClassName('arrowButton');

span_arrow_buttons[0].addEventListener('click', function () { /*alexNet ul*/

    var parent =  span_arrow_buttons[0].closest('li');
    var children_click_ul = parent.getElementsByTagName('ul')[0];/*returns list, i need this, even if it only returns one element*/
    if (children_click_ul.style.display === 'none'){ /*if is not opened, expand*/
        children_click_ul.style.display = 'block';
    }
    else{ /*if it's already opened, then i collapse the ul*/
        children_click_ul.style.display = 'none';
    }
});

span_arrow_buttons[1].addEventListener('click', function () { /*vggNet ul*/

    var parent =  span_arrow_buttons[1].closest('li');
    var children_click_ul = parent.getElementsByTagName('ul')[0];/*returns list, i need this, even if it only returns one element*/
    if (children_click_ul.style.display === 'none'){ /*if is not opened, expand*/
        children_click_ul.style.display = 'block';
    }
    else{ /*if it's already opened, then i collapse the ul*/
        children_click_ul.style.display = 'none';
    }
});

span_arrow_buttons[2].addEventListener('click', function () { /*resnet ul*/

    var parent =  span_arrow_buttons[2].closest('li');
    var children_click_ul = parent.getElementsByTagName('ul')[0];/*returns list, i need this, even if it only returns one element*/
    if (children_click_ul.style.display === 'none'){ /*if is not opened, expand*/
        children_click_ul.style.display = 'block';
    }
    else{ /*if it's already opened, then i collapse the ul*/
        children_click_ul.style.display = 'none';
    }
});

span_arrow_buttons[3].addEventListener('click', function () { /*densenet ul*/

    var parent =  span_arrow_buttons[3].closest('li');
    var children_click_ul = parent.getElementsByTagName('ul')[0];/*returns list, i need this, even if it only returns one element*/
    if (children_click_ul.style.display === 'none'){ /*if is not opened, expand*/
        children_click_ul.style.display = 'block';
    }
    else{ /*if it's already opened, then i collapse the ul*/
        children_click_ul.style.display = 'none';
    }
});
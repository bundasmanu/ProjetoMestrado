/*ref pass variable to javascript file: https://stackoverflow.com/questions/28516101/django-how-to-pass-template-variable-to-javascript-onclick-routine*/
/*logic of display only datasets that are submitted by logged user*/
/*I need to check for each row, if a dataset was submitted by logged user, if not i need to make is display = none*/
/*Another way to solve this is to use AJAX, but i think the first way is better, in terms of performance (i would have to make new database request and render page, etc)*/

$('.inlineCheckBoxLabelFilter').one().click(function(){

    var ffff = document.getElementsByClassName('inlineCheckBoxLabelFilter');
    var $check_content = document.getElementsByClassName('inlineCheckBoxLabelFilter')[0].getElementsByTagName("input")[0].checked;
    var table = document.getElementById('tabelaDatasets'); /*get table*/

    if ($check_content === true){ /*if checkbox is clicked to check --> event (False (unchecked) --> True (check)) --> i need to hid datasets that aren't not submitted by logged user*/

        for (let row of table.rows){ /*fill all table rows, except first one (thead row)*/
            var k = row.cells[0].innerText;
            if (row.cells[0].innerText === ''){
                row.style.display = 'none';
            }
        }
    }
    else{
        for (let row of table.rows){ /*fill all table rows, except first one (thead row)*/
            if (row.style.display === 'none'){
                row.style.display = '';
            }
        }
    }
});

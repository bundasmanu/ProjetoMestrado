
/*get token to permit to make AJAX post requests*/
var csrftoken = Cookies.get('csrftoken'); /*uses jquery library defined in listDatasets.html, and stored in dependencies js folder*/

/*ajax check if token is needed, for example in a POST request it is necessary to add the token*/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*AJAX setup*/
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
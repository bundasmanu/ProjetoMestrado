/*definition of cookie shared information between pagination*/
/*https://www.w3schools.com/js/js_cookies.asp*/
function setCookie(cname, cvalue) {
  document.cookie = cname + "=" + cvalue;
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function deleteAllCookies() {
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT"; /*this date is a previous date comparing to current date*/
    }
}

/*reset cookies, when user clicks in menu options*/
var navBarPrincipal = document.getElementById("navigationGenericBar");

Array.prototype.forEach.call(navBarPrincipal.getElementsByTagName("a"),child =>{
    child.addEventListener('click', function (event) {
        deleteAllCookies();
    })
});

/**
 * Created by Evdal on 17.09.2016.
 */
$(document).ready(function () {
    if(window.location.href.indexOf("utested") > -1) {
        $(".utested").addClass("current");
    }
    else if(window.location.href.indexOf("hjem") > -1) {
        $(".hjem").addClass("current");
    }
    else if(window.location.href.indexOf("blog") > -1) {
        $(".blog").addClass("current");
    }
    else if(window.location.href.indexOf("omoss") > -1) {
        $(".omoss").addClass("current");
    }
});
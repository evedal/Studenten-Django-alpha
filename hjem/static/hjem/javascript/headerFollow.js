/**
 * Created by Evdal on 03.09.2016.
 */

function yScroll(){
    var yPos = window.pageYOffset;
    if(yPos > 100 && !$('#headscroll').hasClass("headnavShow")){
        $('#headscroll').addClass("headnavShow");
    }
    else if(yPos < 100 && $('#headscroll').hasClass("headnavShow")){
        $('#headscroll').removeClass("headnavShow");
    }
}
window.addEventListener("scroll", yScroll);
/*
$(document).ready(function () {
    var height = $(document).height();
    var footer = $(".footer_container");
    $(".fullpage").css("height", height+footer.height());
});

*/
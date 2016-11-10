/**
 * Created by Evdal on 11.10.2016.
 */

$(document).ready(function () {
    function yScroll(){
        var yPos = window.pageYOffset;
        if(yPos > 190 && !$('.sidebar').hasClass("sidebarFixed")){
            $('.sidebar').addClass("sidebarFixed");
        }
        else if(yPos < 190 && $('.sidebar').hasClass("sidebarFixed")){
            $('.sidebar').removeClass("sidebarFixed");
        }
    }
    window.addEventListener("scroll", yScroll);

   $(".up-arrow").click(function () {
            var rateCount = $(this).next();
            rateCount.html(parseInt(rateCount.html()) + 1);
            $.ajax({

                url: "/utesteder/upvote/" + $(this).closest('.anmeldelse').attr("dataid"),
                type: "GET",
                success: function (data) {
                    console.log("Vote registered");
                },
                error: function () {
                    rateCount.html(rateCount.html() - 1)
                }
            })


    });
    $(".down-arrow").click(function () {
            var rateCount = $(this).prev();
            rateCount.html(rateCount.html() - 1);
            $.ajax({
                url: "/utesteder/downvote/" + $(this).closest('.anmeldelse').attr("dataid"),
                type: "GET",
                success: function (data) {
                    console.log("Vote registered");
                },
                error: function () {
                    rateCount.html(parseInt(rateCount.html()) + 1);
                }
            })

    });
    $(".addcomment_text_btn").click(function () {
        $(".article_addcomment").toggle();
        $("#id_comment").focus();

    })

});
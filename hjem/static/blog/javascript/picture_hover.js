/**
 * Created by Evdal on 18.09.2016.
 */

$(document).ready(function(){
    $(".content_picture").on({
        mouseenter: function () {
            $(".picture_text").addClass("picture_text_hover");

            $('.article_picture').addClass('article_picture_show')
        },
        mouseleave: function () {
            $('.picture_text').removeClass('picture_text_hover ');
            $('.article_picture').removeClass('article_picture_show')
        }
    });
});
/**
 * Created by Evdal on 07.10.2016.
 */
var needConfirm  = false;
window.onbeforeunload = function () {
    if(needConfirm){
        return "Du har endringer som ikke er lagret!"
    }
    return null;
};

$(document).ready(function () {

    $("#first_name_wrapper").click(function () {
        $(this).find(".profile_edit_bg").removeClass("profile_edit_bg");
        var input = $(this).find(".input");
        input.prop("readonly",false);
        var button = $(this).find("button");

        input.on("input",function () {
            needConfirm = true;
            button.text("Lagre endringer");

        });
        button.click(function () {

            if(button.text() != 'Endre') {
                needConfirm = false;
                button.prop("type","submit");
                button.click();
            }
            else{
                input.select();
            }
        })

    });
        $("#last_name_wrapper").click(function () {
        $(this).find(".profile_edit_bg").removeClass("profile_edit_bg");
        var input = $(this).find(".input");
        input.prop("readonly",false);
        var button = $(this).find("button");

        input.on("input",function () {
            needConfirm = true;
            button.text("Lagre endringer");
        });
        button.click(function () {
            if(button.text() != 'Endre') {
                needConfirm = false;
                button.prop("type","submit");
                button.click();
            }
            else{
                input.select();
            }
        })

    });
        $("#email_wrapper").click(function () {
            $(this).find(".profile_edit_bg").removeClass("profile_edit_bg");
            var input = $(this).find(".input");
            input.prop("readonly", false);
            var button = $(this).find("button");

            input.on("input", function () {
                needConfirm = true;
                button.text("Lagre endringer");
            });
            button.click(function () {
                if (button.text() != 'Endre') {
                    needConfirm = false;
                    button.prop("type", "submit");
                    button.click();
                }
                else {
                    input.select();
                }
            })
        });
    $("#password_wrapper").click(function () {
        $(this).find(".profile_edit_bg").removeClass("profile_edit_bg");
        var input = $(this).find(".input");
        input.prop("readonly",false);
        var button = $(this).find("button");
        $(".pass_hidden").css("display","initial");
        $(".label_hidden").css("display","inline-block");
        $("#old_pass_label").html("Gammelt passord:");
        button.css("display","none");
        var saveButton = $(".save_edit_button");
        saveButton.css("display","initial");
        input.select();

        saveButton.click(function () {
            if($("#password_new1").text() == $("#password_new2").text()) {
                needConfirm = false;
                button.prop("type","submit");
                button.click();
            }
            else{
                alert("Passordene må være like!");
            }
        })

    });

});
"use strict";
$(document).ready(function(){
    $('.button-1').click(function(){
        if($(this).attr('name') == 'login'){
            $('#register-box').slideUp("fast");
            if($("#login-box").css('display') == 'none'){
                $('#login-box').slideDown("slow");
                $('#login-box').css('display','inline-block');
            }
        }
        if($(this).attr('name') == 'register'){
            $('#login-box').slideUp("fast");
            if($('#register-box').css('display') == 'none'){
                $('#register-box').slideDown("slow");
                $('#register-box').css('display','inline-block');
            }
        }
    })

    $('.content-toggle').click(function(){
        if($(this).html() == 'Hide'){
            $(this).html('Show');
        }
        else {
            $(this).html('Hide');
        }
        $(this).closest('.message-box').find('.content-box').slideToggle();
    })
});
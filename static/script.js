// Styling navbar
$(window).scroll(()=>{
    if($(window).scrollTop()>100){
        $('.header').css('background-color', 'var(--blue)');
    }
    else{
        $('.header').css('background-color', 'transparent');
    }
})

// Styling card
VanillaTilt.init(document.querySelectorAll(".disease_card"), {
    max: 20,
    speed: 400
});

// For getting data from contact us page
function contact_data(){
    contact_data_ = {
        'first_name': $('input[name="firstname"]').val(),
        'last_name': $('input[name="lastname"]').val(),
        'mob_nu': $('input[name="mobnu"]').val(),
        'email': $('input[name="email"]').val(),
        'pwd' : $('input[name="password"]').val()
    }

    // Sending data
    $.ajax({ 
        url: '/contact', 
        type: 'POST', 
        data: contact_data_
    }).done((data)=>{
        console.log(data);
    })
}


// For getting data from login page
function login(){
    login_data = {
        "mob_no":$('input[name="login_user"]').val(),
        "pwd":$('input[name="login_pwd"]').val()
    }

    $.ajax({
        url:"/login",
        type:"POST",
        data:login_data,
    }).done((data)=>{
        // Means that user exists
        if (data["result"]=="True"){
            window.location.replace("/")
        }
        else{
            $('.login_incorrect').css('display','block');
        }
    })
}
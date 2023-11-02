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

    $('input').val()='';

}

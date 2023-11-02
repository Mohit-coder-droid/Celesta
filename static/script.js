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

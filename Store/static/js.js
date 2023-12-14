
// for swiper js
var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
    delay: 2500,
    disableOnInteraction: false,
    },
    pagination: {
    el: ".swiper-pagination",
    clickable: true,
    },
    navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
    },
});
// end of swiper js

var swiper = new Swiper(".mycard", {
    effect: "cards",
    grabCursor: true,
});

// for displaying and hidding mune bar on media screen
let bars = document.querySelector('.bar')
let menus = document.querySelector('.menu-link')
bars.addEventListener("click", e =>{

    if(menus.style.display === "none"){
        menus.style.display = "block";
    }
    else{
        menus.style.display = "none";
    }
})

let admin_bars = document.querySelector('.bar')
let admin_menus = document.querySelector('.leftside-manu')
bars.addEventListener("click", e =>{

    if(admin_menus.style.display === "none"){
        admin_menus.style.display = "block";
    }
    else{
        admin_menus.style.display = "none";
    }
})


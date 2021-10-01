window.addEventListener("scroll", (event) => {
    let scroll      = this.scrollY;
    var navbar      = document.getElementsByTagName("nav")[0];
    var navLinks    = document.getElementsByClassName("nav-link");
    var navLogo     = document.getElementById("nav-logo");

    if(scroll > 150){
        navbar.classList.remove("nav-gradient");
        navbar.classList.add("nav-transparent");

        for(var i = 0; i < navLinks.length; i++){
            navLinks[i].style = "background-color: black;"
            navLinks[i].classList.add("me-1");
        }

        navLogo.src = "/static/lp_assets/images/logo-black.png";

    }

    if(scroll <= 150){
        navbar.classList.add("nav-gradient");
        navbar.classList.remove("nav-transparent");

        for(var i = 0; i < navLinks.length; i++){
            navLinks[i].style = "background-color: none;"
            navLinks[i].classList.remove("me-1");
        }

        navLogo.src = "/static/lp_assets/images/logo-white.png";
    }
});
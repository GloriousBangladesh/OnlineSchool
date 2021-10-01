function replaceClass(element, class1, class2){
    element.classList.remove(class1);
    element.classList.add(class2);
}

setInterval(function(){
    var banner          = document.getElementById("banner");
    var banner_title    = document.getElementById("banner-title");
    var banner_subtitle = document.getElementById("banner-subtitle");
    
    setTimeout(function(){
        replaceClass(banner, "bg-7", "bg-6");
        banner_title.textContent = "Classroom in hand";
        banner_subtitle.textContent = "With all the features for an actual school!";
    }, 4000);

    setTimeout(function(){
        replaceClass(banner, "bg-6", "bg-1");
        banner_title.textContent = "No more app-hopping!";
        banner_subtitle.textContent = "Just one app to rule them all!"; // JUST LIKE A REAL SCHOOL BUT ON SCREEN
    }, 8000);

    setTimeout(function(){
        replaceClass(banner, "bg-1", "bg-7");
        banner_title.textContent = "Download Now";
        banner_subtitle.textContent = "The only app your institution needs!";
    }, 12000);

} ,15000);
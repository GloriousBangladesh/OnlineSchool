
/* Set the width of the side navigation to 280px */
let sidebar = document.getElementById("sidebar");
function openNav() {
  sidebar.style.display = "block";

  setTimeout(function(){
    sidebar.style.opacity = "1"
    sidebar.style.width = "280px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  },100);

  let bgElemenets = document.querySelectorAll(".bg-light");

  for(var i = 0; i < bgElemenets.length; i++){
    bgElemenets[i].classList.toggle("bg-light");
  }


}

/* Set the width of the side navigation to 0 */
function closeNav() {
  sidebar.style.opacity = "0"
  sidebar.style.width = "0px";
  document.body.style.backgroundColor = "white";

  setTimeout(function(){
    sidebar.style.display = "none";
  },300);

  let bgElemenets = document.querySelectorAll(".bg-light");

  for(var i = 0; i < bgElemenets.length; i++){
    bgElemenets[i].classList.toggle("bg-light");
  }
}

function toggleSidebar() {
  console.log(sidebar.style.width)
  if(sidebar.style.width == "0px"){
    openNav();
  }
  else{
    closeNav();
  }
}
function dropdown(e){
    let id = e.parentElement.getAttribute('aria-labelledby');
    document.getElementById(id+"Text").textContent = e.textContent;
    document.getElementById("institute-type").value = e.textContent;
}
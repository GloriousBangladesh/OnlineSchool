function dropdown(e){
    let id = e.parentElement.getAttribute('aria-labelledby');
    document.getElementById(id).textContent = e.textContent;
}
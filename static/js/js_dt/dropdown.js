function dropdown(e){
    let id = e.parentElement.getAttribute('aria-labelledby');
    document.getElementById(id).textContent = e.textContent;
}

function examClassSelect(e, id){
    let className = e.textContent;
    document.getElementById("examClassSelect").value = id;
    document.getElementById("dropdownSelectClass").textContent = className;
}

function examSubjectSelect(e, id){
    let subjectName = e.textContent;
    document.getElementById("examSubjectSelect").value = id;
    document.getElementById("dropdownSelectSubject").textContent = subjectName;
}
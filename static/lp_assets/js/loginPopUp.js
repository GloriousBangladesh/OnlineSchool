function showLoginPopup(){
    Swal.fire({
        title: '<i class="fas fa-sign-in-alt"></i> &nbsp; Login/Register',
        
        html:
          '<hr>' +
          '<span style="text-align: left">' +
          '<a href="/institute/sign-in"><button style="width: 244px;" type="button" class="btn btn-primary btn-lg m-2 button-width"><i class="fas fa-school"></i>&nbsp; Institute Login</button></a>' +
          '<a href="/teacher/sign-in"><button style="width: 244px;" type="button" class="btn btn-primary btn-lg m-2 button-width"><i class="fas fa-chalkboard-teacher"></i>&nbsp; Teacher Login</button></a>' +
          '<a href="/student/sign-in"><button style="width: 244px;" type="button" class="btn btn-primary btn-lg m-2 button-width"><i class="fas fa-user-graduate"></i>&nbsp; Student Login</button></a>' +
          '</span>'+
          '<br/>or register a an institution!',
        showCloseButton: true,
        showCancelButton: true,
        focusConfirm: false,
        confirmButtonText:
          '<a href="/institute/register"><i class="fa fa-user-plus"></i> Register!</a>',
        confirmButtonAriaLabel: 'Register!',
        cancelButtonText:
          '<i class="fa fa-clock"></i> Later',
        cancelButtonAriaLabel: 'Later'
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = "/institute/register";
      }
    });
    
}
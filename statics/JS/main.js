
document.querySelector('.menu-btn').addEventListener('click', () => {
    document.querySelector('.nav-main ul.nav-menu').classList.toggle('show');
});
/*Validacion Formulario*/

function validar() {
    var nombre, email, password, expresion;
    nombre = document.getElementById("nombre").value;
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;

    expresion = /\w+@\w+\.+[a-z]/;

    if (nombre === "" || email === "" || password === "") {
        alert("Todos los campos son obligatorios");
        return false;
    }
    else if (nombre.length >15) {
        alert("El nombre es muy largo");
        return false;
    }
    else if (email.length >30) {
        alert("El email es muy largo");
        return false;
    }
    else if (!expresion.test(correo)) {
        alert("El correo no es valido");
        return false;
    }
    else if (password.length <8) {
        alert("La contraseña debe tener al menos 8");
        return false;
    }
}

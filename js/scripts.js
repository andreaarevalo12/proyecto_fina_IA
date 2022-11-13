window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 72,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

inforUsuario = {
    usuario: {
        nombre: null,
        errorMessage: null,
        error: false
    },
    pregunta1: {
        respuesta: null,
        errorMessage: null,
        error: false
    },
    pregunta2: {
        respuesta: null,
        errorMessage: null,
        error: false
    },
    pregunta3: {
        respuesta: null,
        errorMessage: null,
        error: false
    },
    pregunta4: {
        respuesta: null,
        errorMessage: null,
        error: false
    },
    pregunta5: {
        respuesta: null,
        errorMessage: null,
        error: false
    }
}



si = ['Si', 'SI', 'SÍ', 'Sí', 'si', 'sí', 'sÍ', 'sI']
no = ['No', 'NO', 'NÓ', 'Nó', 'no', 'nó', 'nÓ', 'nO']
nums = ["num0", "num1", "num2", "num3", "num4", "num5", "num6", "num7", "num8"]


function getData() {
    inforUsuario.usuario.nombre = document.getElementById("name"),
        inforUsuario.pregunta1.respuesta = document.getElementById("pregunta1")
    inforUsuario.pregunta2.respuesta = document.getElementById("pregunta2")

    nums.forEach(num => {
        if (document.getElementById(num).checked) {
            inforUsuario.pregunta3.respuesta = document.getElementById(num)
        }
    });

    inforUsuario.pregunta4.respuesta = document.getElementById("pregunta4")
    inforUsuario.pregunta5.respuesta = document.getElementById("pregunta5")

    inforUsuario.usuario.errorMessage = document.getElementById("errorName")
    inforUsuario.pregunta1.errorMessage = document.getElementById("errorPregunta1")
    inforUsuario.pregunta2.errorMessage = document.getElementById("errorPregunta2")
    inforUsuario.pregunta3.errorMessage = document.getElementById("errorPregunta3")
    inforUsuario.pregunta4.errorMessage = document.getElementById("errorPregunta4")
    inforUsuario.pregunta5.errorMessage = document.getElementById("errorPregunta5")
}

function sistemasDeReglas() {
    getData()
    validaciones()

    if (!inforUsuario.pregunta1.error && !inforUsuario.pregunta2.error && !inforUsuario.pregunta3.error && !inforUsuario.pregunta4.error && !inforUsuario.pregunta5.error) {
        alert = document.getElementById("alert")
        alert.style.display = "block";

        console.log(
            'INFORMACION USUARIO ', inforUsuario
        )

        limpiarDatos()

    }
}

function limpiarDatos() {
    inforUsuario.usuario.nombre.value = ''
    inforUsuario.pregunta1.respuesta.value = ''
    inforUsuario.pregunta2.respuesta.value = ''
    inforUsuario.pregunta4.respuesta.value = ''
    inforUsuario.pregunta5.respuesta.value = ''
}



function validaciones() {
    validarNombre()
    validarPreguntas(inforUsuario.pregunta1, inforUsuario.pregunta1.errorMessage)
    validarPreguntas(inforUsuario.pregunta2, inforUsuario.pregunta2.errorMessage)
    validarPregunta3()
    validarPreguntas(inforUsuario.pregunta4, inforUsuario.pregunta4.errorMessage)
    validarPreguntas(inforUsuario.pregunta5, inforUsuario.pregunta5.errorMessage)
}

function validarNombre() {
    if (inforUsuario.usuario.nombre.value === '' || !isNaN(inforUsuario.usuario.nombre.value)) {
        inforUsuario.usuario.errorMessage.innerHTML = `Usuario Invalido!`
        inforUsuario.usuario.error = true
    } else {
        inforUsuario.usuario.error = false
    }
}

function validarPregunta3() {
    if (inforUsuario.pregunta3.respuesta == null) {
        inforUsuario.pregunta3.errorMessage.innerHTML = `Campo requerido!`
        inforUsuario.pregunta3.error = true
        return
    } else {
        inforUsuario.pregunta3.error = false
    }
}

function validarPreguntas(pregunta, idAvisoError) {
    siFind = si.filter(function (element) {
        return element == pregunta.respuesta.value;
    });

    noFind = no.filter(function (element) {
        return element == pregunta.respuesta.value;
    });

    while (siFind.length == 0 && noFind.length == 0) {
        idAvisoError.innerHTML = `Campo requerido!`
        pregunta.error = true
        return false
    }
    pregunta.error = false
}


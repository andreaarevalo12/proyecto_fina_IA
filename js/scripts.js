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

nums = ["num0", "num1", "num2", "num3", "num4", "num5", "num6", "num7", "num8"]

var radios = $('[type="radio"]');

radios.change(function () {
    radios.not(this).prop('checked', false);
});


const sistemasDeReglas = async () => {
    getData()
    validaciones()

    if (!inforUsuario.pregunta1.error &&
        !inforUsuario.pregunta2.error &&
        !inforUsuario.pregunta3.error &&
        !inforUsuario.pregunta4.error &&
        !inforUsuario.pregunta5.error) {


        const informacionUsuarioFinal = {
            fullname: inforUsuario.usuario.nombre,
            respuesta1: inforUsuario.pregunta1.respuesta,
            respuesta2: inforUsuario.pregunta2.respuesta,
            respuesta3: inforUsuario.pregunta3.respuesta,
            respuesta4: inforUsuario.pregunta4.respuesta,
            respuesta5: inforUsuario.pregunta5.respuesta
        }

        url = 'http://127.0.0.1:5000/api/v1/sistemasDeReglas'

        var config = {
            headers: { 'Access-Control-Allow-Origin': '*' }
        }

        await axios({ method: 'POST', url: url, data: informacionUsuarioFinal, headers: config })
            .then(response => {
                alert = document.getElementById("alert")
                alert.innerHTML = response.data
                alert.style.display = "block";
            })
            .catch()
    }
}

function getData() {
    inforUsuario.usuario.nombre = document.getElementById("name").value,
        inforUsuario.pregunta1.respuesta = document.getElementById("pregunta1").value == 'Seleccione su respuesta' ? null : document.getElementById("pregunta1").value
    inforUsuario.pregunta2.respuesta = document.getElementById("pregunta2").value == 'Seleccione su respuesta' ? null : document.getElementById("pregunta2").value

    nums.forEach(num => {
        if (document.getElementById(num).checked) {
            inforUsuario.pregunta3.respuesta = document.getElementById(num).value
        }
    });
    inforUsuario.pregunta4.respuesta = document.getElementById("pregunta4").value == 'Seleccione su respuesta' ? null : document.getElementById("pregunta4").value
    inforUsuario.pregunta5.respuesta = document.getElementById("pregunta5").value == 'Seleccione su respuesta' ? null : document.getElementById("pregunta5").value


    inforUsuario.usuario.errorMessage = document.getElementById("errorName")
    inforUsuario.pregunta1.errorMessage = document.getElementById("errorPregunta1")
    inforUsuario.pregunta2.errorMessage = document.getElementById("errorPregunta2")
    inforUsuario.pregunta3.errorMessage = document.getElementById("errorPregunta3")
    inforUsuario.pregunta4.errorMessage = document.getElementById("errorPregunta4")
    inforUsuario.pregunta5.errorMessage = document.getElementById("errorPregunta5")
}


function validaciones() {
    validarNombre()
    validarPreguntaIfSelected(inforUsuario.pregunta1)
    validarPreguntaIfSelected(inforUsuario.pregunta2)
    validarPreguntaIfSelected(inforUsuario.pregunta3)
    validarPreguntaIfSelected(inforUsuario.pregunta4)
    validarPreguntaIfSelected(inforUsuario.pregunta5)
}

function validarNombre() {
    if (inforUsuario.usuario.nombre === '' || !isNaN(inforUsuario.usuario.nombre)) {
        inforUsuario.usuario.errorMessage.innerHTML = `Usuario Invalido!`
        inforUsuario.usuario.error = true
    } else {
        inforUsuario.usuario.error = false
    }
}

function validarPreguntaIfSelected(pregunta) {
    if (pregunta.respuesta == null) {
        pregunta.errorMessage.innerHTML = `Campo requerido!`
        pregunta.error = true
        return
    } else {
        pregunta.errorMessage.innerHTML = ``
        pregunta.error = false
    }
}

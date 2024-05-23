/* CARRUSEL */
const slides = document.querySelectorAll('.carruseles');
let slideActual = 0;

function carrusel() {
  slides.forEach((slide, i) => {
    if (i === slideActual) {
      slide.classList.remove('izquierda', 'derecha');
      slide.classList.add('centro');
    } else if (i < slideActual) {
        slide.classList.remove('centro', 'derecha');
        slide.classList.add('izquierda');
    } else {
        slide.classList.remove('centro', 'izquierda');
        slide.classList.add('derecha');
    }
  });
}

function siguiente() {
  slideActual = (slideActual + 1) % slides.length;
  carrusel();
}
function anterior() {
  slideActual = (slideActual - 1 + slides.length) % slides.length;
  carrusel();
}
document.getElementById('botonSiguiente').addEventListener('click', siguiente);
document.getElementById('botonAnterior').addEventListener('click', anterior);

carrusel();


/* VALIDACIÓN FORMULARIO */
var form = document.getElementById("formularioReservas, formularioContacto");
var nombre = document.getElementById("nombre");
var telefono = document.getElementById("telefono");
var dni = document.getElementById("dni");
var mensaje = document.getElementById("mensaje");
var error = document.getElementById("error");

form.addEventListener("submit", function(event){
  console.log("formulario funcionando");
  event.preventDefault();
  var mensajeError = [];
  
  if (nombre.value === null || nombre.value === ""){
    mensajeError.push("El campo nombre está vacío");
  }
  if (telefono.value === null || telefono.value === ""){
    mensajeError.push("El campo teléfono está vacío");
  }
  if (dni.value === null || dni.value === ""){
    mensajeError.push("El campo DNI está vacío");
  }  

  error.innerHTML = mensajeError.join(', <br>');
  
  if (mensajeError.length === 0) {
    // Acá se enviar el formulario si no hay errores
    // form.submit();
    console.log("Formulario enviado");
  } else {
    console.log("Errores en el formulario");
  }
});

document.addEventListener('DOMContentLoaded', () => {
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
  setInterval(siguiente, 5000); // Cambiar de diapositiva cada 5 segundos
});
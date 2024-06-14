document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.mostrarDetalles');
    buttons.forEach(button => {
    button.addEventListener('click', function() {
        const details = this.nextElementSibling;
        if (details.style.display === 'none' || details.style.display === '') {
            details.style.display = 'block';
            this.textContent = '» Ocultar detalles';
        } else {
            details.style.display = 'none';
            this.textContent = '» Ver detalles';
        }
    });
    });
});

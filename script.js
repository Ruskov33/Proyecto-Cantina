//Declaracion de constantes
const iniciarBtn = document.getElementById('iniciarBtn');
const content = document.querySelector('.content');
const salirBtn = document.getElementById('salirBtn');
const manualBtn = document.getElementById('manualBtn');
const NEXT_PAGE = 'menu.html';

//Pasar pagina con el boton INICIAR
iniciarBtn.addEventListener('click', () => {
    content.classList.add('slide-out');
    
    content.addEventListener('transitionend', () => {
        window.location.href = NEXT_PAGE;
    }, { once: true });
});

//Cerrar pagina con el boton de SALIR
salirBtn.addEventListener('click', () => {
    window.close();
    console.log('SALIR presionado');
});

//Pasar pagina con el boton de MANUAL
manualBtn.addEventListener('click', () => {
    window.location.href = 'manual.html';
    console.log('MANUAL presionado');
});

//SOLUCIÓN PARA EL BFCache
window.addEventListener('pageshow', (event) => {
    // Si la página se está cargando desde el caché (botón 'Atrás') 
    // o si el contenedor ya tiene la clase aplicada, la removemos.
    if (event.persisted || content.classList.contains('slide-out')) {
        content.classList.remove('slide-out');
    }
});

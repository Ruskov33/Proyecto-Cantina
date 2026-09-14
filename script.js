//Declaracion de constantes
const iniciarBtn = document.getElementById('iniciarBtn');
const content = document.querySelector('.content');
const salirBtn = document.getElementById('salirBtn');
const manualBtn = document.getElementById('manualBtn');
const cancelarBtn = document.getElementById('cancelar-btn');
const NEXT_PAGE = 'menu.html';
const HOME_PAGE = 'inicio.html';

//Pasar pagina con el boton INICIAR
if (iniciarBtn && content) {
    iniciarBtn.addEventListener('click', () => {
        content.classList.add('slide-out');

        content.addEventListener('transitionend', () => {
            window.location.href = NEXT_PAGE;
        }, { once: true });
    });
}

//Cerrar pagina con el boton de SALIR
if (salirBtn) {
    salirBtn.addEventListener('click', () => {
        window.close();
        console.log('SALIR presionado');
    });
}

//Pasar pagina con el boton de MANUAL
if (manualBtn) {
    manualBtn.addEventListener('click', () => {
        window.open("manual.txt", "Manual", "width=800,height=600,resizable=yes,scrollbars=yes");
        console.log('MANUAL presionado');
    });
}

//Volver a inicio.html al darle a Cancelar desde el menu
if (cancelarBtn) {
    cancelarBtn.addEventListener('click', () => {
        window.location.href = HOME_PAGE;
    });
}

//SOLUCIÓN PARA EL BFCache
window.addEventListener('pageshow', (event) => {
    if (content && (event.persisted || content.classList.contains('slide-out'))) {
        content.classList.remove('slide-out');
    }
});
function toogle_menu() {
    menu_btn = document.querySelector('menu_btn');
    menu_block = document.querySelector('.nav');

    if (menu_block.classList.contains('hidden')) {
        menu_block.classList.remove('hidden');
    }
    else {
        menu_block.classList.add('hidden');
    }
}
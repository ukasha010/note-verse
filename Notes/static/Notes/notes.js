// Function to toggle content visibility classes
let toggleContentVisibility = (element, isVisible) => {
    if (isVisible) {
        element.classList.add('content-visible');
        element.classList.remove('content-invisible');
    } else {
        element.classList.add('content-invisible');
        element.classList.remove('content-visible');
    }
};

let contentInvisible = () => {
    const iconContents = document.querySelectorAll('.icon-content');
    for (var i = 0; i < iconContents.length; i++) {
        if (!iconContents[i].classList.contains('image')) {
            toggleContentVisibility(iconContents[i], false);
        }
    }
    toggleContentVisibility(document.querySelector('.name'), false);
};

let contentVisible = () => {
    const iconContents = document.querySelectorAll('.icon-content');
    for (var i = 0; i < iconContents.length; i++) {
        if (!iconContents[i].classList.contains('image')) {
            toggleContentVisibility(iconContents[i], true);
        }
    }
    toggleContentVisibility(document.querySelector('.name'), true);
};

document.querySelector('.expand').addEventListener('click', function() {
    // Change the width of the side bar
    const sideBar = document.querySelector('.side-bar');
    const isSidebarReduced = sideBar.classList.contains('reduce');

    // Change content visibility and main section margin
    const iconContents = document.querySelectorAll('.icon-content');

    const marginLeft = document.querySelector('.main-section');
    if (isSidebarReduced) {
        contentVisible();
        marginLeft.classList.add('default-main-section');
        marginLeft.classList.remove('reduced-main-section');
    } else {
        contentInvisible();
        marginLeft.classList.add('reduced-main-section');
        marginLeft.classList.remove('default-main-section');
    }


    // Change the width of the side bar
    const searchContainer = document.querySelector('.search-bar-container');
    const expandBtn = document.querySelector('.expand');
    if (isSidebarReduced) {
        sideBar.classList.remove('reduce');
        searchContainer.style.left = '150px';
        expandBtn.classList.remove('new-position');
    } else {
        sideBar.classList.add('reduce');
        searchContainer.style.left = '40px';
        expandBtn.classList.add('new-position');
    }

    // Change the direction of the arrow
    const arrowDirection = document.querySelector('.expand i');
    if (arrowDirection.classList.contains('fa-angle-right')) {
        arrowDirection.classList.remove('fa-angle-right');
        arrowDirection.classList.add('fa-angle-left');
    } else {
        arrowDirection.classList.add('fa-angle-right');
        arrowDirection.classList.remove('fa-angle-left');
    }
});
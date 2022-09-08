const darkmodeCheckbox = document.getElementById("dm-toggle");

const toggleDarkMode = () => {
    if (darkmodeCheckbox.checked) {
        document.querySelector(".body").classList.add('dark-mode')
    } else {
        document.querySelector(".body").classList.remove('dark-mode')
    }
}

darkmodeCheckbox.addEventListener("change", () => toggleDarkMode());
window.addEventListener("load", () => toggleDarkMode());
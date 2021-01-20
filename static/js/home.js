if (screen.width > 800 && window.innerWidth > 800) {
    document.getElementsByClassName("friends")[0].style.height = "" + window.innerHeight + "px";
    document.getElementsByClassName("friends")[0].style.position = "sticky";
}
else {
    document.getElementsByClassName("friends")[0].style.height = "" + 300 + "px";
    document.getElementsByClassName("friends")[0].style.position = "static";
}

window.addEventListener("resize", () => {
    if (screen.width > 800 && window.innerWidth > 800) {
        document.getElementsByClassName("friends")[0].style.height = "" + window.innerHeight + "px";
        document.getElementsByClassName("friends")[0].style.position = "sticky";
    }
    else {
        document.getElementsByClassName("friends")[0].style.height = "" + 300 + "px";
        document.getElementsByClassName("friends")[0].style.position = "static";
    }
});
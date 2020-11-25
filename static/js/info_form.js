var form_container = document.getElementById("form-container");
console.log(window.innerHeight, " ", screen.width);
document.getElementById("body").style.backgroundSize  = "" + window.innerHeight + "px" + screen.width + "px";
form_container.style.marginTop = "" + (window.innerHeight - form_container.offsetHeight)/2 + "px";
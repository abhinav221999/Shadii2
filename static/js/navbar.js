var navitems = document.getElementsByClassName("navitems");
var special = document.getElementById("special");
var mobile = document.getElementById("mobile_view");
mobile.style.display = "none";
if(window.innerWidth > 800 && screen.width > 800){
		for(var i = 0; i < navitems.length; i++){
			navitems[i].style.display = "inline";
		}
		special.style.display = "none";
	}
	else{
		for(var i = 0; i < navitems.length; i++){
			navitems[i].style.display = "none";
		}
		special.style.display = "inline";
	}
window.addEventListener("resize", ()=>{
	if(window.innerWidth > 800 && screen.width > 800){
		for(var i = 0; i < navitems.length; i++){
			navitems[i].style.display = "inline";
		}
		special.style.display = "none";
		mobile.style.display = "none";
	}
	else{
		for(var i = 0; i < navitems.length; i++){
			navitems[i].style.display = "none";
		}
		special.style.display = "inline";
	}
});
special.addEventListener("click", () =>{
	if(mobile.style.display == "none"){
		mobile.style.display = "block";
	}
	else{
		document.getElementById("mobile_view").style.display = "none";
	}
});
console.log(window.innerWidth);

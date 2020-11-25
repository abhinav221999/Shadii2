
//centering the encloser
		var encloser = document.getElementById('Encloser');
		console.log(screen.height);
		encloser.style.marginTop = "" + (window.innerHeight - 450)/2 + "px";
		//functions to control the white element
		function first(){
			document.getElementById("inner").style.transform = "translateX(" + 500 + "px)";	
			document.getElementById("left").style.transform = "translateX(" + -500 + "px)";
			document.getElementById("right").style.transform = "translateX(" + -500 + "px)";
		}
		function second(){
			document.getElementById("inner").style.transform = "translateX(" + 0 + "px)";
			document.getElementById("left").style.transform = "translateX(" + 0 + "px)";
			document.getElementById("right").style.transform = "translateX(" + 0 + "px)";
		}
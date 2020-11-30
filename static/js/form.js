var container = document.getElementById("form_container");
var first = document.getElementById("first");
var second = document.getElementById("second");
var interest_list = [];
container.style.marginTop = "" + (window.innerHeight - container.offsetHeight)/2 +"px";
first.style.marginLeft = "" + (container.offsetWidth - first.offsetWidth)/2 + "px";
second.style.marginLeft = "" + (container.offsetWidth - second.offsetWidth)/2 +  "px";
function next_form(){
	var check = performCheck();
	if(check == 1){
		first.style.transition = "1s";
		second.style.transition = "1s";
		document.getElementById("bar").style.transition = "1s";
		document.getElementById("bar").style.transform = "translateX(0px)";
		first.style.transform = "translateX(-" + 650 + "px)";
		second.style.transform = "translateX(-" + 650 + "px)";
	}
	else{
		alert("please fill all the details");
	}
}
function previous_form(){
	document.getElementById("bar").style.transform = "translateX(-200px)";
	first.style.transform = "translateX(" + 0 + "px)";
	second.style.transform = "translateX(" + 0 + "px)";	
}

function performCheck(){
	var nodes = first.children;
	for(var i = 0; i < nodes.length - 1; i++){
		if(!nodes[i].checkValidity()){
			return 0;
		}
	}
	return 1;
}

function add_interests(){
	if(document.getElementById("interest-list").value != ""){
		var wrapper = document.createElement("SPAN");
		var element = document.createElement("SPAN");
		var button = document.createElement("SPAN");
		button.innerHTML = "<i class='fas fa-minus-circle'></i>";
		wrapper.setAttribute("class", "interestElements");
		button.setAttribute("class", "interestButton");
		var text = document.getElementById("interest-list").value;
		var textNode = document.createTextNode(text);
		element.appendChild(textNode);
		wrapper.appendChild(element);
		wrapper.appendChild(button);
		button.addEventListener("click", () => {
			button.parentElement.remove();
		});
		document.getElementById("interests").appendChild(wrapper);
		interest_list.push(document.getElementById("interest-list").value);
		console.log(interest_list);
		document.getElementById("interest-list").value = "";
	}
	
}

function submit_func(){
	var data = {};
	var inputs = document.getElementByClassName("post_inputs");
	for(var i = 0; i < inputs.length; i++){
		data["" + inputs[i].name] = inputs[i].value;
	}
	data["interest_list"] = interest_list;
	console.log(data);
 	var request = new XMLHttpRequest();
 	request.open("POST", "/info/", data);
 	request.setRequestHeader("Content-Type", "applicatoin/json");
 	//request.send(JSON.stringify(data));  configure the csrf token
}

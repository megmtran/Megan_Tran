function drag() {
	cat = document.getElementById("catRoll");
	leftbox = document.getElementById("leftBox");
	
	cat.addEventListener("dragstart",startDrag,false);
	cat.addEventListener("dragend",endDrag,false);
	
	leftbox.addEventListener("dragenter",dragEnter,false);
	leftbox.addEventListener("dragleave",dragLeave,false);
	leftbox.addEventListener("dragover",function(e){e.preventDefault()},false);
	leftbox.addEventListener("drop",drop,false);
}
function startDrag(e) {
	var pic = '<img id = "catRoll" src = "https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg">';
	e.dataTransfer.setData('Picture',pic);
}

function dragEnter(e) {
	e.preventDefault();
	leftbox.style.background = "#7b8ead";
	leftbox.style.border = "3px solid #ea3ad3";
}

function dragLeave(e) {
	e.preventDefault();
	leftbox.style.background = "white"
	leftbox.style.border = "3px solid black";
}

function drop(e) {
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e) {
	pic = e.target
	pic.style.visibility = "hidden";
}

window.addEventListener("load",drag,false);
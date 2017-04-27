function drag() {
	cat = document.getElementById("catRoll");
	leftbox = document.getElementById("leftBox");
	
	cat.addEventListener("dragstart",starDrag,false);
	
leftbox.addEventListener("dragenter",function(e)(e.preventDefault()},false);
	leftbox.addEventListener("dragover",function(e)(e.preventDefault()},false);
	leftbox.addEventListener("drop",drop,false);
}
function startDrag(e) {
	var pic = '<img id = "catRoll" src = "https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg">';
	e.datatranfer.setData('Picture',pic);
}

window.addEventListener("load",drag,false);
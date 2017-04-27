function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	window.addEventListener("mousemove",icon,false);
}

function icon(e) 
{
	var pic = new Image();
	pic.src = pic.src = "http://sheltongrp.com/wp-content/uploads/2013/09/Mushrooms.jpg";
	canvas.clearRect(0,0,700,700);
	var xPos = e.clientX;
	var yPos = e.clientY;
	canvas.drawImage(pic,xPos-100,yPos-100,200,200);
}
window.addEventListener("load",mouse,false);

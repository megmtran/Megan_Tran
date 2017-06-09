function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	window.addEventListener("mousemove",icon,false);
}

function icon(e) 
{
	var pic = new Image();
	pic.src = pic.src = "http://www.h3daily.com/wp-content/uploads/2009/08/ButtonMushroom-fb.jpg";
	canvas.clearRect(0,0,700,700);
	var xPos = e.clientX;
	var yPos = e.clientY;
	canvas.drawImage(pic,xPos-100,yPos-100,200,200);
}
window.addEventListener("load",mouse,false);

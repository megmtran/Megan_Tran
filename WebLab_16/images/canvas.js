function text()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	var pic = new Image();
	pic.src = "http://i.huffpost.com/gen/1132416/images/o-SLOTH-ON-A-RAILING-facebook.jpg";
	
	pic.addEventListener("load",function() {canvas.drawImage(pic,0,0,600,700)},false);
}
window.addEventListener("load",text,false);
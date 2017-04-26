function text()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	canvas.shadowOffsetX = 4;
	canvas.shadowOffsetY =4;
	canvas.shadowBlur = 6;
	canvas.shadowColor = "rgba(0,0,255,.8)";
	
	canvas.font = "bold 36px Tahoma";
	canvas.textAlign = "end";
	canvas.save();
	canvas.fillText("Robinette",300,100);
	
	canvas.translate(100,150);
	canvas.fillText("after translate",300,100);
	
	canvas.rotate(180 * Math.PI/180);
	canvas.fillText("after rotate",0,0);
	
	canvas.restore();
	canvas.scale(1.5,4);
	canvas.fillText("after scale",300,100);
}
window.addEventListener("load",text,false);
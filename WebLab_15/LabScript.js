function shapes ()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	canvas.beginPath();
	canvas.moveTo(208,648);
	canvas.lineTo(208,459);
	canvas.lineTo(20,459);
	canvas.lineTo(153,326);
	canvas.lineTo(20,193);
	canvas.lineTo(208,193);
	canvas.lineTo(208,5);
	canvas.lineTo(341,138);
	canvas.lineTo(474,5);
	canvas.lineTo(474,193);
	canvas.lineTo(662,193);
	canvas.lineTo(529,326);
	canvas.lineTo(662,459);
	canvas.lineTo(474,459);
	canvas.lineTo(474,648);
	canvas.lineTo(341,515);
	canvas.closePath();
	canvas.stroke();
}
window.addEventListener("load",shapes,false);
function validate() {
	var x = document.forms.input.username.value;
	var atPos = x.indexOf("@");
	var dotPos = x.lastIndexOf(".");
	if(atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
		alert("This is not a valid email address!");
	else
		alert("Success");
}

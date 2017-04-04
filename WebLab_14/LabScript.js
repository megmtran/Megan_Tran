function valUser() {
	var x = document.forms.input.username.value;
	var atPos = x.indexOf("@");
	var dotPos = x.lastIndexOf(".");
	if(atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
		var user = "f";
	else
		var user = "t";
	valPass();
}
function valPass() {
	var passL = document.forms.input.passwd.length;
	if(passL < 6)
		var pass = "f";
	else
		var pass = "t";
}
function validate() {
	valUser();	
	if(user = "t" || pass = "t")
		alert("Success");
	if(user = "f" || pass = "f")
		alert("We were unable to process your request. Please enter a valid email address and a password of at least 6 characters.");
	if(user = "f" || pass = "t")
		alert("We were unable to process your request. Please enter a valid email address.");
	if(user = "t" || pass = "f")
		alert("We were unable to process your request. Please enter a password of at least 6 characters.");
}
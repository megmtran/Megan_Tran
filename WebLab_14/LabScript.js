var x = document.forms.input.username.value;
var atPos = x.indexOf("@");
var dotPos = x.lastIndexOf(".");
var user = ""
var pass = ""

validate();

function valUser()
{
	if(atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
		user = "f";
	else
		user = "t";
}

function valPass() {
	var passL = document.forms.input.passwd.length;
	if(passL < 6)
		var pass = "f";
	else
		var pass = "t";
}

function validate() 
{
	valUser();
	valPass();
	
	if(user = "f" && pass = "f")
		alert("We were unable to process your request. Please enter a valid email address and a password of at least 6 characters.");
	else
	{
		if(user = "f")
			alert("We were unable to process your request. Please enter a valid email address.");
		if(pass = "f")
			alert("We were unable to process your request. Please enter a password of at least 6 characters.");
		else
			alert("Success!");
	}
}
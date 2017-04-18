



function valUser(u)
{
	var atPos = u.indexOf("@");
	var dotPos = u.lastIndexOf(".");
	if(atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > u.length)
		return "f";
	else
		return "t";
}

function valPass(p) {
	var passL = p.length;
	if(passL < 6)
		return "f";
	else
		return "t";
}

function validate() 
{
	var userName = document.forms.input.username.value;
	var passWord = document.forms.input.passwd.value;	
	user = valUser(userName);
	pass = valPass(passWord);


	if(user == "f" && pass == "f")
		alert("We were unable to process your request. Please enter a valid email address and a password of at least 6 characters.");
	else
	{
		if(user == "f")
			alert("We were unable to process your request. Please enter a valid email address.");
		else if(pass == "f")
			alert("We were unable to process your request. Please enter a password of at least 6 characters.");
		else
			alert("Success!");
	}
}
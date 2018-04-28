Global $Welcome, $Authentication, $Password, $Correction, $Retry

$Welcome = MsgBox(4, "Phaux", "This is Phaux, a self interacting Program. Do u want to Proceed ?")

If $Welcome = 6 Then
	$Authentication = InputBox("Authenticatiion", "Please Enter your Name")
	if $Authentication = "Taheer"  Then
		$Password = InputBox("Password", "Welcome " & $Authentication & " Please Enter Your Password Below", "", "*M")
    Else
		MsgBox(5, "Authentication", "Wrong Username or Password")
			if $Password = "ilovephaux" Then
			MsgBox(0, "Phaux", "Authentication Was Successful. " & $Authentication)
			Else
			MsgBox(5, "Authentication", "Wrong Username or Password")
			if $Correction = 4 Then
			$Retry = $Authentication

EndIf


	EndIf
	EndIf
	EndIf
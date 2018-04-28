Global $welcome, $UserName

$welcome = MsgBox(4, "Phaux", "Hi my name is Phaux, I am a self interacting Program. Do You want to Proceed ?")

if $welcome = 6 Then

	$UserName = InputBox("Phaux", "Please enter Your UserName below;", "UserName is your first name")
	if IsString($UserName) Then
		InputBox("Phaux", "Welcome " & $UserName & " Please Enter Your Password;", "", "*M")
	Else
		MsgBox(0, "Phaux", "That is not Your FirstName!!")
	EndIf

EndIf

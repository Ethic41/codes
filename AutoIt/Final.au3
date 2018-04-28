Global $Welcome, $Pass, $Name, $Ipass


$Pass = "ilovephauX"

$Welcome = MsgBox(4, "Phaux", "Hi My name is Phaux, an AI self interacting Program. Do you want to proced ? ")
if $Welcome = 6 then
	Call("Everything")
EndIf


Func Everything()

	Call("UserName")

	if $Name <> "" Then
	Call("Password")
	If $Ipass <> "" Then
	if $Ipass == $Pass Then
	MsgBox(0, "Authenticated", "Congratulations " & $Name & " You have Successfully Authenticated!!", "5")
    Else
	MsgBox(0, "Phaux", "Wrong UserName or Password!!", "5")
	Call("Everything")
	EndIf
	EndIf
	EndIf


EndFunc

Func UserName()
	$Name = InputBox("Phaux", "Please Enter your UserName(Your First name) Below; ", "", " M")
EndFunc


Func Password()
	$Ipass = InputBox("Phaux", "Welcome " & $Name & " Please enter your Password.", "", "*M")
EndFunc


Global $request

Func Phaux()
	MsgBox(4, "Phaux", "Hi my name is Phaux Are u sure u want to proceed ?")
EndFunc


$request = MsgBox(4, "Phaux", "Do u want to proceed ?")

	if $request = 6 Then
	Call("Phaux")
	EndIf



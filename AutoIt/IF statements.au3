Global $Entrance, $Confirmation

$Entrance = MsgBox(4, "Welcome", "Hi Welcome to Phaux! Do U want to Proceed ?")

If $Entrance = 6 Then
	MsgBox(0, "Phaux", "This is Phaux a program mean't specially for U!")
ElseIf $Entrance = 7 Then
	$Confirmation = MsgBox(4, "Phaux", "Are U sure u want To Quit ? ")
	If $Confirmation = 6 Then
		MsgBox(0, "Phaux", "Goodbye")
	ElseIf $Confirmation = 7 Then
		MsgBox(0, "Phaux", "This is Phaux a program mean't specially for U!")

	EndIf
	EndIf
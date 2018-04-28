Global $CPU

$CPU = @CPUArch

if $CPU = "X64" Then
	MsgBox(0, 'Test', 'it is 64')
ElseIf $CPU = 'X86' Then
	MsgBox(0, 'Test', 'it is 32')
EndIf





#RequireAdmin
#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_UseUpx=y
#AutoIt3Wrapper_Run_Au3Stripper=y
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
Run(@ScriptDir & "\IDM.exe")
AutoItSetOption('MouseCoordMode', 0)

WinWait('Internet Download Manager Installation Wizard')
WinActivate('Internet Download Manager Installation Wizard')
MouseClick('Primary', 315,338, 1, 10)

WinWait('Please read IDM license')
WinActivate('Please read IDM license')
MouseClick('Primary',315, 338, 1, 10)

WinWait('Choose Destination Location')
WinActivate('Choose Destination Location')
MouseClick('Primary', 315,338, 1, 10)

WinWait('Start Installation of Internet Download Manager')
WinActivate('Start Installation of Internet Download Manager')
MouseClick('Primary', 315, 338, 1, 10)

WinWait('Installation Complete')
WinActivate('Installation Complete')
MouseClick('Primary', 315, 338, 1, 10)

WinWait('IDM browser integration')
WinActivate('IDM browser integration')
MouseClick('Primary', 355, 134, 1, 10)

Global $CPU
$CPU = @CPUArch

if $CPU = 'X64' Then
Run(@ScriptDir & '\64bit.exe')

WinWait('SandySeedings Team')
WinActivate('SandySeedings Team')
MouseClick('Primary', 370, 370, 1, 10)

Sleep(300)
MouseClick('Primary', 370, 370, 1, 10)

Sleep(3000)
WinActivate('SandySeedings Team')
MouseClick('Primary', 190, 191, 1, 10)

Sleep(300)
MouseClick('Primary', 370, 370, 1, 10)

Else
Run(@ScriptDir & '\32bit.exe')

WinWait('SandySeedings Team')
WinActivate('SandySeedings Team')
MouseClick('Primary', 370, 370, 1, 10)

Sleep(300)
MouseClick('Primary', 370, 370, 1, 10)

Sleep(3000)
WinActivate('SandySeedings Team')
MouseClick('Primary', 190, 191, 1, 10)

Sleep(300)
MouseClick('Primary', 370, 370, 1, 10)
EndIf



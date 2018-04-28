#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Icon=Ethical_icon.ico
#AutoIt3Wrapper_Compile_Both=y
#AutoIt3Wrapper_UseX64=y
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#RequireAdmin
#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ### Form=C:\Users\Yakubu\Desktop\KODA\PowerISO.kxf
Global $Matlab = GUICreate("PowerISO Installer ---- By Ethical", 449, 223, -1, -1)
Global $Welcome = GUICtrlCreateLabel("Welcome to Power-iso installer", 48, 24, 378, 27)
GUICtrlSetFont(-1, 14, 800, 2, "Perpetua Titling MT")
Global $Button1 = GUICtrlCreateButton("Start PowerISO Installation", 120, 144, 219, 49)
GUICtrlSetFont(-1, 10, 800, 0, "Lucida Fax")
Global $Label1 = GUICtrlCreateLabel("Please Close all unnecessary Program and Plug Your PC to", 16, 64, 415, 20)
GUICtrlSetFont(-1, 10, 800, 0, "MS Sans Serif")
Global $Label2 = GUICtrlCreateLabel("an AC Power Source to Start Installation", 16, 88, 277, 20)
GUICtrlSetFont(-1, 10, 800, 0, "MS Sans Serif")
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###
Global $OSArc = @OSArch
While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		Case $Button1
			If FileExists(@ScriptDir & "\PowerISO.exe") Then
				Run(@ScriptDir & "\PowerISO.exe")
				AutoItSetOption("MouseCoordMode", 0)
				WinWait('PowerISO 4.8 Setup')
				WinActivate('PowerISO 4.8 Setup', 'Choose Install Location')
				MouseClick("Primary", 365, 365)
				WinWait('PowerISO 4.8 Setup', 'Installation Complete')
				ControlClick('PowerISO 4.8 Setup', 'Installation Complete', 'Button2')
				Winwait('PowerISO 4.8 Setup', 'File Associations')
				MouseClick('Primary', 362, 364)
				WinWait('PowerISO', 'You need reboot')
				MouseClick('Primary', 427, 133)
				Sleep(3000)

				if $OSArc = 'X64' Then
					Run('C:\Program Files (x86)\PowerISO\PowerISO.exe')
				Else
					Run('C:\Program Files\PowerISO\PowerISO.exe')
				EndIf
				AutoItSetOption("MouseCoordMode", 0)
				WinWait('PowerISO', 'Order online')
				WinActivate('PowerISO', 'Order online')
				MouseClick('Primary', 157, 390)
				WinWait('Registration')
				WinActivate('Registration')
				MouseClick('Primary', 210, 81)
				Send("Ahmed1337x")
				MouseClick('Primary', 157, 108)
				Send("SQCZA")
				MouseClick('Primary', 211, 109)
				Send("9UKW9")
				MouseClick('Primary', 267, 109)
				Send("PI3YU")
				MouseClick('Primary', 325, 108)
				Send("QTE9W")
				MouseClick('Primary', 380, 109)
				Send("77UUL")
				MouseClick('Primary', 336, 194)
				WinWait('PowerISO', 'Thank you')
				WinActivate('PowerISO', 'Thank you')
				MouseClick('Primary', 221, 135)
				WinClose('PowerISO - New Image File.daa')
				Sleep(3000)
				MsgBox(0, "Completed --- By Ethical", "Installation Completed Successfully.")
			Else
				MsgBox(0, "Error", "Installer Can't Find PowerISO.exe setup file. Please Make Sure that this Program is in thesame location with the setup file and Try again")
			EndIf

	EndSwitch
WEnd

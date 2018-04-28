#RequireAdmin
#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Icon=Ethical_icon.ico
#AutoIt3Wrapper_Compile_Both=y
#AutoIt3Wrapper_UseX64=y
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ### Form=C:\Users\Yakubu\Desktop\KODA\DirectX 11.kxf
Global $Matlab = GUICreate("DirectX 11 Installer ---- By Ethical", 449, 223, -1, -1)
Global $Welcome = GUICtrlCreateLabel("Welcome to Direct x 11 installer", 48, 24, 381, 27)
GUICtrlSetFont(-1, 14, 800, 2, "Perpetua Titling MT")
Global $Button1 = GUICtrlCreateButton("Start Direct X 11 Installation", 120, 144, 219, 49)
GUICtrlSetFont(-1, 10, 800, 0, "Lucida Fax")
Global $Label1 = GUICtrlCreateLabel("Please Close all unnecessary Program and Plug Your PC to", 16, 64, 415, 20)
GUICtrlSetFont(-1, 10, 800, 0, "MS Sans Serif")
Global $Label2 = GUICtrlCreateLabel("an AC Power Source to Start Installation", 16, 88, 277, 20)
GUICtrlSetFont(-1, 10, 800, 0, "MS Sans Serif")
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		Case $Button1
			If FileExists(@ScriptDir & "\DirectX11Setup\DXSETUP.exe") Then
				Run(@ScriptDir & '/DirectX11Setup/DXSETUP.exe')
				AutoItSetOption('MouseCoordMode', 0)

				WinWait('Installing Microsoft(R) DirectX(R)')
				WinActivate('Installing Microsoft(R) DirectX(R)')
				ControlCommand('Installing Microsoft(R) DirectX(R)', '', 'Button1', 'Check')
				ControlClick('Installing Microsoft(R) DirectX(R)', '', 'Button4')

				WinWait('Installing Microsoft(R) DirectX(R)', 'please click Next.')
				ControlClick('Installing Microsoft(R) DirectX(R)', '', 'Button4')

				WinWait('Installing Microsoft(R) DirectX(R)', 'Installation Complete')
				ControlClick('Installing Microsoft(R) DirectX(R)', '', 'Button5')
				Sleep(2000)
				MsgBox(0, "Completed --- By Ethical", "Installation Competed Successfully.")
			ElseIf FileExists(@ScriptDir & "\DXSETUP.exe") Then
				Run(@ScriptDir & '/DirectX11Setup/DXSETUP.exe')
				AutoItSetOption('MouseCoordMode', 0)

				WinWait('Installing Microsoft(R) DirectX(R)')
				WinActivate('Installing Microsoft(R) DirectX(R)')
				ControlCommand('Installing Microsoft(R) DirectX(R)', '', 'Button1', 'Check')
				ControlClick('Installing Microsoft(R) DirectX(R)', '', 'Button4')

				WinWait('Installing Microsoft(R) DirectX(R)', 'please click Next.')
				ControlClick('Installing Microsoft(R) DirectX(R)', '', 'Button4')

				WinWait('Installing Microsoft(R) DirectX(R)', 'Installation Complete')
				ControlClick('Installing Microsoft(R) DirectX(R)', '', 'Button5')
				Sleep(2000)
				MsgBox(0, "Completed --- By Ethical", "Installation Competed Successfully.")
			Else
				MsgBox(0, "Error", "Installer Can't Find DirectX 11 setup file. Please Make Sure that this Program is in thesame location with the setup file and Try again")
			EndIf



	EndSwitch
WEnd

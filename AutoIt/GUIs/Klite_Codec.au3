#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Icon=..\..\W\Ethical_icon.ico
#AutoIt3Wrapper_Compile_Both=y
#AutoIt3Wrapper_UseX64=y
#RequireAdmin
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ### Form=C:\Users\Yakubu\Desktop\KODA\Klite Codec.kxf
Global $Matlab = GUICreate("K-Lite Codec Player Installer ---- By Ethical", 449, 223, -1, -1)
Global $Welcome = GUICtrlCreateLabel("Welcome to K-lite player installer", 16, 24, 413, 27)
GUICtrlSetFont(-1, 14, 800, 2, "Perpetua Titling MT")
Global $Button1 = GUICtrlCreateButton("Start K-lite Installation", 120, 144, 219, 49)
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
			Run(@ScriptDir & '\K-lite_Player.exe')
			AutoItSetOption('MouseCoordMode', 0)

			WinWait('Setup - K-Lite Codec Pack')
			WinActivate('Setup - K-Lite Codec Pack')
			MouseClick('Primary', 376, 447)

			WinWaitActive('Setup - K-Lite Codec Pack', 'Installation Mode')
			ControlClick('Setup - K-Lite Codec Pack', '', 'TNewButton2')

			WinWaitActive('Setup - K-Lite Codec Pack', 'Installation Preferences')
			ControlClick('Setup - K-Lite Codec Pack', '', 'TNewButton2')

			WinWaitActive('Setup - K-Lite Codec Pack', 'Hardware Acceleration')
			ControlClick('Setup - K-Lite Codec Pack', '', 'TNewButton2')

			WinWaitActive('Setup - K-Lite Codec Pack', 'MPC-HC configuration')
			MouseClick('Primary', 58, 236)
			MouseClick('Primary', 36, 199)
			ControlClick('Setup - K-Lite Codec Pack', '', 'TNewButton2')

			WinWaitActive('Setup - K-Lite Codec Pack', 'Preferred language(s) for audio and subtitles')
			ControlCommand('Setup - K-Lite Codec Pack', 'Preferred language(s) for audio and subtitles', 'TCheckBox1', 'Check')
			ControlClick('Setup - K-Lite Codec Pack', '', 'TNewButton2')

			WinWaitActive('Setup - K-Lite Codec Pack', 'Audio configuration')
			ControlClick('Setup - K-Lite Codec Pack', 'Audio configuration', 'TNewButton3')

			WinWaitActive('Setup - K-Lite Codec Pack', 'Ready to Install')
			ControlClick('Setup - K-Lite Codec Pack', 'Ready to Install', 'TNewButton3')

			WinWaitActive('Setup - K-Lite Codec Pack', 'Done!')
			ControlClick('Setup - K-Lite Codec Pack', 'Done!', 'TNewButton3')
			Sleep(3000)
	EndSwitch
WEnd
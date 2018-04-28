#RequireAdmin
#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Icon=Ethical_icon.ico
#AutoIt3Wrapper_Compile_Both=y
#AutoIt3Wrapper_UseX64=y
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <ProgressConstants.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ### Form=C:\Users\Yakubu\Desktop\KODA\Matlab.kxf

Global $DriveLetter, $data, $OSVer, $OSArc
$OSArc = @OSArch
$OSVer = @OSVersion


Global $Matlab = GUICreate("NetFrameWork 3.5 Installer ---- By DMD", 449, 223, -1, -1)
Global $Welcome = GUICtrlCreateLabel("Welcome to NetFX 3.5 installer", 48, 24, 350, 27)
GUICtrlSetFont(-1, 14, 800, 2, "Perpetua Titling MT")
Global $Button1 = GUICtrlCreateButton("Start NetFX 3.5 Installation", 120, 144, 219, 49)
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
			If $OSVer = "WIN_7" Then
				MsgBox(0,"Successful", "Completed Successfully")

			ElseIf $OSVer = "WIN_81" Then
				DirCopy(@ScriptDir & "/win81", @HomeDrive & "\", 1)
				Run("cmd /c Dism /online /enable-feature /featurename:NetFx3 /All /Source:"&@HomeDrive&"\sources\sxs /LimitAccess & sleep 8")
				sleep(100)

			ElseIf $OSVer = "WIN_10" Then
				DirCopy(@ScriptDir & "/win10", @HomeDrive & "\", 1)
				Run("cmd /c Dism /online /enable-feature /featurename:NetFx3 /All /Source:"&@HomeDrive&"\sources\sxs /LimitAccess & sleep 8")
				sleep(100)

			EndIf

	EndSwitch
WEnd

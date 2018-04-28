#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Icon=..\..\W\167.ico
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#include <ButtonConstants.au3>
#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#include <Date.au3>
#include <StringConstants.au3>
#include <String.au3>
#Region ### START Koda GUI section ### Form=C:\Users\Yakubu\Desktop\KODA\KeYGEN2.kxf
Global $Form1 = GUICreate("KEYGEN --- Ethical", 327, 179, -1, -1)
Global $serial = GUICtrlCreateInput("", 72, 104, 177, 21)
Global $Label1 = GUICtrlCreateLabel("SERIAL KEY", 112, 80, 103, 24)
GUICtrlSetFont(-1, 12, 800, 0, "Perpetua Titling MT")
Global $Button1 = GUICtrlCreateButton("GENERATE KEY", 72, 144, 179, 25)
GUICtrlSetFont(-1, 9, 800, 0, "Sitka Text")
Global $year = GUICtrlCreateInput("", 72, 48, 177, 21)
Global $Label2 = GUICtrlCreateLabel("ENTER THE CURRENT YEAR", 40, 24, 243, 24)
GUICtrlSetFont(-1, 12, 800, 0, "Perpetua Titling MT")
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		Case $Button1
		Global $ctime = _NowTime(4)
		Global $chour = StringSplit($ctime, ":")
		Global $serialKey = (($chour[1] * 5) + 1000) * GUICtrlRead($year)
		GUICtrlSetData($serial, $serialKey)




	EndSwitch
WEnd

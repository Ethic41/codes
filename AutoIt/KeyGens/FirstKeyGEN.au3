#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Icon=..\..\167.ico
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#include <ButtonConstants.au3>
#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#include <StringConstants.au3>
#include <String.au3>
#Region ### START Koda GUI section ### Form=C:\Users\Yakubu\Desktop\KeyGEN.kxf
Global $KeyGEN = GUICreate("KeyGEN --- By Ethical", 362, 201, -1, -1)
Global $Name = GUICtrlCreateInput("", 80, 40, 201, 21)
Global $Label1 = GUICtrlCreateLabel("N A M E", 160, 16, 60, 22)
GUICtrlSetFont(-1, 12, 400, 0, "Algerian")
Global $Label2 = GUICtrlCreateLabel("S E R I A L", 144, 88, 79, 22)
GUICtrlSetFont(-1, 12, 400, 0, "Algerian")
Global $Serial = GUICtrlCreateInput("", 80, 112, 201, 21)
Global $Button1 = GUICtrlCreateButton("GENERATE", 80, 160, 91, 25)
GUICtrlSetFont(-1, 8, 800, 0, "MS Sans Serif")
Global $Button2 = GUICtrlCreateButton("EXIT", 192, 160, 91, 25)
GUICtrlSetFont(-1, 8, 800, 0, "MS Sans Serif")
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		Case $Button2
			Exit
		Case $Button1
			Global $nameInput = GUICtrlRead($Name)
			$nameInput = StringSplit($nameInput, "", $STR_CHRSPLIT)
			Global $firstAlph = _StringToHex($nameInput[1])
			$firstAlph = Dec($firstAlph) + 100
			$firstAlph = Hex($firstAlph, 2)
			Global $secondAlph = _StringToHex($nameInput[2])
			$secondAlph = Dec($secondAlph) + 100
			$secondAlph = Hex($secondAlph, 2)
			Global $thirdAlph = _StringToHex($nameInput[3])
			$thirdAlph = Dec($thirdAlph) + 100
			$thirdAlph = Hex($thirdAlph, 2)
			Global $fourthAlph = _StringToHex($nameInput[4])
			$fourthAlph = Dec($fourthAlph) + 100
			$fourthAlph = Hex($fourthAlph, 2)
			Global $SerialKey = $firstAlph & $secondAlph & $thirdAlph & $fourthAlph
			GUICtrlSetData($Serial, $SerialKey)

	EndSwitch
	WEnd

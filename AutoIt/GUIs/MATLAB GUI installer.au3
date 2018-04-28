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
Global $Matlab = GUICreate("MATLAB Installer ---- By DMD", 449, 223, -1, -1)
Global $Welcome = GUICtrlCreateLabel("Welcome to matlab installer", 48, 24, 350, 27)
GUICtrlSetFont(-1, 14, 800, 2, "Perpetua Titling MT")
Global $Button1 = GUICtrlCreateButton("Start MATLAB Installation", 120, 144, 219, 49)
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
			If FileExists(@ScriptDir & "\Matlab\setup.exe") Then
				Run(@ScriptDir & '\Matlab\Setup.exe')
				AutoItSetOption('MouseCoordMode', 0)

				WinWait('MathWorks Installer')
				WinActivate('MathWorks Installer')

				MouseClick('Primary', 28, 159)
				Sleep(20)

				MouseClick('Primary', 174, 395)
				Sleep(20)

				WinWait('License Agreement')
				WinActivate('License Agreement')

				MouseClick('Primary', 324, 351, 2)
				Sleep(20)

				MouseClick('Primary', 174, 395)
				Sleep(20)

				WinWait('File Installation Key')
				WinActivate('File Installation Key')

				MouseClick('Primary', 27, 81, 2)
				Sleep(20)

				MouseClick('Primary', 51, 108)
				Sleep(20)

				ControlSend('File Installation Key', '', '', '58691-35070-25550-28046-23042')
				Sleep(50)

				MouseClick('Primary', 169, 394)
				Sleep(20)

				WinWait('Folder Selection')
				WinActivate('Folder Selection')

				MouseClick('Primary', 171, 394)
				Sleep(20)

				WinWait('Product Selection')
				WinActivate('Product Selection')

				MouseClick('Primary', 172, 396)
				Sleep(20)

				WinWait('Confirmation')
				WinActivate('Confirmation')

				MouseClick('Primary', 169, 396)
				Sleep(20)

				WinWait('Product Configuration Notes')
				WinActivate('Product Configuration Notes')

				MouseClick('Primary', 172, 396)
				Sleep(20)

				WinWait('Installation Complete')
				WinActivate('Installation Complete')

				MouseClick('Primary', 172, 394)
				Sleep(20)


				FileCopy(@ScriptDir & '\Crack\', 'C:\Program Files\MATLAB\MATLAB Production Server\R2015a', 1)
				Sleep(2000)


				Run('C:\Program Files\MATLAB\MATLAB Production Server\R2015a\bin\win64\MATLAB.exe')
				AutoItSetOption('MouseCoordMode', 0)

				WinWait('MathWorks Software Activation')
				WinActivate('MathWorks Software Activation')

				MouseClick('Primary', 28, 172, 2)
				Sleep(20)

				MouseClick('Primary', 156, 395)
				Sleep(20)

				WinWait('Offline Activation')
				WinActivate('Offline Activation')

				MouseClick('Primary', 28, 80, 2)
				Sleep(20)

				MouseClick('Primary', 49, 110)
				Sleep(20)

				ControlSend('Offline Activation', '', '', @ScriptDir & '\Matlab\crack\lic_standalone.dat')
				Sleep(20)

				MouseClick('Primary', 156, 394)
				Sleep(20)

				WinWait('Activation Complete')
				WinActivate('Activation Complete')

				MouseClick('Primary', 498, 393)
				Sleep(2000)

				MsgBox(0, "Completed --- by Ethical", "Installation has Completed Successfully")
			ElseIf FileExists(@ScriptDir & "\setup.exe") Then
				Run(@ScriptDir & '\Setup.exe')
				AutoItSetOption('MouseCoordMode', 0)

				WinWait('MathWorks Installer')
				WinActivate('MathWorks Installer')

				MouseClick('Primary', 28, 159)
				Sleep(20)

				MouseClick('Primary', 174, 395)
				Sleep(20)

				WinWait('License Agreement')
				WinActivate('License Agreement')

				MouseClick('Primary', 324, 351, 2)
				Sleep(20)

				MouseClick('Primary', 174, 395)
				Sleep(20)

				WinWait('File Installation Key')
				WinActivate('File Installation Key')

				MouseClick('Primary', 27, 81, 2)
				Sleep(20)

				MouseClick('Primary', 51, 108)
				Sleep(20)

				ControlSend('File Installation Key', '', '', '58691-35070-25550-28046-23042')
				Sleep(50)

				MouseClick('Primary', 169, 394)
				Sleep(20)

				WinWait('Folder Selection')
				WinActivate('Folder Selection')

				MouseClick('Primary', 171, 394)
				Sleep(20)

				WinWait('Product Selection')
				WinActivate('Product Selection')

				MouseClick('Primary', 172, 396)
				Sleep(20)

				WinWait('Confirmation')
				WinActivate('Confirmation')

				MouseClick('Primary', 169, 396)
				Sleep(20)

				WinWait('Product Configuration Notes')
				WinActivate('Product Configuration Notes')

				MouseClick('Primary', 172, 396)
				Sleep(20)

				WinWait('Installation Complete')
				WinActivate('Installation Complete')

				MouseClick('Primary', 172, 394)
				Sleep(20)

				FileCopy(@ScriptDir & "\Matlab\crack\bin\win64\cublas64_65.dll", 'C:\Program Files\MATLAB\MATLAB Production Server\R2015a\bin\win64', 1)
				FileCopy(@ScriptDir & "\Matlab\crack\bin\win64\cufft64_65.dll", 'C:\Program Files\MATLAB\MATLAB Production Server\R2015a\bin\win64', 1)
				FileCopy(@ScriptDir & "\Matlab\crack\bin\win64\libmwservices.dll", 'C:\Program Files\MATLAB\MATLAB Production Server\R2015a\bin\win64', 1)
				FileCopy(@ScriptDir & "\Matlab\crack\bin\win64\mps_support_info_impl.dll", 'C:\Program Files\MATLAB\MATLAB Production Server\R2015a\bin\win64', 1)
				FileCopy(@ScriptDir & "\Matlab\crack\bin\win64\pst.dll", 'C:\Program Files\MATLAB\MATLAB Production Server\R2015a\bin\win64', 1)

				FileCopy(@ScriptDir & "\Matlab\crack\etc\win64\MLM.exe", 'C:\Program Files\MATLAB\MATLAB Production Server\R2015a\etc\win64', 1)

				FileCopy(@ScriptDir & "\Matlab\crack\java\jar\install.jar", 'C:\Program Files\MATLAB\MATLAB Production Server\R2015a\java\jar', 1)

				FileCopy(@ScriptDir & "\Matlab\crack\toolbox\slrt\blocks\flexray\simbus_slblk.mexw64", 'C:\Program Files\MATLAB\MATLAB Production Server\R2015a\toolbox\slrt\blocks\flexray', 1)



				Sleep(2000)


				Run('C:\Program Files\MATLAB\MATLAB Production Server\R2015a\bin\win64\MATLAB.exe')
				AutoItSetOption('MouseCoordMode', 0)

				WinWait('MathWorks Software Activation')
				WinActivate('MathWorks Software Activation')

				MouseClick('Primary', 28, 172, 2)
				Sleep(20)

				MouseClick('Primary', 156, 395)
				Sleep(20)

				WinWait('Offline Activation')
				WinActivate('Offline Activation')

				MouseClick('Primary', 28, 80, 2)
				Sleep(20)

				MouseClick('Primary', 49, 110)
				Sleep(20)

				ControlSend('Offline Activation', '', '', @ScriptDir & '\crack\lic_standalone.dat')
				Sleep(20)

				MouseClick('Primary', 156, 394)
				Sleep(20)

				WinWait('Activation Complete')
				WinActivate('Activation Complete')

				MouseClick('Primary', 498, 393)
				Sleep(2000)

				FileCreateShortcut("C:\Program Files\MATLAB\MATLAB Production Server\R2015a\bin\win64\MATLAB.exe", @DesktopDir & "\MATLAB.lnk")

				MsgBox(0, "Completed --- by Ethical", "Installation has Completed Successfully")
			Else
				MsgBox(0, "Error", "Installer Can't Find the Matlab Folder Please make sure you copied this program to your Matlab folder and Run again")
			EndIf

	EndSwitch
WEnd

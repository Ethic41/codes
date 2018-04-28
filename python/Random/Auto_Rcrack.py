import subprocess

def main():
	print('''
        #*****************::::::::::*******************#
        #         -----    Auto_Rcrack   ------        #
        #         -----    By Ethical    ------        #
        #                                              #
        #            Auto_Crack Automate               #
        #          Rainbow Table Generation            #
        #                                              #
        #*****************:::::::::::******************#
        ''')
	while True:
		try:
			go = raw_input("Go Manual 'M' or Auto 'A'")
			go = str(go).lower()
			if go == "a":
				auto()
			elif go == "m":
				manual()
			else:
				raise()
		except:
			print("Invalid input, please check your input")
	

def auto():
	print("auto called!")


def manual():
	print("manual called!")

if __name__ == "__main__":
	main()
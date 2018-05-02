#CodeName: separator.py
#Author: Dahir Muhammad Dahir
#Date: 2nd-May-2018
#About: as the name implies

import os
import argparse

thisDir = os.getcwd()

def main():
	parser = argparse.ArgumentParser(description="Separate the file lines based on parameter you specify")
	parser.add_argument("file", help="specify a input fileName")
	parser.add_argument("-p", "--parameter", help="the parameter to separate the lines by", required=True)
	parser.add_argument("-m", "--max", help="optional max[of the parameter] to split lines", default=None)
	parser.add_argument("-i", "--index", help="index of the the data to return e.g 2,5", required=True)
	parser.add_argument("-f", "--outFile", help="the file to output the result [default = separated.dmd]", default="separated.dmd")
	parser.add_argument("-n", "--newParam", help="optional new parameter to separate the result if it's multiple[default is white space]")
	args = parser.parse_args()
	separator(args.file, args.parameter, args.index, args.outFile, args.max, args.newParam)


def separator(fileName, parameter, index, outfile, max=None, newParam=None):
	strippedLines = []
	with open(fileName, "r") as f:
		lines = f.readlines()

	for line in lines:
		line = line.strip("\n")
		strippedLines.append(line)

	print(strippedLines)

	newList = []
	for line in strippedLines:
		validLine = []
		if max:
			splittedLine = line.split(parameter.strip(" "), max)
		else:
			splittedLine = line.split(parameter.strip(" "))

		print(splittedLine)

		index = index.split(",")
		print(index)
		if len(index) > 1:
			for i in index[:-1]:
				validLine.append(splittedLine[int(i)])

			if newParam:
				newLine = newParam.join(validLine)
				newList.append(newLine)

		else:
			newList.append(splittedLine[index])

	newList.sort()

	with open(outfile, "ab") as f:
		for line in newList:
			f.write(line+"\n")












if __name__ == '__main__':
	main()

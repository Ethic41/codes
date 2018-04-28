from operator import xor

inputText = raw_input("Enter text:\n")
outputText = ""
for i in inputText:
    out = chr(xor(xor(xor(ord(i), 0x55), 0x1E), 0x43))
    outputText += out

print(outputText)


def mapper(word):
	alphs = list("abcdefghijklmnopqrstuvwxyz")
	n_word = [] #new word holder
	for l in word:
		n_word.append(alphs[alphs.index(l)+2])
	print(n_word)

mapper("")
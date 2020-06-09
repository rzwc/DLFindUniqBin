# Python >= 3
# see LICENSE file for licensing information

WORDS = '/usr/share/dict/words'

X = {}

f = open(WORDS)
for word in f:
	# strip \n
	word = word[:-1]
	if not word.isalpha():
		# skip hyphenated words and other oddness
		continue
	if word.isupper():
		# skip acronyms
		continue
	# fold case
	word = word.lower()
	trigrams = [word[i:i+3] for i in range(len(word)-2)]
	for d in trigrams:
		# save freq info in case it's useful for filtering later
		if d in X:
			X[d] = X[d] + 1
		else:
			X[d] = 1
f.close()

print('# AUTOMATICALLY GENERATED -- DO NOT EDIT')
print('TRIGRAMS =', X)

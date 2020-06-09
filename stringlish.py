# for Python >= 3
# see LICENSE file for licensing information

import re
import sys
import string
import ngram

N_PRINT = 4	# minimum number of printable chars to look for

X = '0123456789abcdefghijklmnopqrstuvwxyz'

def code(s):
	rv = ''
	for i in range(len(s)-1):
		pair = s[i:i+2]
		diff = abs(ord(pair[0]) - ord(pair[1]))
		try:
			rv += X[diff]
		except IndexError:
			return '!'
	return rv

# 1st "derivative"
yawn = re.compile(r'(^.00+$) | (^00+.$) | (^11+$) | (.*000) | (.*11111) | (.*22222) | (.*33333) | (.*44444) | (.*55555) | (.*66666) | (.*77777) | (.*88888) | (.*99999)',
			re.VERBOSE|re.DOTALL)
# 2nd "derivative"
yawn2 = re.compile(r'(^.00+$) | (^00+.$) | (^11+$) | (.*000) | (.*1111) | (.*2222) | (.*3333) | (.*4444) | (.*5555) | (.*6666) | (.*7777) | (.*8888) | (.*9999)',
			re.VERBOSE|re.DOTALL)

def boring(s):
	# too short?
	if len(s) < N_PRINT:
		return True
	# no vowels?
	for ch in s:
		if ch in 'AEIOUYaeioiuy':
			break
	else:
		return True
	if yawn.match(code(s)) is not None:
		return True
	if yawn2.match(code(code(s))) is not None:
		return True
	return False

def filter_trigram(s):
	for i in range(len(s)-2):
		tri = s[i:i+3]
		if tri in ngram.TRIGRAMS:
			# ignore low-frequency trigrams
			if ngram.TRIGRAMS[tri] < 75:
				continue
			return True
	return False
	
# can't make this .+ or .* because it can capture the patterns we want
pattern = re.compile(r'( [A-Z][A-Z]+ ) | ( [a-z][a-z]+ ) | ( . )',
			re.VERBOSE|re.DOTALL)

def process(ps, label):
	L = []
	interesting = False
	ps = str(ps, 'ISO-8859-1')		# sigh
	for mo in re.finditer(pattern, ps):
		bold = False
		if mo.groups()[0] is not None:
			# uppercase alpha
			s = mo.groups()[0].lower()
			if not boring(s):
				if filter_trigram(s):
					interesting = True
					bold = True
		elif mo.groups()[1] is not None:
			# lowercase alpha
			s = mo.groups()[1].lower()
			if not boring(s):
				if filter_trigram(s):
					interesting = True
					bold = True
		else:
			# nothing to see here
			pass
		L.append( (bold, mo.group(0)) )

	if interesting:
		if label is not None:
			print('[', label, '] ', end='')
		for bold, s in L:
			if not bold:
				sys.stdout.write(s)
			else:
				for ch in s:
					# this emboldens in less (the pager)
					sys.stdout.write(ch)
					### uncomment for bold output
					#sys.stdout.write('\b')
					#sys.stdout.write(ch)
					###
		sys.stdout.write('\n')

# newlines are annoying in line-based output; remove them
printable = ''.join([ch for ch in string.printable if ch != '\n'])
# Python 3 is such a joy
printable = bytes(printable, 'ISO-8859-1')

def newfile(file):
	# this is broken out so we can retain seen's contents across
	# multiple obfuscation candidates (when called by obfus engine)
	global seen
	seen = {}

def filter_printable(s, label=None):
	start = 0
	isprintable = True
	s += b'\xff'			# append unprintable sentinel
	for i in range(len(s)):
		if not isprintable:
			if s[i] in printable:
				start = i
				isprintable = True
		else:
			if s[i] not in printable:
				isprintable = False
				if i-start >= N_PRINT:
					# canonicalize case so we don't
					# see a string candidate in both
					# upper and lower case
					key = s[start:i].lower()
					if key not in seen:
						process(s[start:i], label)
						seen[key] = True

if __name__ == '__main__':
	for file in sys.argv[1:]:
		#print('==>', file, '<==')
		try:
			f = open(file, 'rb')
			s = f.read()
			f.close()
		except IOError as e:
			sys.stderr.write('%s: %s\n' % (file, e.strerror))
			continue
		newfile(file)
		filter_printable(s)

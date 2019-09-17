# 97 - 122

key = 'abc'
#cipher = [120,121,122]
cipher = [19,'1b',19]

def key_to_ascii(key):	
	keylen = len(key)
	key = list(key)
	akey = [0] * keylen
	for i in range(keylen):
		akey[i] = ord(key[i])
	return akey

def ascii_to_string(ascii):
	alen = len(ascii)
	string = [0] * alen
	for i in range(alen):
		string[i] = chr(ascii[i])
	return string

def xor(akey, cipher):
	keylen = len(akey)
	decoded = [0] * keylen
	for i in range(keylen):
		decoded[i] = akey[i] ^ cipher[i]
	return decoded

akey = key_to_ascii(key)
#encoded = xor(akey, cipher)
decoded = xor(akey, cipher)

string = ascii_to_string(decoded)
print string

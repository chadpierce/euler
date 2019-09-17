

def make_words(number):
		
	length = len(str(number))
	
	#ignore zeros in a hacky way
	ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
	tens = ["placeholder0", "placeholder1", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
	
	if(length > 3):
		words = "one thousand"
		return words
	
	if(length == 1):
		words = ones[number]
		return words

	elif(length == 2):
		n = str(number)
		first = int(n[0])
		second = int(n[1])
		if(first == 1): 
			words = teens[second]
		elif(first > 1):
			words = tens[first] + " " + ones[second]		
		return words
	
	elif(length == 3):
		n = str(number)
		first = int(n[0])
		second = int(n[1])
		third = int(n[2])
		
		words = ones[first] + " hundred"

		if(second == 0):
			if(third == 0): 
				return words
			words = words + " and " + ones[third]
			return words
		if(second == 1): 
			words = words + " and " + teens[third]
			return words
		elif(second > 1):
			words = words + " and " + tens[second] + " " + ones[third]
			return words


def count_letters(words):
	#need to remove spaces or you are WRONG!
	letter_count = len(words) - words.count(' ')
	return letter_count


letters = 0
for i in range(1,1001):
	letters = letters + count_letters(make_words(i))

#letters no longer looks like a real word
print(letters)

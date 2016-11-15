class pigLatinTranslator(object):
	'''
	Translate to and from Pig Latin!
	'''
	def __init__(self, word):
		self.word = word

	def __str__(self):
		return str(self.word)

	def newWord(self, new):
		self.word = new

	def engToPig(self):
		vowels = 'aeiouy'
		word = self.word.lower()

		if word[0] not in vowels:
			
			vowelsInWord = [word.index(let) for let in word if let in vowels]
			firstVowel = vowelsInWord[0]
			return word[firstVowel:] + word[:firstVowel] + 'ay'

		else:
			return word + 'way'

	def pigToEng(self):
		word = self.word.lower()

		if word[-3:] == 'way':
			return word[:-3]

		else:
			word = word[:-2]
			for index in range(0,len(word),1):
				word = word[index:] + word[:index]
				
				if isWord(word):
					return 'The english word = {}'.format(word)
			return "Not a pig latin word."

def isWord(word):
	words = open('words.txt', 'r')
	for w in words:

		if w.rstrip() == word:
			words.close()
			return True
	words.close()
	return False

def main():
	word = input("What word would you like to translate? ")
	translator = pigLatinTranslator(word)
	while True:
		print("Word to be translated = " + str(translator))
		inp = int(input("""What would you like to do?
				Translate to Pig Latin = 1
				Translate to English = 2
				Translate a different word = 3
				Quit = 4\n"""))
		if inp == 1:
			print(translator.engToPig())
		elif inp == 2:
			print(translator.pigToEng())
		elif inp == 3:
			new = input("Which word? ")
			translator.newWord(new)
		elif inp == 4:
			break
		else:
			print("Not valid input. Try again.")

if __name__ == "__main__":
	main()
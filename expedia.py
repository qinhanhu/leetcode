# https://www.geeksforgeeks.org/count-of-pairs-of-strings-whose-concatenation-forms-a-palindromic-string/
def countComplementaryPairs(stringData):
	# base: if a str A is palindrome, there is at most one character of A has odd frequence. 

	patternMap = {}
	ans = 0
	for word in stringData:
		pattern = [0] * 26

		# count frequency
		for ch in word:
			pattern[ord(ch) - ord('a')] += 1

		# convert frequency to parity
		for i, freq in enumerate(pattern):
			pattern[i] = freq % 2

		# case1: the parity of each character in strA and strB are same.
		# Their combination will be a palindrome.
		tupPattern = tuple(pattern)
		if tupPattern in patternMap:
			ans += patternMap[tupPattern]

		for i in range(26):
			newPattern = pattern[:]
			# reverse one character's parity
			if newPatternp[i] == 1:
				newPattern[i] = 0
			else:
				newPattern[i] = 1

			# case2: just one character's parity in strA and strB is different.
			tupNewPattern = tuple(newPattern)
			if tupNewPattern in patternMap:
				ans += patternMap[tupNewPattern]

		# update patternMap
		if tupPattern not in patternMap:
			patternMap[tupPattern] = 0
		patternMap[tupPattern] += 1
	return ans




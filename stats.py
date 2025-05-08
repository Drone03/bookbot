def get_num_words(text):
	return len(text.split())

def count_chars(text):
	char_count = {}
	for char in text:
		char = char.lower()
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count
def sorted_chars_list(char_count):
	def sort_on(dict):
		return dict["num"]
	chars_list = []
	for char, count in char_count.items():
		chars_list.append({"char":char,"num":count})
	chars_list.sort(reverse=True, key=sort_on)
	return chars_list

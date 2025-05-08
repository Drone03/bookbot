from stats import get_num_words, count_chars, sorted_chars_list
import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(path):
	with open(path) as f:
		contents = f.read()
	return contents

def main():
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	char_counts = count_chars(text)
	sorted_chars = sorted_chars_list(char_counts)
	print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
	for char_dict in sorted_chars:
		if char_dict["char"].isalpha():
			print(f"{char_dict['char']}: {char_dict['num']}")
	print("============= END ===============")
main()

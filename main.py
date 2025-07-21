from stats import count_words
from stats import count_char_occurrences
from stats import sort_char_occurrences

import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
def display_char_occurrences(num_words, char_occurrences, filepath):
  sorted_occurrences = sort_char_occurrences(char_occurrences)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")

  for occurrence in sorted_occurrences:
    print(f"{occurrence['char']}: {occurrence['count']}")
  
  print("============= END ===============")

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  path_to_book = sys.argv[1]
  book_text = get_book_text(path_to_book)
  num_words = count_words(book_text)
  char_occurrences = count_char_occurrences(book_text)
  # print(f"Character occurrences: {char_occurrences}")
  # print(f"{num_words} words found in the document")
  
  display_char_occurrences(num_words, char_occurrences, path_to_book)
  
main()
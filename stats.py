def count_words(text):
  return len(text.split())

def count_char_occurrences(text):
  split_text = list(text.lower())
  chars_count = {}
  chars_object_count= []
  
  for char in split_text:
    if char not in chars_count:
      chars_count[char] = 0
    chars_count[char] += 1
    
  for char in list(chars_count.keys()):
    if char.isalpha():
      chars_object_count.append({'char': char, 'count': chars_count[char]})
  
  return chars_object_count

def sort_char_occurrences(char_occurrences):
  return sorted(char_occurrences, key=lambda x: x['count'], reverse=True)
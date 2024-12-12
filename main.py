def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")

    num_words = count_words(file_contents)
    print(f"{num_words} words found in the document\n")

    num_characters = count_characters(file_contents)
    for item in num_characters:
      print(f"The '{item["character"]}' character was found {item["count"]} times")

    print("--- End report ---")

def count_words(text):
  words = text.split()
  return len(words)

def sort_on(dict):
  return dict["count"]

def count_characters(text):
  text = text.lower()
  char_count = {}

  for char in text:
    if char.isalpha():
      char_count[char] = char_count.get(char, 0) + 1

  # Convert the dictionary to a list of dictionaries
  characters = [{"character": char, "count": count} for char, count in char_count.items()]

  # Sort the list by count in descending order
  characters.sort(reverse=True, key=sort_on)

  return characters

main()
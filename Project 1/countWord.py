T = str(input())
def countWord(text):
  text = text.replace(" ", "").replace("\t", "").replace("\n", "")

  # Split the text into words.
  words = text.split()

  # Return the number of words.
  return len(words)


print(countWord(T))
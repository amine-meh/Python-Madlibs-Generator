with open("story.txt", "r") as f:
  story = f.read()

words = set()
target_word_starting = "<"
target_word_ending = ">"
start_of_word = -1

for i, char in enumerate(story):
  if char == target_word_starting:
    start_of_word = i

  if char == target_word_ending and start_of_word != -1:
    word = story[start_of_word : i+1]
    words.add(word)
    start_of_word = -1

answers = {}

for word in words:
  answer = input("Enter a word for "+ word +" :")
  answers[word] = answer

for word in words:
  story = story.replace(word, answers[word])

print(story)



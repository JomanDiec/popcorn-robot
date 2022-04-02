trivia = """288. Miscellaneous JPATS are the initials of an US domestic airline which was created (by the federal government) to perform what specific service. Transportation of prisoners

289. Geography If viewed on a globe, the longest straight line you can trace on the ocean without touching any land would connect what pair of unlikely countries with one end being almost 20,000 miles from the other? (provide basic world map image?)  Pakistan and Russia

290. Geography Point Nemo is a spot in the South Pacific so named because it has what distinction? Furthest spot from any land

291. Science, Geology Kimberlite pipes are a type of igneous rock formation that is the most common source in the mining of what mineral? Diamonds"""

questions = trivia.splitlines()

# while("" in question) :
#     question.remove("")

questions = list(filter(None, questions))

# print(question)

for triv in questions:
  trivia_question = triv.split(". ", 1)
  questions = trivia_question + questions
  questions.remove(triv)

questions = list(filter(lambda i: len(i) > 4, questions))

print(questions)

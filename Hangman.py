
def checkGuess(word, guessLetter):

  """
  check if the letter exists in the word
  :param word:
  :param guessLetter:
  :return: int[] list of index positions of letter in word
  """
  pos = []

  for i in range(len(word)):
     if word[i] == guessLetter:
         pos.append(i)
  return pos

def displayBoard(wordBoard):

  """
  shows word board on the screen
  :param wordBoard: string[] i.e ["_", "A", "_"]
  :return: None
  """

  print(" ".join(wordBoard))

def askLetter(guessedLetters):

 """
 gets a valid guess from the player
 :guessedLetters - list of letters guessed
 :return:string - a single valid letter
 """

 guess = input("Enter a single letter: ")
 return guess

def displayHangmanBoard(phaseInt):

 """
 show the current hangman board on the screen based on the given phase
 :return:None
 """

 if phaseInt == 1:
         print ("              ")
         print ("|             ")
         print ("|             ")
         print ("|             ")
         print ("|             ")
         print ("|             ")
 elif phaseInt == 2:
         print ("________      ")
         print ("|             ")
         print ("|             ")
         print ("|             ")
         print ("|             ")
         print ("|             ")
 elif phaseInt == 3:
         print ("________      ")
         print ("|      |      ")
         print ("|             ")
         print ("|             ")
         print ("|             ")
         print ("|             ")
 elif phaseInt == 4:
         print ("________      ")
         print ("|      |      ")
         print ("|      0      ")
         print ("|             ")
         print ("|             ")
         print ("|             ")
 elif phaseInt == 5:
         print ("________      ")
         print ("|      |      ")
         print ("|      0      ")
         print ("|      |      ")
         print ("|             ")
         print ("|             ")
 elif phaseInt == 6:
         print ("________      ")
         print ("|      |      ")
         print ("|      0      ")
         print ("|     /|      ")
         print ("|             ")
         print ("|             ")
 elif phaseInt == 7:
         print ("________      ")
         print ("|      |      ")
         print ("|      0      ")
         print ("|     /|\     ")
         print ("|             ")
         print ("|             ")
 elif phaseInt == 8:
         print ("________      ")
         print ("|      |      ")
         print ("|      0      ")
         print ("|     /|\     ")
         print ("|      |       ")
         print ("|             ")
 elif phaseInt == 9:
         print ("________      ")
         print ("|      |      ")
         print ("|      0      ")
         print ("|     /|\     ")
         print ("|      |      ")
         print ("|       \     ")
 elif phaseInt == 10:
         print ("________      ")
         print ("|      |      ")
         print ("|      0      ")
         print ("|     /|\     ")
         print ("|      |      ")
         print ("|     / \     ")

def updateBoard(currentBoard, letter, positions):

   """

   :param currentBoard: current board list
   :param letter: letter to add
   :param positions: list of positions to add the letter
   :return: a string list of the updated board
   """
   for i in range(len(positions)):
       currentBoard[positions[i]] = letter
   return currentBoard

def getWord():

  """
  retrieve word from text file
  :return: string
  """
  #Open source file
  sourcefile = open('words.txt','r+')
  #Read the lines of the source files
  sourcelist = sourcefile.readlines()
  #Close the source file
  sourcefile.close()

  for i in range(len(sourcelist)):
      number = (i + 1)

  from random import randint

  word = (sourcelist[(randint(0,number - 1))])
  return word

def playGame(word):

  """
  run the game
  :return: string result
  """

  # initialize hangmanBoard
  hangmanBoardInt = 0
  max_guesses = 10


  # initialize guessedLetters to empty list
  guessedLetters = []

  # initialize wordBoard
  wordBoard = ["_"] * (len(word) - 1)


  game_over = False
  won = False

  while not game_over:
      letter = askLetter(guessedLetters) # get letter from the user
      positions = checkGuess(word, letter)

      if len(positions) > 0:
          wordBoard = updateBoard(wordBoard, letter, positions)
      else:
          hangmanBoardInt += 1

      displayBoard(wordBoard)
      displayHangmanBoard(hangmanBoardInt)

      if "".join(wordBoard).lower().strip() == word.lower().strip():
          won = True
          game_over = True

      if hangmanBoardInt == max_guesses:
          game_over = True

      guessedLetters.append(letter)
      print("Guessed Letters: " + "".join(guessedLetters))

  if won:
       return "Won"
  else:
       return "Lost"

def outputResult(result):

   """
   output result to the screen
   :param result: string
   :return:
   """
   if result == "Won":
       print ("Congratulations! You have guessed the word. You win!")
   elif result == "Lost":
       print  ("Sorry, you ran out of guesses")
   else:
       print ("Error in the result")



def main():
  filename = "words.txt"
  word = getWord()
  result = playGame(word)
  outputResult(result)







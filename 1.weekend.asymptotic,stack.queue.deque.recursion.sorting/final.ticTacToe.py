"""
  +---+---+---+
  | 0 | 1 | 2 |
  +---+---+---+
  | 3 | 4 | 5 |
  +---+---+---+
  | 6 | 7 | 8 |
  +---+---+---+
Step 1: Player X, choose a number in an empty square >>> 4

(We better validate the user's inputs.
 Loop if necessary util a valid input is entered.)

  +---+---+---+
  | 0 | 1 | 2 |
  +---+---+---+
  | 3 | X | 5 |
  +---+---+---+
  | 6 | 7 | 8 |
  +---+---+---+

Step 2: Player O, choose a number in an empty square >>> 5
  +---+---+---+
  | 0 | 1 | 2 |
  +---+---+---+
  | 3 | X | O |
  +---+---+---+
  | 6 | 7 | 8 |
  +---+---+---+

Step 3:

...

Step 9:


  Game Over!!!







TicTacToe:
   Input: display game and prompt players  to input their choice 
     functions: display the game
   Process: Based on the choice from players, mark the new move.
            display the new game board.
   Output: display the game board
"""
def getName (step, playerX, playerO ):
  name = "";
  if step % 2 ==0: # if step number is even, then the current player is "X"
    name = playerX
  else:            # otherwise, the current player is "O"
    name = playerO
  return name

def getPlayer (step ):
  p = "";
  if step % 2 ==0: # if step number is even, then the current player is "X"
    p = "X"
  else:            # otherwise, the current player is "O"
    p = "O"
  return p

def getChoice (step, playerX, playerO ):
  p = getPlayer (step)          # p will be the curren player

  name = getName (step, playerX, playerO)
  # prompt user to enter the choice
  prompt = "Step " + str (step) + ": Hello " + name + \
     " , please choose a number at an empty square  >>> "
  n = int ( input (prompt) )
  return n

def updateStatus (s, n, step ):
  p = getPlayer (step)          # p will be the curren player
  s = s.replace ( str(n) , p)
  return s

def displayStatus (s ):
  line = "+---+---+---+"  # boardline
  #       | ? | ? | ? |
  #      "+---+---+---+"  # boardline
  #       | ? | ? | ? |
  #      "+---+---+---+"  # boardline
  #       | ? | ? | ? |
  #      "+---+---+---+"  # boardline
  print (line);
  k = 0  #  k is the square index, begining with 0
  for i in range (3): # repeat for each of three rows
    t= "|"            # each row begins with a left edge "|"
    for j in range (3): # repeat for each of three columns " ? |"
      t  += " " + s[k] + " |" # s[k] is the k_th letter in s
      k = k+1;
    print (t);
    print (line);

def playGame ( playerX, playerO ):
  s = "012345678"    # it prescribe the current game status
  step = 0          # keep track of the steps so far  

  displayStatus (s )
  for step in range ( 9 ):
    # prompt user to enter the choice
    n = getChoice ( step, playerX, playerO )      # get the square index "n" from player p
    # update the game status 
    s = updateStatus (s, n, step )   #  given
    displayStatus (s )

def main():
  prompt = "Player 1 (X): Enter your name >>> " 
  playerX = input ( prompt )
  if (playerX == ""):
    playerX = "X"
  prompt = "Player 2 (O): Enter your name >>> " 
  playerO = input ( prompt )
  if (playerO == ""):
    playerO = "O"

  while True:
    playGame ( playerX ,  playerO  )
    prompt = "Player another game (y/n) >>> " 
    if ( prompt != "y" ):
      break;
main ()

  





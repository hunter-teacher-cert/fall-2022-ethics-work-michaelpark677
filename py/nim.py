# Nim
# Moo Joon Park
# CSCI 77800 Fall 2022
# collaborators: none
# consulted: Brian Blais


#Initialize the starting player
player = 1

# Initialize the stack of objects
stack = int(input("Let's play the Nim game! \n\nHow many objects would you like on the stack? "))

# Loop will run until the stack is empty
while True:

  # Asks players how many objects to remove from the stack
  remove = int(input("Player " + str(player) + " removes how many objects? "))

  # Asks players to re-enter number if invalid number is entered
  while remove not in [1,2,3]:
    remove = int(input("Enter a number from 1 to 3: "))
    break

  # recalculates the number of objects in the stack
  stack = stack - remove

  # prints the new stack count
  print("Stack now has " + str(stack) + " object(s).")
  
  # check if the stack has no objects and declare winner
  if stack <= 0:
    print("Player " + str(player) + " wins!")
    break
    
  # switch player who will remove objects from the stack
  if player == 1:
    player = 2
  else:
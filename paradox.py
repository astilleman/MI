##
#  Simulate the Monty Hall Paradox.
#

from random import randint

# Count how many times the game is won with each strategy for 1000 trials.
keep_strategy = 0
switch_strategy = 0
for i in range(0, 1000) :
   
   # Select the winning door.
   winning_door = randint(1, 3)
   
   # Select a door for the user.
   user_door = randint(1, 3)
   
   # If the user did not select the winning door, the host only has one door
   # that he can open.
   if winning_door != user_door :
      other_door = 6 - user_door - winning_door
   else :
      # Randomly select one of the two non-winning doors.
      other_door = randint(1, 3)
      while other_door == user_door :
         other_door = randint(1, 3)
   
   # Record which strategy won this time.
   if user_door == winning_door :
      keep_strategy = keep_strategy + 1
   else :
      switch_strategy = switch_strategy + 1
   
# Display the number of games won with each strategy.
print(keep_strategy, "games were won by keeping the original door.")
print(switch_strategy, "games were won by switching to a different door.")


# INSTRUCTIONS: - UP, RIGHT, DOWN, LEFT, ARROWS TO PLAY
#               - 'SPACEBAR' TO PAUSE / RESUME
#               - PRESS 'ESC' BUTTON WHILE THE IS CURSER MOVING TO QUIT. WILL NOT ESCAPE IF PAUSED.
#               - HAVE FUN!! It's even more breaking down the code and understanding it all! :)
#
# Sidebar: I don't mean array... Jumping back and forth from languages :D | D:


import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, A_BOLD, A_UNDERLINE
from random import randint

print(KEY_UP, KEY_RIGHT, KEY_DOWN, KEY_LEFT)                                        # Put this print statement so you can see what these values are in case you don't want to go look for them. Will print after the game ends.
curses.initscr()                                                                    # This is the initialization of the terminal window.
win = curses.newwin(50, 120, 5, 10)                                                 # This will size the window to what you want.

win.attron(A_BOLD)                                                                  # Makes the message "snake attack!" in bold lettering
win.addstr( 15, 25, 'Snake attack!' )                                               # Just a fun message, immediately eaten by the snake when it starts. It doesn't add body to the snake
win.attroff(A_BOLD)                                                                 # Ends the bold lettering for "snake attack!"
win.keypad(1)                                                                       # Keep 1. 1 = yes. 0 = no. 
curses.noecho()
curses.curs_set(0)                                                                  # Curser 0 = invis. 1 = visible. 2 = very freakin visible.
win.nodelay(1)                                                                      # Why is this not making a difference?


key = KEY_RIGHT                                                                     # Assigning value for key
score = 0                                                                           # Assigning value to score
count = 0
snake = [[15,15],[0,0]]                                                             # snake[0] is the starting position. Each new list in the arry is a "body part" so in this case the snake starts with 2 body parts.

food = [randint(1, 49), randint(1, 119)]                                            # coordinates of where the first piece of food will be in the window. Random makes it more fun than the same spot each time.
win.addch(food[0], food[1], '$')                                                    # Assigns a character for that particular spot on the window where the food will start. Both index 0, and index 1 of Food will need the same char symbol. Think about it.


while key != 27:                                                                    # This is where the fun happens. 27 ASCII code for 'ESC'. When you hit it, while it's moving. It will break the while loop and end the window.
    win.attron(A_BOLD)                                                              
    win.border(0)                                                                   
    win.addstr(0, 15, ' Score : ' + str(score) + ' ')                               # Printing 'Score' on the window. You can position it where ever you want.
    win.addstr(0, 45, ' SNAKE! Traveled - ' + str(count) + ' spaces! ')             # Printing 'SNAKE' on the window. You can position it where ever you want
    win.attroff(A_BOLD)                                                    
    
    speed = int(90 - (len(snake)/5 + len(snake)/10) % 120)                          # Adjusts the speed. Write it out if it helps you do the math on how this equates. 
    win.timeout(speed)                                                              # Each time you eat food and a body part extends the body, this number will adjust to make it go faster.
    count += 1 
    
    prevKey = key                                                                   # Assigns var prevKey to the current key, or the last key pressed if unpressed again.
    event = win.getch()                                                             # var event waiting for win.getch() to capture character from user so it can exist.
    key = key if event == -1 else event                                             

    if key == ord(' '):                                                             # empty space == '32' which is ASCII for 'space bar'. If the keystroke is spacebar, key is assigned to 32 and gets stuck in this if statement. Then key is reassigned to -1. Thus placing it in a loop of being reassigned to -1 in the code above.
        key = -1                                                                    # one (Pause/Resume)

        while key != ord(' '):                                                      # Tried to explain the loop but it takes too much text. Figure it out :D
            key = win.getch()                                                       
            curses.beep()                                                           # Added a beep so you can hear when it repeats the loop. Just delete if it's annoying.

        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:                      # If an invalid key is pressed it reverts back to the stored prevKey
        key = prevKey

    # This insert actually adds a new 'head' to the snake, then the if statement below about the food, the else: in that statement actually pops the last array within the array so it appears to stay the same length when in fact it does increase here.
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # Will exit the game if the borders are touched by the snake.
    if snake[0][0] == 0 or snake[0][0] == 49 or snake[0][1] == 0 or snake[0][1] == 119:
        curses.beep() 
        break


    if snake[0] in snake[1:]:                                       # If the snakehead's [x,y] values match another value within the snakes array. It will exit.  
        break

    
    if snake[0] == food:                                            # When snakes postion on the window matches the foods position = "eaten". This if statement will execute.
        food = []                                                   # Reassigns food to an empty array, ready to be reassigned.    
        score += 1                                                  # LVL UP BITCH!
        while food == []:                                           # Executed because the window is hungry for food.
            food = [randint(1, 48), randint(1, 118)]                # Random [x,y]'s generated for the food, placing it somewhere on the window next.
            if food in snake:                                       # If the new generated foods values match a set of values within the snakes array, it will reset the while. 
                food = []                                          
        win.addch(food[0], food[1], '$')                            # WHen the new food passes the while validator, it will then be assigned to actual food variable.
    else:    
        last = snake.pop()                                          # Since the snake.insert statement above is adding new snake heads, if the snake doesn't eat the food, then it's here that the snake.pop() pops the last [x,y] in the snake array, but the tail end of the simulated snake.
        win.addch(last[0], last[1], ' ')                            # Now the snakes array doesn't contain this [x,y] but it's still printed to the screen. So this is called to fill that particular [x,y] coordinate with blanks. Essentially eraseing the symbol.
        
    win.addch(snake[0][0], snake[0][1], '@')                        # This keeps the head a '@'
    win.addch(snake[1][0], snake[1][1], '$')                        # Keeps the body of the snake '$' making it look more like a snake in action!
  
curses.endwin()                                                     # You should be able to figure this out.

print('Your score was ' + str(score) + '!')                         # Bet you cant beat my score of 245!! :D





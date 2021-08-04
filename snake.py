import random
import curses

# Creating the Window
s = curses.initscr() # initializes screen, always do first
curses.curs_set(0) # setting to 0 so it doesn't show up in screen
sh, sw = s.getmaxyx() # height and width of screen
w = curses.newwin(sh, sw, 0, 0) # making new window starting at top left hand corner of screen
w.keypad(1) # accepts keypad input
w.timeout(100) # refreshes every 100 milliseconds

# Creating the Snake
snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Creating the Food, starting place at center
food = [sh/2, sw/2]

# adds it to the screen as pi
w.addch(food[0], food[1], curses.ACS_PI) 

key = curses.KEY_RIGHT # snake initially goes to the right

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # end game if snake hits the border or if it's in itself
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin() # restores terminal to original operating mode
        quit()

    new_head = [snake[0][0], snake[0][1]]

    # figures how to move based on what key pressed
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    
    snake.insert(0, new_head)

    # food generates in random place after eaten else stays at the same position
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
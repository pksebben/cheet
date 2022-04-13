# Curses interface for cheet.

import curses

def setup():
    """
    Perform initialization.  Returns the screen intsance.
    """
    stdscr = curses.initscr() # get the terminal screen
    curses.noecho()           # Do not print every key to screen.
    curses.cbreak()             # Process input without waiting on ENTER
    stdscr.keypad(True)         # Allow returning of things like curses.KEY_LEFT instead of escape bytes
    
    return stdscr

def teardown(screen):
    """
    Clean up terminal once we're done with it
    """
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    

def main(screen):
    # do the rest of the work
    screen.clear()
    curses.start_color()
    screen.addstr(0,0, "test")
    screen.refresh()
    curses.napms(2000)
    screen.clear()
    screen.addstr("another test")

    # Window 1
    win = curses.newwin(100, 100, 0, 0)
    win.addstr(0,0, "test")
    win.refresh()
    
    screen.getkey()
    pass

if __name__ == "__main__":
    print("init cheet curses")
    curses.wrapper(main)

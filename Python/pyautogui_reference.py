import pyautogui

# Move mouse
# pyautogui.moveTo(0,1080) #  Move to bottom left of screen.
# pyautogui.moveTo(1920,1080) #  Move to bottom right of screen.
# pyautogui.moveTo(1920,0) #  Move to top right of screen.
# pyautogui.moveTo(1000,0)  # Move to top left of screen.
# pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
# pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position

# Scrolling and dragging
# pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
# pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
# pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position

# Writing
# pyautogui.keyDown('a')  # Holds down the 'a' key.
# pyautogui.keyUp('a')  # Releases the 'a' key.
# pyautogui.typewrite('Hello, world!')  # Types message instantly.
# pyautogui.typewrite('Hello, world!', interval=seconds)  # Types one key per interval.
# pyautogui.typewrite('Hello, world!')

# Hot keys
# pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
# pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
# Keys of note: 'win', 'winleft', 'winright', 'backspace', 'browserrefresh'
# TL;DR: Everything is lowercase and there are browser controls / all misc. keys accounted for.

# Clicking
# pyautogui.click()  # Clicks wherever the mouse currently is.
# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
# pyautogui.rightClick(x=moveToX, y=moveToY)
# pyautogui.middleClick(x=moveToX, y=moveToY)
# pyautogui.doubleClick(x=moveToX, y=moveToY)

# Screenshots
# pyautogui.screenshot()
# pyautogui.screenshot('foo.png')  # returns a Pillow/PIL Image object, and saves it to a file

# Screen recognition
# autogui.locateOnScreen('looksLikeThis.png')  # returns (left, top, width, height) of first place it is found
# list(pyautogui.locateAllOnScreen('looksLikeThis.png'))  # Lists all found matches.

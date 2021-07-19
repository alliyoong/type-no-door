from pynput.keyboard import Controller, Key, Listener
from pynput import mouse
import time
import pyscreenshot
import pytesseract

def on_click(x, y, button, pressed):
    if pressed:
        on_click.x = x
        on_click.y = y
    else:
        on_click.xx = x
        on_click.yy = y
    if not pressed:
        return False

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

    
img = pyscreenshot.grab(bbox=(on_click.x, on_click.y, on_click.xx, on_click.yy))
img.save('screenshot.png')
        
text = str(pytesseract.image_to_string(img, lang='eng')).replace('|', 'I')
text = ' '.join(text.splitlines())
print(text)

keyboard = Controller()

def on_press(key):
    if key == Key.shift:
        for i in text:
            keyboard.press(i)
            keyboard.release(i)
            time.sleep(0.05)
        return False
            
with Listener(on_press=on_press) as listener:
    listener.join()


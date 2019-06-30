from pynput.mouse import Listener
from pynput.keyboard import Key, Listener, KeyCode
import logging

logging.basicConfig(filename=("mouse_log1.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

counter = 0

# def on_click(x, y, button, pressed):
#     if pressed:
#         logging.info(' clicked at ({0}, {1}) with {2}'.format(x, y, button))

#counts the amount of clicks with left mouse  and saves the count into a file 

def on_click(x, y, button, pressed):
    global counter

    if pressed:
        counter += 1
        # print(counter)faaa
        logging.info(counter)

def on_press(key):
        a = "a"
        if key.char == 'a':
                print('a was pressed ')
        else:
                print('not a ')

#     print('{0} pressed'.format(
#         key))
        
with Listener( on_click=on_click, on_press=on_press) as listener:
    listener.join()
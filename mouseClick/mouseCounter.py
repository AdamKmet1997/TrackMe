from pynput.mouse import Listener
import logging

logging.basicConfig(filename=("mouse_log7.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

counter = 0

# def on_click(x, y, button, pressed):
#     if pressed:
#         logging.info(' clicked at ({0}, {1}) with {2}'.format(x, y, button))

#counts the amount of clicks with left mouse  and saves the count into a file 

def on_click(x, y, button, pressed):
    global counter

    if pressed:
        counter += 1
        # print(counter)
        logging.info(counter)

with Listener( on_click=on_click) as listener:
    listener.join() 
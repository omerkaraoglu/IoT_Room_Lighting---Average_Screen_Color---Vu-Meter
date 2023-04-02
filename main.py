import mss
import cv2
from PIL import Image, ImageStat
import udpclient
import numpy as np
import time

def screenshot():
    # Capture entire screen
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        img = sct.grab(monitor)

        img = cv2.resize(np.array(img), (128, 72))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)

        return img


def send_color(RGB_array, FPS):
    udpclient.send_RGB_string(int(round(RGB_array[0])), int(round(RGB_array[1])), int(round(RGB_array[2])))
    time.sleep(1 / FPS*2)


# screenshot().show()
# update_flag = 0


while 1:
    if True:  # udpclient.incoming('N'):
        avg_color = ImageStat.Stat(screenshot()).mean
        send_color(avg_color, 144)

        # print(avg_color, update_flag)
        # update_flag += 1

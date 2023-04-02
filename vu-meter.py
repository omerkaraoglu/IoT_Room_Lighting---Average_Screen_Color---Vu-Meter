import sounddevice as sd
import numpy as np
import udpclient as client


def disco(RMS, rms):
    if RMS < 100:
        R = RMS
        G = round(RMS * rms ** 4)
        B = 0

    elif 100 <= RMS and RMS < 128:
        R = round(RMS * rms ** 2)
        G = round(RMS * rms)
        B = round(RMS * rms ** 4)

    elif 128 <= RMS:
        R = 255 - RMS
        G = 0
        B = round(RMS * rms)

    client.send_RGB_string(R, G, B)


def warm(RMS, rms):
    if RMS < 192:
        R = RMS
        G = round(R * rms ** 2)
        B = 0

    elif 192 <= RMS:
        R = RMS
        G = round(RMS * rms)
        B = 0

    client.send_RGB_string(R, G, B)


def retrowave(RMS, rms):
    if RMS < 128:
        R = RMS
        G = 0
        B = round(RMS * rms)

    elif 128 <= RMS:
        R = 255 - RMS
        G = 0
        B = round(RMS * rms)

    client.send_RGB_string(R, G, B)


def death_metal(RMS, rms):      
    if RMS < 92:
        R = round(RMS * rms)
        G = round(RMS * rms ** 3)
        B = round(RMS * rms ** 4)

    elif 92 <= RMS and RMS < 144:
        R = RMS
        G = round(RMS * rms ** 4)
        B = round(RMS * rms ** 5)

    elif 144 <= RMS:
        R = RMS
        G = round(RMS * rms ** 6)
        B = round(RMS * rms ** 7)

    client.send_RGB_string(R, G, B)

def black_metal(RMS, rms):
    R = round(RMS * rms)
    G = 0
    B = 0
    
    client.send_RGB_string(R, G, B)


# print(sd.query_devices())

BLOCKSIZE = 1024  # Buffer
RATE = 48000  # Sample Rate

sd.default.device = 'CABLE Output (VB-Audio Virtual Cable), Windows DirectSound'
sd.default.channels = 2


def select():
    return int(input("""
    -----SELECT MODE-----
    1 - Disco
    2 - Warm
    3 - Retro
    4 - Death Metal
    5 - Black Metal
    
    Selection: """))


def mode(RMS, rms, selection):
    if selection == 1:
        disco(RMS, rms)
    elif selection == 2:
        warm(RMS, rms)
    elif selection == 3:
        retrowave(RMS, rms)
    elif selection == 4:
        death_metal(RMS, rms)
    elif selection == 5:
        black_metal(RMS, rms)


selection = select()


def callback(indata, frames, time, status):
    audio = np.asarray(indata)

    rms = np.sqrt(np.mean(np.square(audio)))
    RMS = round(rms * 255)

    mode(RMS, rms, selection)


with sd.InputStream(blocksize=BLOCKSIZE, samplerate=RATE, callback=callback):
    while True:
        pass

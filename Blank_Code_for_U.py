# importing all libraries
import board
import neopixel
import time
import analogio
import digitalio
import random
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket
from adafruit_bluefruit_connect.button_packet import ButtonPacket
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
try:
    from audiocore import WaveFile
except ImportError:
    from audioio import WaveFile
try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

# Enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

ble = BLERadio()
uart_service = UARTService()
advertisement = ProvideServicesAdvertisement(uart_service)
LED = 204
lights = neopixel.NeoPixel(board.A6, LED, brightness=0.4, auto_write=False)
frame = 0
on = []
setting = "NA"
print("hello world")
print(on)
on_Length = len(on)
LastTime = -1
lights.fill(0)
lights.show()
color = (255, 0, 0)
mode = 0


# DONT EDIT, function forces tv to update when called
def write():
    global on
    for i in range(len(on)):
        if lights[on[i]] != (0, 0, 0):
            lights[on[i]] = (0, 0, 0)
        else:
            lights[on[i]] = (255, 0, 0)
    lights.show()
    on = []
    print("show")

# Animation Libraries
# Name libraries accordingly, this is how their refrenced
# "F0" = setup frame, will only be called once when screen swaps setting
# "F1"-"Finf" = what pixels will change each frame of animation
# "Frame_cnt" = amt of frames in animation
# "Rate" = how long will the animation wait between loops(make zero for continouous ani)
# "Timing" = time between each frame, make sure firs number is always 0
Off = {
   "F0" : (),
   "F1" : (),
   "F2" : (),
   "Frame_cnt" : 2,
   "Rate" : 0,
   "Timing" : (0.1, 0.1, 0.1)
}

# main while true loop, starts by advertising bluetooth
while True:
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()
    while ble.connected:
        now = time.monotonic()
        if setting != "NA":
            if now >= setting["Rate"] + LastTime or loopDone == 0:
                loopDone = 0
                if loopDone == 0:
                    if now >= setting["Timing"][frame] + LastTime:
                        print("update now")
                        current = "F" + str(frame)
                        print(current)
                        on = setting[current]
                        for i in range(len(on)):
                            if lights[on[i]] != (0, 0, 0):
                                lights[on[i]] = (0, 0, 0)
                            else:
                                lights[on[i]] = (color)
                        lights.show()
                        on = []
                        print("show")
                        LastTime = now
                        frame = frame + 1
                        if frame > setting["Frame_cnt"]:
                            frame = 1
                            loopDone = 1
        if uart_service.in_waiting:
            packet = Packet.from_stream(uart_service)
            if isinstance(packet, ColorPacket):
                color = (packet.color)
                on.clear()
                lights.fill(0)
                lights.show
                frame = 0
                loopDone = 0
                print(color)
            if isinstance(packet, ButtonPacket):
               # add library names here
               # comments specify directions
               if packet.pressed:
                    on.clear()
                    lights.fill(0)
                    lights.show
                    frame = 0
                    loopDone = 0
                    if packet.button == ButtonPacket.BUTTON_1:
                        #  1, no direction
                        setting = Off
                        mode = 1
                    if packet.button == ButtonPacket.BUTTON_2:
                         # 2, no direction
                        setting = Off
                        mode = 2
                    if packet.button == ButtonPacket.BUTTON_3:
                        #  3, no direction
                        setting = Off
                        mode = 3
                    if packet.button == ButtonPacket.BUTTON_4:
                        # 4, no direction
                        setting = Off
                        mode = 4
                    if packet.button == ButtonPacket.UP:
                        if mode == 1:
                            # 1, UP
                            pass
                        if mode == 2:
                            # 2, UP
                            pass
                        if mode == 3:
                            # 3, UP
                            pass
                        if mode == 4:
                            # 4, UP
                            pass
                    if packet.button == ButtonPacket.DOWN:
                        if mode == 1:
                            # 1, DOWN
                            pass
                        if mode == 2:
                            # 2, DOWN
                            pass
                        if mode == 3:
                            # 3, DOWN
                            pass
                        if mode == 4:
                            # 4, DOWN
                            pass
                    if packet.button == ButtonPacket.LEFT:
                        if mode == 1:
                            # 1, LEFT
                            pass
                        if mode == 2:
                            #2, LEFT
                            pass
                        if mode == 3:
                            # 3, LEFT
                            pass
                        if mode == 4:
                            # 4, LEFT
                            pass
                    if packet.button == ButtonPacket.RIGHT:
                        if mode == 1:
                            # 1, RIGHT
                            pass
                        if mode == 2:
                            # 2, RIGHT
                            pass
                        if mode == 3:
                            # 3, RIGHT
                            pass
                        if mode == 4:
                            # 4, RIGHT
                            pass
                    print(setting)
                    on_Length = len(on)
                    print(on)

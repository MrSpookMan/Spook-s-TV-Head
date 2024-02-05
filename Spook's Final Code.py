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
face_owo = (38 ,39 ,45 ,46 ,55 ,56 ,62 ,63 ,72 ,73 ,79 ,80 ,89
,90 ,96 ,97 ,140 ,144 ,148 ,158 ,159 ,160 ,162 ,163 ,164)
print(on)
on_Length = len(on)
LastTime = -1
lights.fill(0)
lights.show()
color = (255, 0, 0)
mode = 0

def bootup(filename):
# custom animation for when the tv connects to bluetooth,
# if you want to get rid of it or change it edit over this
# code or delete Bootup function in the while true loop
    global on
    global on_Length
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with WaveFile(wave_file) as wave:
        with AudioOut(board.SPEAKER) as audio:
            audio.play(wave)
            while audio.playing:
                for i in range(12):
                    lights.fill(0)
                    lights.show()
                    if i == 0:
                        on = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                    else:
                        for a in range(17):
                            on[a] = on[a] + 17
                    for i in range(len(on)):
                        if lights[on[i]] != (0, 0, 0):
                            lights[on[i]] = (0, 0, 0)
                        else:
                            lights[on[i]] = (255, 0, 0)
                    lights.show()
                    print("show")
                    print(on)
                    time.sleep(0.055)
                for i in range(12):
                    lights.fill(0)
                    lights.show()
                    if i == 0:
                        on = [187 ,188 ,189 ,190 ,191 ,192 ,193 ,194 ,195 ,196 ,
                        197 ,198 ,199 ,200 ,201 ,202 ,203]
                    else:
                        for a in range(17):
                            on[a] = on[a] - 17
                    for i in range(len(on)):
                        if lights[on[i]] != (0, 0, 0):
                            lights[on[i]] = (0, 0, 0)
                        else:
                            lights[on[i]] = (0, 0, 255)
                    lights.show()
                    print("show")
                    print(on)
                    time.sleep(0.055)
                lights.fill(0)
                lights.show
                # this shows my personal trademark/name for the tv(Spook OS)
                # change this string to a diffrent design
                # from the translator if you wanna edit it
                on = [1 ,2 ,17 ,19 ,28 ,29 ,33 ,35 ,38 ,40 ,42 ,45 ,48 ,49 ,51 ,53 ,
                55 ,57 ,58 ,60 ,62 ,63 ,65 ,68 ,69 ,
                72 ,76 ,79 ,82 ,84 ,107 ,108 ,109 ,113 ,114 ,125 ,127 ,131 ,
                140 ,144 ,147 ,157 ,161 ,165 ,175 ,176 ,177 ,180 ,181]
                for i in range(len(on)):
                    if lights[on[i]] != (0, 0, 0):
                        lights[on[i]] = (0, 0, 0)
                    else:
                        # RGB color for logo
                        lights[on[i]] = (255, 255, 255)
                    lights.show()
                time.sleep(1.768)
    print("Finished")
    lights.fill(0)
    lights.show()

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
# feel free to edit or delete existing libraries, but make sure names of
# deleted libraries dont appear in code later
# Name libraries accordingly, this is how their refrenced
# "F0" = setup frame, will only be called once when screen swaps setting
# "F1"-"Finf" = what pixels will change each frame of animation
# "Frame_cnt" = amt of frames in animation
# "Rate" = how long will the animation wait between loops(make zero for continouous ani)
# "Timing" = time between each frame, make sure firs number is always 0
# All current animations only work for 17 by 13 grids
FaceUwU = {
    "F0" : (38 ,39 ,45 ,46 ,55 ,56 ,62 ,63 ,72 ,73 ,79 ,80 ,89
    ,90 ,96 ,97 ,140 ,144 ,148 ,158 ,159 ,160 ,162 ,163 ,164),
    "F1" : (38, 39, 45, 46),
    "F2" : (55, 56, 62, 63),
    "F3" : (72, 73, 79, 80),
    "F4" : (89, 90, 96, 97),
    "F5" : (89, 90, 96, 97),
    "F6" : (72, 73, 79, 80),
    "F7" : (55, 56, 62, 63),
    "F8" : (38, 39, 45, 46),
    "Frame_cnt" : 8,
    "Rate" : 5,
    "Timing" : (0, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1),
}

eyeN = {
   "F0" : (40 ,41 ,42 ,43 ,44 ,54 ,55 ,56 ,62 ,63 ,64 ,69 ,70 ,
   76 ,82 ,83 ,85 ,93 ,101 ,103 ,104 ,110 ,116 ,117 ,122 ,123 ,
   124 ,130 ,131 ,132 ,142 ,143 ,144 ,145 ,146),
   "F1" : (40 ,41 ,42 ,43 ,44 ,57 ,58 ,59 ,60 ,61),
   "F2" : (54 ,55 ,56 ,57 ,58 ,59 ,60 ,61 ,62 ,63 ,64 ,71 ,72 ,
   73 ,74 ,75 ,77 ,78 ,79 ,80 ,81),
   "F3" : (69 ,70 ,71 ,72 ,73 ,74 ,75 ,76 ,77 ,78 ,79 ,80 ,81 ,
   82 ,83 ,86 ,87 ,88 ,89 ,90 ,91 ,92 ,94 ,95 ,96 ,97 ,98 ,99 ,100),
   "F4" : (86 ,87 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,97 ,98 ,99 ,
   100 ,105 ,106 ,107 ,108 ,109 ,111 ,112 ,113 ,114 ,115),
   "F5" : (107 ,108 ,109 ,110 ,111 ,112 ,113 ,125 ,126 ,127 ,128 ,129,
   105 ,106 ,114 ,115),
   "F6" : (125 ,126 ,127 ,128 ,129),
   "F7" : (125 ,126 ,127 ,128 ,129),
   "F8" : (107 ,108 ,109 ,110 ,111 ,112 ,113 ,125 ,126 ,127 ,128 ,129,
   105 ,106 ,114 ,115),
   "F9" : (86 ,87 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,97 ,98 ,99 ,
   100 ,105 ,106 ,107 ,108 ,109 ,111 ,112 ,113 ,114 ,115),
   "F10" : (69 ,70 ,71 ,72 ,73 ,74 ,75 ,76 ,77 ,78 ,79 ,80 ,81 ,
   82 ,83 ,86 ,87 ,88 ,89 ,90 ,91 ,92 ,94 ,95 ,96 ,97 ,98 ,99 ,100),
   "F11" : (54 ,55 ,56 ,57 ,58 ,59 ,60 ,61 ,62 ,63 ,64 ,71 ,72 ,
   73 ,74 ,75 ,77 ,78 ,79 ,80 ,81),
   "F12" : (40 ,41 ,42 ,43 ,44 ,57 ,58 ,59 ,60 ,61),
   "Frame_cnt" : 12,
   "Rate" : 5,
   "Timing" : (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
   }

eyeCry = {
   "F0" : (40 ,41 ,42 ,43 ,44 ,54 ,55 ,56 ,62 ,63 ,64 ,69 ,70 ,76 ,82 ,83 ,85 ,92 ,94
,101 ,103 ,104 ,110 ,116 ,117 ,122 ,123 ,124 ,130 ,131 ,132 ,142 ,143 ,144 ,145 ,146),
   "F1" : (161, 0, 0),
   "F2" : (177 ,178 ,179),
   "F3" : (194 ,195 ,196),
   "F4" : (161 ,177 ,179),
   "F5" : (178 ,194 ,196),
   "F6" : (195 , 0, 0),
   "Frame_cnt" : 6,
   "Rate" : 1.5,
   "Timing" : (0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
   }

eyePissed = {
   "F0" : (69 ,70 ,71 ,72 ,73 ,74 ,75 ,76 ,77 ,78 ,79 ,80 ,81 ,82 ,83 ,85 ,93
   ,101 ,103 ,104 ,110 ,116 ,117 ,122 ,123 ,124 ,130 ,131 ,132 ,142 ,143 ,144 ,145 ,146),
   "F1" : (69 ,70 ,71 ,72 ,73 ,74 ,75 ,76 ,77 ,78 ,79 ,80 ,81 ,
   82 ,83 ,86 ,87 ,88 ,89 ,90 ,91 ,92 ,94 ,95 ,96 ,97 ,98 ,99 ,100),
   "F2" : (86 ,87 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,97 ,98 ,99 ,
   100 ,105 ,106 ,107 ,108 ,109 ,111 ,112 ,113 ,114 ,115),
   "F3" : (107 ,108 ,109 ,110 ,111 ,112 ,113 ,125 ,126 ,127 ,128 ,129,
   105 ,106 ,114 ,115),
   "F4" : (125 ,126 ,127 ,128 ,129),
   "F5" : (125 ,126 ,127 ,128 ,129),
   "F6" : (107 ,108 ,109 ,110 ,111 ,112 ,113 ,125 ,126 ,127 ,128 ,129,
   105 ,106 ,114 ,115),
   "F7" : (86 ,87 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,97 ,98 ,99 ,
   100 ,105 ,106 ,107 ,108 ,109 ,111 ,112 ,113 ,114 ,115),
   "F8" : (69 ,70 ,71 ,72 ,73 ,74 ,75 ,76 ,77 ,78 ,79 ,80 ,81 ,
   82 ,83 ,86 ,87 ,88 ,89 ,90 ,91 ,92 ,94 ,95 ,96 ,97 ,98 ,99 ,100),
   "Frame_cnt" : 8,
   "Rate" : 5,
   "Timing" : (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
   }

eyeLove = {
   "F0" : (40 ,41 ,42 ,43 ,44 ,54 ,55 ,56 ,62 ,63 ,64 ,69 ,70 ,75 ,77 ,82 ,83 ,85 ,
   92 ,93 ,94 ,101 ,103 ,104 ,110 ,116 ,117 ,122 ,123 ,124 ,130 ,131 ,
   132 ,142 ,143 ,144 ,145 ,146),
   "F1" : (0 ,2 ,14 ,16 ,17 ,18 ,19 ,31 ,32 ,33 ,35 ,49 ,153 ,155 ,167 ,169 ,170 ,171 ,
172 ,184 ,185 ,186 ,188 ,202),
   "F2" : (0 ,2 ,14 ,16 ,17 ,18 ,19 ,31 ,32 ,33 ,35 ,49 ,153 ,155 ,167 ,169 ,170 ,171 ,
172 ,184 ,185 ,186 ,188 ,202),
   "Frame_cnt" : 2,
   "Rate" : 0,
   "Timing" : (0.0, 0.25, 0.25)
   }

eyeFuck = {
   "F0" : (40 ,41 ,42 ,43 ,44 ,54 ,55 ,56 ,62 ,63 ,64 ,69 ,70 ,82 ,83 ,85 ,
93 ,101 ,103 ,104 ,116 ,117 ,122 ,123 ,124 ,130 ,131 ,132 ,142 ,143 ,144 ,145 ,146),
   "F1" : (92 ,93),
   "F2" : (92 ,91),
   "F3" : (91 ,90),
   "F4" : (90 ,89),
   "F5" : (90 ,89),
   "F6" : (91 ,90),
   "F7" : (92 ,91),
   "F8" : (92 ,93),
   "F9" : (93 ,94),
   "F10" : (94 ,95),
   "F11" : (95 ,96),
   "F12" : (97 ,96),
   "F13" : (97 ,96),
   "F14" : (95 ,96),
   "F15" : (94 ,95),
   "F16" : (94, 93),
   "Frame_cnt" : 16,
   "Rate" : 3,
   "Timing" : (0, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
   0.1, 0.2, 0.1, 0.1, 0.1)
}
faceN = {
   "F0" : (38 ,39 ,45 ,46 ,55 ,56 ,62 ,63 ,72 ,73 ,79 ,80 ,89 ,90 ,96 ,97 ,106
   ,107 ,113 ,114),
   "F1" : (38, 39, 45, 46),
   "F2" : (55, 56, 62, 63),
   "F3" : (72, 73, 79, 80),
   "F4" : (89, 90, 96, 97),
   "F5" : (106, 107, 113, 114),
   "F6" : (106, 107, 113, 114),
   "F7" : (89, 90, 96, 97),
   "F8" : (72, 73, 79, 80),
   "F9" : (55, 56, 62, 63),
   "F10" : (38, 39, 45, 46),
   "Frame_cnt" : 10,
   "Rate" : 5,
   "Timing" : (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
}

faceHeart = {
   "F0" : (36 ,37 ,39 ,40 ,44 ,45 ,47 ,48 ,52 ,55 ,58 ,60 ,63 ,66 ,69 ,75 ,
77 ,83 ,86 ,92 ,94 ,100 ,104 ,108 ,112 ,116 ,122 ,124 ,130 ,132 ,140 ,148),
   "F1" : (89 ,97),
   "F2" : (71 ,73 ,79 ,81 ,88 ,90 ,96 ,98 ,106 ,114),
   "F3" : (53 ,54 ,56 ,57 ,61 ,62 ,64 ,65 ,70 ,72 ,74 ,78 ,80 ,82 ,87 ,91 ,95 ,
   99 ,105 ,107 ,113 ,115 ,123 ,131),
   "Frame_cnt" : 3,
   "Rate" : 0,
   "Timing" : (0, 0.1, 0.1, 0.1)
   }

faceDead = {
   "F0" : (19 ,23 ,27 ,31 ,37 ,39 ,45 ,47 ,55 ,63 ,71 ,73 ,79 ,81 ,87 ,91 ,95 ,99),
   "F1" : (19 ,23 ,27 ,31 ,37 ,39 ,45 ,47 ,55 ,63 ,71 ,73 ,79 ,81 ,87 ,91 ,95 ,99 ,
18 ,22 ,26 ,30 ,38 ,40 ,46 ,48 ,54 ,62 ,72 ,74 ,80 ,82 ,86 ,90 ,94 ,98),
   "F2" : (18 ,22 ,26 ,30 ,38 ,40 ,46 ,48 ,54 ,62 ,72 ,74 ,80 ,82 ,86 ,90 ,94 ,98 ,
20 ,24 ,28 ,32 ,36 ,38 ,44 ,46 ,56 ,64 ,70 ,72 ,78 ,80 ,88 ,92 ,96 ,100),
   "F3" : (20 ,24 ,28 ,32 ,36 ,38 ,44 ,46 ,56 ,64 ,70 ,72 ,78 ,80 ,88 ,92 ,96 ,100),
   "F4" : (19 ,23 ,27 ,31 ,37 ,39 ,45 ,47 ,55 ,63 ,71 ,73 ,79 ,81 ,87 ,91 ,95 ,99),
   "Frame_cnt" : 2,
   "Rate" : .5,
   "Timing" : (0, 0.1, 0.1, 0.1, 0.15)
   }

faceCry = {
   "F0" : (19 ,20 ,21 ,29 ,30 ,31 ,35 ,39 ,45 ,49 ,52 ,56 ,62 ,66 ,69 ,73 ,79 ,83 ,
87 ,88 ,89 ,97 ,98 ,99 ,142 ,144 ,146 ,158 ,160 ,162 ,164),
   "F1" : (107 ,117),
   "F2" : (120 ,130),
   "F3" : (107 ,117, 120 ,130),
   "Frame_cnt" : 3,
   "Rate" : 0,
   "Timing" : (0, 0.2, 0.2, 0.2)
   }

faceHuh = {
   "F0" : (20 ,21 ,22 ,29 ,30 ,31 ,39 ,48 ,53 ,62 ,73 ,82 ,88 ,89 ,97 ,98 ,105 ,114 ,139 ,148),
   "F1" : (20 ,21 ,22 ,29 ,30 ,31 ,39 ,48 ,53 ,62 ,73 ,82 ,88 ,89 ,97 ,98 ,105 ,114 ,139 ,148),
   "F2" : (20 ,21 ,22 ,29 ,30 ,31 ,39 ,48 ,53 ,62 ,73 ,82 ,88 ,89 ,97 ,98 ,105 ,114 ,139 ,148),
   "Frame_cnt" : 2,
   "Rate" : 1,
   "Timing" : (0, .75, .75)
   }

Off = {
   "F0" : (),
   "F1" : (),
   "F2" : (),
   "Frame_cnt" : 2,
   "Rate" : 0,
   "Timing" : (0.1, 0.1, 0.1)
}

lowBattery = {
   "F0" : (55 ,56 ,57 ,58 ,59 ,60 ,61 ,62 ,63 ,64 ,71 ,72 ,73 ,74 ,75 ,77 ,78 ,79 ,80 ,81 ,88 ,
89 ,90 ,91 ,95 ,96 ,97 ,98 ,105 ,106 ,107 ,108 ,109 ,
111 ,112 ,113 ,114 ,115 ,123 ,124 ,125 ,126 ,127 ,128 ,129 ,130 ,131 ,132),
   "F1" : (78 ,79 ,80 ,89 ,90 ,91 ,112 ,113 ,114),
   "F2" : (75 ,77 ,92 ,93 ,94 ,109 ,111),
   "F3" : (72 ,73 ,74 ,95 ,96 ,97 ,106 ,107 ,108),
   "F4" : (78 ,79 ,80 ,89 ,90 ,91 ,112 ,113 ,114 ,75 ,77 ,92 ,93 ,94 ,109 ,111 ,72 ,73 ,74 ,
95 ,96 ,97 ,106 ,107 ,108),
   "Frame_cnt" : 4,
   "Rate" : 0,
   "Timing" : (0, .75, .75, .75, .75)
}

loading = {
   "F0" : (),
   "F1" : (70 ,71 ,72 ,97 ,98 ,99 ,104 ,105 ,106),
   "F2" : (75 ,76 ,77 ,92 ,93 ,94 ,109 ,110 ,111),
   "F3" : (80 ,81 ,82 ,87 ,88 ,89 ,114 ,115 ,116),
   "F4" : (70 ,71 ,72 ,75 ,76 ,77 ,80 ,81 ,82 ,87 ,88 ,89 ,92 ,93 ,94 ,97
   ,98 ,99 ,104 ,105 ,106 ,109 ,110 ,111 ,114 ,115 ,116),
   "Frame_cnt" : 4,
   "Rate" : 0,
   "Timing" : (0, 1, 1, 1, 1),
}

error = {
   "F0" : (35 ,38 ,41 ,42 ,43 ,46 ,49 ,52 ,55 ,57 ,61 ,63 ,66 ,69 ,72 ,
   74 ,78 ,80 ,83 ,86 ,87 ,88 ,89 ,91 ,95 ,97 ,98 ,99 ,100 ,106 ,108 ,112 ,
   117 ,120 ,125 ,129 ,131 ,140 ,143 ,144 ,145 ,151,),
   "F1" : (35 ,38 ,41 ,42 ,43 ,46 ,49 ,52 ,55 ,57 ,61 ,63 ,66 ,69 ,72 ,
   74 ,78 ,80 ,83 ,86 ,87 ,88 ,89 ,91 ,95 ,97 ,98 ,99 ,100 ,106 ,108 ,112 ,
   117 ,120 ,125 ,129 ,131 ,140 ,143 ,144 ,145 ,151,),
   "F2" : (35 ,38 ,41 ,42 ,43 ,46 ,49 ,52 ,55 ,57 ,61 ,63 ,66 ,69 ,72 ,
   74 ,78 ,80 ,83 ,86 ,87 ,88 ,89 ,91 ,95 ,97 ,98 ,99 ,100 ,106 ,108 ,112 ,
   117 ,120 ,125 ,129 ,131 ,140 ,143 ,144 ,145 ,151,),
   "Frame_cnt" : 2,
   "Rate" : 0,
   "Timing" : (0, .75, .75),
}

vitals = {
   "F0" : (85 ,86 ,87 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,97 ,98 ,99 ,100 ,101),
   "F1" : (67 ,68 ,101),
   "F2" : (33 ,34 ,66 ,67 ,68 ,69 ,100),
   "F3" : (0 ,32 ,33 ,34 ,35 ,65 ,66 ,69 ,70 ,99),
   "F4" : (0 ,1 ,31 ,32 ,33 ,34 ,35 ,36 ,64 ,65 ,70 ,71 ,98),
   "F5" : (1 ,2 ,30 ,31 ,32 ,33 ,34 ,35 ,36 ,37 ,63 ,64 ,67 ,68 ,71 ,72 ,97),
   "F6" : (2 ,3 ,29 ,30 ,31 ,32 ,35 ,36 ,37 ,38 ,
62 ,63 ,66 ,67 ,68 ,69 ,72 ,73 ,96 ,101),
   "F7" : (3 ,4 ,28 ,29 ,30 ,31 ,36 ,37 ,38 ,39 ,61 ,
62 ,65 ,66 ,69 ,70 ,73 ,74 ,95 ,100),
   "F8" : (4 ,5 ,27 ,28 ,29 ,30 ,37 ,38 ,39 ,40 ,
60 ,61 ,64 ,65 ,70 ,71 ,74 ,75 ,94 ,99 ,101 ,102),
   "F9" : (5 ,6 ,26 ,27 ,28 ,29 ,38 ,39 ,40 ,41 ,59 ,60 ,
63 ,64 ,71 ,72 ,75 ,76 ,93 ,98 ,100 ,102 ,103 ,135),
   "F10" : (6 ,7 ,25 ,26 ,27 ,28 ,39 ,40 ,41 ,42 ,58 ,59 ,
62 ,63 ,72 ,73 ,76 ,77 ,92 ,97 ,99 ,102 ,103 ,104 ,134 ,135),
   "F11" : (7 ,8 ,24 ,25 ,26 ,27 ,40 ,41 ,42 ,43 ,57 ,58 ,61 ,
62 ,73 ,74 ,77 ,78 ,91 ,96 ,98 ,101 ,102 ,103 ,104 ,105 ,133 ,134),
   "F12" : (8 ,9 ,23 ,24 ,25 ,26 ,41 ,42 ,43 ,44 ,56 ,57 ,60 ,61 ,
74 ,75 ,78 ,79 ,90 ,95 ,97 ,100 ,103 ,104 ,105 ,106 ,132 ,133),
   "F13" : (9 ,10 ,22 ,23 ,24 ,25 ,42 ,43 ,44 ,45 ,55 ,56 ,59 ,
60 ,75 ,76 ,79 ,80 ,89 ,94 ,96 ,99 ,104 ,105 ,106 ,107 ,131 ,132),
   "F14" : (10 ,11 ,21 ,22 ,23 ,24 ,43 ,44 ,45 ,46 ,54 ,55 ,58 ,59 ,
76 ,77 ,80 ,81 ,88 ,93 ,95 ,98 ,105 ,106 ,107 ,108 ,130 ,131),
   "F15" : (11 ,12 ,20 ,21 ,22 ,23 ,44 ,45 ,46 ,47 ,53 ,54 ,57 ,58 ,
77 ,78 ,81 ,82 ,87 ,92 ,94 ,97 ,106 ,107 ,108 ,109 ,129 ,130),
   "F16" : (12 ,13 ,19 ,20 ,21 ,22 ,45 ,46 ,47 ,48 ,52 ,53 ,56 ,
57 ,78 ,79 ,82 ,83 ,86 ,91 ,93 ,96 ,107 ,108 ,109 ,110 ,128 ,129),
   "F17" : (13 ,14 ,18 ,19 ,20 ,21 ,46 ,47 ,48 ,49 ,51 ,52 ,55 ,56 ,
79 ,80 ,83 ,84 ,85 ,90 ,92 ,95 ,108 ,109 ,110 ,111 ,127 ,128),
   "F18" : (14 ,15 ,17 ,18 ,19 ,20 ,47 ,48 ,49 ,50 ,51 ,54 ,
55 ,80 ,81 ,84 ,89 ,91 ,94 ,109 ,110 ,111 ,112 ,126 ,127),
   "F19" : (15 ,16 ,17 ,18 ,19 ,48 ,49 ,50 ,53 ,54 ,81 ,
82 ,88 ,90 ,93 ,110 ,111 ,112 ,113 ,125 ,126),
   "F20" : (16 ,17 ,18 ,49 ,50 ,52 ,53 ,82 ,83 ,
87 ,89 ,92 ,111 ,112 ,113 ,114 ,124 ,125),
   "F21" : (17 ,50 ,51 ,52 ,83 ,84 ,86 ,88 ,91 ,112 ,113 ,114 ,115
,123 ,124),
   "F22" : (51 ,84 ,85 ,87 ,90 ,113 ,114 ,115 ,116 ,122 ,123),
   "F23" : (86 ,89 ,114 ,115 ,116 ,117 ,121 ,122),
   "F24" : (85 ,88 ,115 ,116 ,117 ,118 ,120 ,121),
   "F25" : (87 ,116 ,117 ,118 ,119 ,120),
   "F26" : (86 ,117 ,118 ,119),
   "F27" : (85 ,118),
   "Frame_cnt" : 27,
   "Rate" : 0.8,
   "Timing" : (0, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,)
}

spiral = {
   "F0" : (0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,34 ,35 ,
36 ,37 ,38 ,39 ,40 ,41 ,42 ,43 ,44 ,45 ,46 ,47 ,48 ,50 ,51 ,53 ,67 ,68 ,70 ,71 ,
72 ,73 ,74 ,75 ,76 ,77 ,78 ,79 ,80 ,82 ,84 ,85 ,87 ,89 ,99 ,101 ,102 ,104 ,106 ,
114 ,116 ,118 ,119 ,121 ,123 ,124 ,125 ,126 ,127 ,128 ,129 ,130 ,131 ,133 ,135 ,
136 ,138 ,150 ,152 ,153 ,155 ,156 ,157 ,158 ,159 ,160 ,161 ,162 ,163 ,164 ,165 ,
166 ,167 ,169 ,170 ,186 ,187 ,188 ,189 ,190 ,191 ,192 ,193 ,194 ,195 ,196 ,197 ,
198 ,199 ,200 ,201 ,202 ,203),
   "F1" : (15 ,31 ,33 ,47 ,55 ,65 ,71 ,79 ,91 ,97, 19 ,31 ,35),
   "F2" : (15 ,19 ,47 ,55 ,79 ,91 ,114 ,122 ,150 ,154 ,186),
   "F3" : (108 ,114 ,122 ,130 ,140 ,150 ,154 ,166 ,172 ,186 ,202),
   "F4" : (33 ,35 ,65 ,71 ,97 ,108 ,130 ,140 ,166 ,172 ,202),
   "Frame_cnt" : 4,
   "Rate" : 0,
   "Timing" : (0, .1, .1, .1, .1)
   }

fuckYou = {
   "F0" : (17 ,20 ,22 ,23 ,26 ,29 ,31 ,32 ,33 ,34 ,38 ,41 ,43 ,47 ,49 ,
53 ,54 ,58 ,60 ,63 ,65 ,66 ,67 ,68 ,72 ,75 ,77 ,81 ,83 ,85 ,88 ,92 ,94 ,
97 ,101 ,102 ,107 ,108 ,112 ,113 ,115 ,118 ,137 ,141 ,144 ,145 ,148 ,151 ,
154 ,157 ,159 ,162 ,165 ,167 ,173 ,177 ,180 ,182 ,185 ,189 ,190 ,194 ,195 ,200),
   "F1" : (17 ,20 ,22 ,23 ,26 ,29 ,31 ,32 ,33 ,34 ,38 ,41 ,43 ,47 ,49 ,
53 ,54 ,58 ,60 ,63 ,65 ,66 ,67 ,68 ,72 ,75 ,77 ,81 ,83 ,85 ,88 ,92 ,94 ,
97 ,101 ,102 ,107 ,108 ,112 ,113 ,115 ,118 ,137 ,141 ,144 ,145 ,148 ,151 ,
154 ,157 ,159 ,162 ,165 ,167 ,173 ,177 ,180 ,182 ,185 ,189 ,190 ,194 ,195 ,200),
   "F2" :  (17 ,20 ,22 ,23 ,26 ,29 ,31 ,32 ,33 ,34 ,38 ,41 ,43 ,47 ,49 ,
53 ,54 ,58 ,60 ,63 ,65 ,66 ,67 ,68 ,72 ,75 ,77 ,81 ,83 ,85 ,88 ,92 ,94 ,
97 ,101 ,102 ,107 ,108 ,112 ,113 ,115 ,118 ,137 ,141 ,144 ,145 ,148 ,151 ,
154 ,157 ,159 ,162 ,165 ,167 ,173 ,177 ,180 ,182 ,185 ,189 ,190 ,194 ,195 ,200),
   "Frame_cnt" : 2,
   "Rate" : 0,
   "Timing" : (0, .75, 0.75)
   }

# main while true loop, starts by advertising bluetooth
while True:
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()
    # Bootup function, make sure to swap soundfile for your own if
    # you need one
    bootup("Startup.wav")
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
                        ##  1, no direction
                        setting = faceN
                        mode = 1
                    if packet.button == ButtonPacket.BUTTON_2:
                        ##  2, no direction
                        setting = eyeN
                        mode = 2
                    if packet.button == ButtonPacket.BUTTON_3:
                        ##  3, no direction
                        setting = Off
                        mode = 3
                    if packet.button == ButtonPacket.BUTTON_4:
                        ## 4, no direction
                        setting = Off
                        mode = 4
                    if packet.button == ButtonPacket.UP:
                        if mode == 1:
                            ## 1, UP
                            setting = faceHeart
                        if mode == 2:
                            ## 2, UP
                            setting = eyeLove
                        if mode == 3:
                            ## 3, UP
                            pass
                        if mode == 4:
                            ## 4, UP
                            setting = vitals
                    if packet.button == ButtonPacket.DOWN:
                        if mode == 1:
                            ## 1, DOWN
                            setting = faceCry
                        if mode == 2:
                            ## 2, DOWN
                            setting = eyePissed
                        if mode == 3:
                            ## 3, DOWN
                            setting = fuckYou
                        if mode == 4:
                            ## 4, DOWN
                            setting = loading
                    if packet.button == ButtonPacket.LEFT:
                        if mode == 1:
                            ## 1, LEFT
                            setting = faceHuh
                        if mode == 2:
                            ## 2, LEFT
                            setting = eyeFuck
                        if mode == 3:
                            ## 3, LEFT
                            pass
                        if mode == 4:
                            ## 4, LEFT
                            setting = error
                    if packet.button == ButtonPacket.RIGHT:
                        if mode == 1:
                            ## 1, RIGHT
                            setting = FaceUwU
                        if mode == 2:
                            ## 2, RIGHT
                            setting = eyeCry
                        if mode == 3:
                            ## 3, RIGHT
                            pass
                        if mode == 4:
                            ## 4, RIGHT
                            setting = lowBattery
                    print(setting)
                    on_Length = len(on)
                    print(on)

